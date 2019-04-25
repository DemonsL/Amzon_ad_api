# encoding: utf-8
import json
import gzip
import datetime
from Config.api_config import report_type
from Common.common import create_client
from Models import Reports
from Timers.TimersHandler import TimersHandler

class DownloadReports:

    def __init__(self):
        pass

    # 通过日期返回报告国别
    def get_report_country(self, table_name, report_date):
        session = Reports.DBSession()
        report_excute = eval('Reports.{}'.format(table_name))
        country = session.query(report_excute, report_excute.Country)\
                         .filter(report_excute.SnapDate==report_date)
        country = set([c[1] for c in country])
        return list(country)

    # 返回数据库报告日期
    def get_report_date(self, table_name):
        session = Reports.DBSession()
        report_excute = eval('Reports.{}'.format(table_name))
        snap_date = session.query(report_excute, report_excute.SnapDate).all()
        snap_date = set([''.join(str(d[1]).split('-')) for d in snap_date])
        return list(snap_date)

    # 保存报告到数据库
    def excute_add_report(self, json_b, table_name, country, params):
        report_json = json.loads(json_b.decode())
        snap_date = params.get('reportDate')
        report_excute = 'Reports.{}'.format(table_name)

        session = Reports.DBSession()
        for report in report_json:
            report_to_sql = eval(report_excute)(snap_date, country, report)
            session.add(report_to_sql)
        session.commit()

    # 生成报告
    def gen_reports(self, client, params):
        reports = client.create_report(params)
        # token失效时，刷新token
        if 'UNAUTHORIZED' in reports.text:
            client.do_refresh_token()
            reports = client.create_report(params)
        print('POST_RESP: ' + reports.text)
        return reports

    # 下载并解压报告
    def download_report(self, client, params):
        reports = self.gen_reports(client, params)
        reports_dict = dict(json.loads(reports.text))
        report_id = reports_dict.get('reportId', None)
        report = client.get_report(report_id, params)
        print('GET_RESP: ' + str(report.content))

        if '<xml' in report.text:
            report = client.get_report(report_id, params)
        report_byte = gzip.decompress(report.content)  # 解压缩
        return report_byte

    # 下载报告并存到数据库
    def report_to_sql(self, client, params):
        record_t = params.get('record_type')
        table_name = 'Apr' + params.get('spon').capitalize() + record_t[0].upper() + record_t[1:]
        country = params.get('mkp')
        report_date = params.get('reportDate')
        snap_dates = self.get_report_date(table_name)
        db_date = str(datetime.datetime.strptime(report_date, '%Y%m%d').date())
        report_mkp = self.get_report_country(table_name, db_date)
        print('tb:{tb}, mkp:{mkp},db_mkp:{dbm},db_date{dd}'
              .format(tb=table_name, mkp=country, dbm=report_mkp, dd=snap_dates))

        if (not snap_dates) or (report_date not in snap_dates) or (country not in report_mkp):
            report_byte = self.download_report(client, params)
            self.excute_add_report(report_byte, table_name, country, params)

    # 批量下载报告
    def batch_download_reports(self, client):
        rp_scope = report_type.get('rp_scope')
        report_date = datetime.datetime.now()
        report_date -= datetime.timedelta(days=2)
        report_date = report_date.strftime('%Y%m%d')
        print(report_date)
        params = {
            'reportDate': str(report_date)
        }
        for scope in rp_scope:            # marketplace
            params['mkp'] = scope[:2]
            params['scope'] = scope[2:]
            for rp_type in report_type.get('type'):      # sp or hsa
                params['spon'] = rp_type
                rc_type_list = report_type.get(rp_type)
                for rc_type in rc_type_list:              # reportType
                    params['record_type'] = rc_type
                    self.report_to_sql(client, params)


if __name__ == '__main__':
    ad_client = create_client()
    dw_report = DownloadReports()
    timer = datetime.datetime(2019, 4, 25, 14, 19)
    timer = timer.strftime('%Y-%m-%d %H:%M')
    dw_report_timer = TimersHandler(timer,
                                    ad_client,
                                    dw_report.batch_download_reports)
    dw_report_timer.set_timer()


    # re_date = 20190401
    # while re_date < 20190422:
    #     dw_report.batch_download_reports(ad_client, str(re_date))
    #     re_date += 1
    #     print('Date: '+ str(re_date))
    # print('Successful!')
