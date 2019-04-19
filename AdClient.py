# coding:utf-8
import json
import requests
from Config.api_config import api_version, regions, oauth_url, report_type

class Client(object):

    def __init__(self, client_id, client_secret, access_token, refresh_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = access_token
        self.refresh_token = refresh_token

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    # 刷新访问令牌
    def do_refresh_token(self):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'grant_type' : 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token
        }
        resp =  requests.post(oauth_url,
                              headers = headers,
                              data = json.dumps(data))
        self._access_token = dict(resp.json()).get('access_token')

    # 获取配置文件列表
    def list_profiles(self):
        interface = 'profiles'
        return self.excute_req(interface)

    # 通过配置文件id获取配置文件
    def get_profile(self, profile_id):
        interface = 'profiles/{}'.format(profile_id)
        return self.excute_req(interface)

    # 创建赞助商品/赞助品牌报告
    def create_report(self, params):
        scope = params.get('scope')
        record_type = params.get('record_type')
        interface = '{spon}/{record_type}/report'.format(
            spon=params.get('spon'),
            record_type = record_type
        )

        metrics_list = report_type.get(record_type) + report_type.get('common')
        payload = {
            'segment': 'query',
            'reportDate': '20190401',
            'metrics': ','.join(metrics_list)
        }
        return self.excute_req(interface, method='POST',scope=scope, payload=payload)

    # 下载报告
    def get_report(self, report_id, params):
        scope = params.get('scope')
        interface = 'reports/{}/download'.format(report_id)
        return self.excute_req(interface, scope=scope)

    # 执行请求操作
    def excute_req(self, interface, method='GET', scope=None, payload=None):
        headers = {
            'Content-Type': 'application/json',
            'Amazon-Advertising-API-ClientId': self.client_id,
            'Authorization': 'Bearer {}'.format(self._access_token)
        }
        host = regions.get('na')
        url = 'https://{host}/{version}/{interface}'.format(
            host=host,
            version=api_version,
            interface=interface
        )
        print(method + ' '+ url)
        if scope:
            headers['Amazon-Advertising-API-Scope'] = scope
        if method == 'POST':
            return requests.post(url, headers=headers, data=json.dumps(payload))
        return requests.get(url, headers=headers)
