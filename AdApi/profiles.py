# coding: utf-8
from AdApi.ad_client import AdClient


class Profiles(AdClient):
    """
    配置文件接口
    """

    def get_profile(self, profile_id):
        interface = 'profiles/{profile_id}'.format(
            profile_id = profile_id
        )
        return self.excute_req(interface)

    def list_profiles(self, params):
        interface = 'profiles'
        return self.excute_req(interface)

    def update_profiles(self, params):
        interface = 'profiles'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', payload=payload)