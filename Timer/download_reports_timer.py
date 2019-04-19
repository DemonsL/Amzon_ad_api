# coding: utf-8
import json
import datetime
from Config.api_config import report_type
from CommonMethod.common import create_client, convert_json_to_csv

def download_report(client, params):
    reports = client.create_report(params)
    # token失效时，刷新token
    if 'UNAUTHORIZED' in reports.text:
        client.do_refresh_token()
        reports = client.create_report(params)

    report_id = dict(json.loads(reports.text)).get('reportId', None)
    if report_id:
        report = client.get_report(report_id, params)
        report_name = params.get('spon') + '_' + params.get('record_type')
        file_name = 'ReportFile/{}_report.json.gz'.format(report_name)
        with open(file_name, 'wb') as f:
            f.write(report.content)

def batch_download_reports(client):
    rp_scope = ['1223366941512513', '4395156076169305']
    params = {}
    for scope in rp_scope:
        params['scope'] = scope
        for rp_type in report_type.get('type'):
            params['spon'] = rp_type
            rc_type_list = report_type.get(rp_type)
            for rc_type in rc_type_list:
                params['record_type'] = rc_type
                download_report(client, params)

def batch_reports_json_to_csv():
    for rp in report_type.get('type'):
        rc_type_list = report_type.get(rp)
        for rc_type in rc_type_list:
            file_name = rp + '_'+ rc_type
            file_path = 'ReportFile/{}_report.json'.format(file_name)
            with open(file_path, encoding='utf-8') as f:
                convert_json_to_csv(f, file_name)

def set_timer(timer, client):
    flag = 0
    while True:
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M')
        if now == timer:
            batch_download_reports(client)
            flag = 1
        else:
            if flag == 1:
                timer = datetime.datetime.strptime(timer, '%Y-%m-%d %H:%M')
                timer += datetime.timedelta(hours=8)
                flag = 0


if __name__ == '__main__':
    print('Download Report is running...')
    timer = datetime.datetime(2019,4,17,11,11)
    timer = timer.strftime('%Y-%m-%d %H:%M')

    ad_client = create_client()
    set_timer(timer, ad_client)
