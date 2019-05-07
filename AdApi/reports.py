# encoding: utf-8
from AdApi.ad_client import AdClient
from Config.api_config import report_type


class Reports(AdClient):
    """
    报告/快照接口
    """

    def create_report(self, params):
        spon = params.get('spon')
        record_type = params.get('record_type')
        interface = '{spon}/{record_type}/report'.format(
            spon=spon,
            record_type=record_type
        )

        rp_common = '{}_common'.format(spon)
        rt = report_type.get(record_type)
        if spon == 'hsa':
            rt = rt[1:]
        metrics_list = rt + report_type.get(rp_common)
        payload = {
            'reportDate': params.get('reportDate'),
            'metrics': ','.join(metrics_list)
        }
        if ('keywords' or 'targets') in interface:
            payload['segment'] = 'query'
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def get_report(self, report_id):
        interface = 'reports/{}/download'.format(report_id)
        return self.excute_req(interface, scope=self.scope)

    def create_snapshot(self, params):
        interface = '{spon}/{record_type}/snapshot'.format(
            spon=params.get('spon'),
            record_type=params.get('record_type')
        )
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def get_snapshot(self, snapshot_id):
        interface = 'snapshots/{}/download'.format(snapshot_id)
        return self.excute_req(interface, scope=self.scope)