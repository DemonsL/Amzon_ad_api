# encoding: utf-8
from AdApi.ad_client import AdClient


class AdGroups(AdClient):
    """
    广告组接口
    """

    def get_adgroup(self, adgroup_id):
        interface = 'sp/adGroups/{}'.format(adgroup_id)
        return self.excute_req(interface, scope=self.scope)

    def get_adgroup_ex(self, adgroup_id):
        interface = 'sp/adGroups/extended/{}'.format(adgroup_id)
        return self.excute_req(interface, scope=self.scope)

    def create_adgroups(self, params):
        interface = 'sp/adGroups'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_adgroups(self, params):
        interface = 'sp/adGroups'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    def delete_adgroup(self, adgroup_id):
        interface = 'sp/adGroups/{}'.format(adgroup_id)
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    def list_adgroups(self, params):
        interface = 'sp/adGroups'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'name': params.get('name'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_adgroups_ex(self, params):
        interface = 'sp/adGroups/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'name': params.get('name'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)