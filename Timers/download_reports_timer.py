# coding: utf-8
import sys
sys.path.append('../')
import json
import gzip
import time
import datetime
from Models import reports
from AdApi.reports import Reports
from Config.api_config import report_type, account
from Timers.timers_handler import TimersHandler

class DownloadReports:
    """
    定时批量下载报告
    """

    def get_report_country_for_date(self, table_name, report_date):
        session = reports.DBSession()
        report_excute = eval('reports.{}'.format(table_name))
        mkps = session.query(report_excute, report_excute.Country)\
                      .filter_by(SnapDate=report_date).all()
        mkps = set([(m[1]) for m in mkps])
        return list(mkps)

    def get_report_date(self, table_name):
        session = reports.DBSession()
        report_excute = eval('reports.{}'.format(table_name))
        snap_report = session.query(report_excute, report_excute.SnapDate).all()
        snap_date = set([''.join(str(d[1]).split('-')) for d in snap_report])
        return list(snap_date)

    def del_reports_for_date(self, table_name, snap_date, country):
        session = reports.DBSession()
        report_excute = eval('reports.{}'.format(table_name))
        records = session.query(report_excute).filter_by(SnapDate=snap_date,
                                                         Country=country).all()
        for record in records:
            session.delete(record)
        session.commit()

    def add_report_to_sql(self, json_b, table_name, country, params):
        report_json = json.loads(json_b.decode())
        snap_date = params.get('reportDate')
        report_excute = 'reports.{}'.format(table_name)

        session = reports.DBSession()
        for report in report_json:
            report_to_sql = eval(report_excute)(snap_date, country, report)
            session.add(report_to_sql)
        session.commit()

    def gen_reports(self, client, params):
        reports = client.create_report(params)
        # token失效时，刷新token
        if 'UNAUTHORIZED' in reports.text:
            client.do_refresh_token()
            reports = client.create_report(params)
        print('POST_RESP: ' + reports.text)
        return reports

    def download_report(self, client, params):
        reports = self.gen_reports(client, params)
        reports_dict = dict(json.loads(reports.text))
        report_id = reports_dict.get('reportId', None)
        if report_id:
            time.sleep(15)                          # 下载报告前，需要报告生成成功
            report = client.get_report(report_id)

            try:
                report = gzip.decompress(report.content)  # 解压缩
            except Exception as e:
                print('Decompress Error: ' + str(e))
            return report

    def report_to_sql(self, client, params):
        record_t = params.get('record_type')
        table_name = 'Apr' + params.get('spon').capitalize() + record_t[0].upper() + record_t[1:]
        country = params.get('mkp')
        report_date = params.get('reportDate')
        # 删除旧数据
        snap_dates = self.get_report_date(table_name)
        mkps = self.get_report_country_for_date(table_name, report_date)
        if (report_date in snap_dates) and (country in mkps):
            try:
                print('delete old data...')
                self.del_reports_for_date(table_name, report_date, country)
            except Exception as e:
                print('DeleteSqlError: ' + str(e))
        # 添加新数据
        report_byte = self.download_report(client, params)
        try:
            self.add_report_to_sql(report_byte, table_name, country, params)
        except Exception as e:
            print('AddSqlError: ' + str(e))

    def batch_download_reports(self, client, params):
        for rp_type in report_type.get('type'):      # sp or hsa
            params['spon'] = rp_type
            rc_type_list = report_type.get(rp_type)
            for rc_type in rc_type_list:              # reportType
                params['record_type'] = rc_type
                self.report_to_sql(client, params)

    def run(self, client, params):
        print('Report download start...')
        client.do_refresh_token()
        interval_day = 2
        while interval_day < 62:    # 更新前30天内报告数据
            report_date = datetime.datetime.now()
            report_date -= datetime.timedelta(days=interval_day)
            report_date = report_date.strftime('%Y%m%d')
            print(report_date)
            params['reportDate'] = str(report_date)
            self.batch_download_reports(client, params)
            interval_day += 1
        print('Report download end!')


def get_clients():
    client_id = account.get('client_id')
    client_secret = account.get('client_secret')
    access_token = account.get('access_token')
    refresh_token = account.get('refresh_token')
    rp_scope = report_type.get('rp_scope')
    clients = []
    for scope in rp_scope:  # marketplace
        params = {}
        params['mkp'] = scope[:2]
        params['scope'] = scope[2:]
        report_client = Reports(client_id, client_secret, access_token, refresh_token, params['scope'])
        clients.append([report_client, params])
    return clients


if __name__ == '__main__':
    dw_report = DownloadReports()
    args = get_clients()

    # timer = datetime.datetime(2019, 5, 8, 16, 15)
    dw_report_timer = TimersHandler(datetime.datetime.now() + datetime.timedelta(minutes=1), dw_report.run, args)
    dw_report_timer.excute_job()

