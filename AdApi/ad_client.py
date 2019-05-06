# encoding:utf-8
import json
import requests
from Config.api_config import api_version, regions, oauth_url

class AdClient:

    def __init__(self, client_id, client_secret, access_token, refresh_token, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = access_token
        self.refresh_token = refresh_token
        self.scope = scope

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
        if method == 'GET':
            resp = requests.get(url, headers=headers)
            if payload:
                resp = requests.get(url, headers=headers, params=payload)
            return resp
        elif method == 'POST':
            resp = requests.post(url, headers=headers)
            if payload:
                resp = requests.post(url, headers=headers, data=json.dumps(payload))
            return resp
        elif method == 'PUT':
            resp = requests.put(url, headers=headers)
            if payload:
                resp = requests.put(url, headers=headers, params=payload)
            return resp
        elif method == 'DELETE':
            return requests.delete(url, headers=headers)

