# encoding: utf-8
import sys
sys.path.append('../')
import json
import gzip
import datetime
from Models import reports
from AdApi.reports import Reports
from Config.api_config import report_type, account
from Timers.timers_handler import TimersHandler

class DownloadReports:

    # 通过日期返回报告国别
    def get_report_country(self, table_name, report_date):
        session = reports.DBSession()
        report_excute = eval('reports.{}'.format(table_name))
        country = session.query(report_excute, report_excute.Country)\
                         .filter(report_excute.SnapDate==report_date).all()
        country = set([c[1] for c in country])
        return list(country)

    # 返回数据库报告日期
    def get_report_date(self, table_name):
        session = reports.DBSession()
        report_excute = eval('reports.{}'.format(table_name))
        snap_date = session.query(report_excute, report_excute.SnapDate).all()
        snap_date = set([''.join(str(d[1]).split('-')) for d in snap_date])
        return list(snap_date)

    def del_reports_for_date(self, table_name, report_date):
        session = reports.DBSession()
        report_excute = eval('reports.{}'.format(table_name))
        records = session.query(report_excute).filter_by(SnapDate=report_date).all()
        for rec in records:
            session.delete(rec)
        session.commit()

    # 保存报告到数据库
    def excute_add_report(self, json_b, table_name, country, params):
        report_json = json.loads(json_b.decode())
        snap_date = params.get('reportDate')
        report_excute = 'reports.{}'.format(table_name)

        session = reports.DBSession()
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
        report = client.get_report(report_id)
        print('GET_RESP:{}' + report.text)

        report_byte = gzip.decompress(report.content)  # 解压缩
        return report_byte

    # 下载报告并存到数据库
    def report_to_sql(self, client, params):
        record_t = params.get('record_type')
        table_name = 'Apr' + params.get('spon').capitalize() + record_t[0].upper() + record_t[1:]
        country = params.get('mkp')
        report_date = params.get('reportDate')
        snap_dates = self.get_report_date(table_name)

        if report_date in snap_dates:
            try:
                self.del_reports_for_date(table_name, report_date)
            except Exception as e:
                print(e)
        try:
            report_byte = self.download_report(client, params)
            self.excute_add_report(report_byte, table_name, country, params)
        except Exception as e:
            print(e)

    # 批量下载报告
    def batch_download_reports(self, client, params):
        for rp_type in report_type.get('type'):      # sp or hsa
            params['spon'] = rp_type
            rc_type_list = report_type.get(rp_type)
            for rc_type in rc_type_list:              # reportType
                params['record_type'] = rc_type
                self.report_to_sql(client, params)

    def run(self, client, params):
        report_date = datetime.datetime.now()
        interval_day = 2
        while interval_day < 32:    # 更新前30天内报告数据
            report_date -= datetime.timedelta(days=interval_day)
            report_date = report_date.strftime('%Y%m%d')
            print(report_date)
            params['reportDate'] = str(report_date)
            self.batch_download_reports(client, params)
            interval_day += 1




if __name__ == '__main__':
    client_id = account.get('client_id')
    client_secret = account.get('client_secret')
    access_token = account.get('access_token')
    refresh_token = account.get('refresh_token')
    rp_scope = report_type.get('rp_scope')
    params = {}
    for scope in rp_scope:  # marketplace
        params['mkp'] = scope[:2]
        params['scope'] = scope[2:]

        report = Reports(client_id, client_secret, access_token, refresh_token, params['scope'])
        dw_report = DownloadReports()
        timer = datetime.datetime(2019, 5, 5, 16, 28).strftime('%Y-%m-%d %H:%M')
        dw_report_timer = TimersHandler(timer, report, dw_report.run, params)
        dw_report_timer.set_timer()


        # re_date = 20190309
        # while re_date < 20190310:
        #     dw_report.run(report, params, str(re_date))
        #     re_date += 1
        # print('Successful!')
