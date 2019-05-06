# encoding: utf-8
from AdApi.ad_client import AdClient


class AdGroups(AdClient):

    # 通过id获取广告组
    def get_adgroup(self, adgroup_id):
        interface = 'sp/adGroups/{}'.format(adgroup_id)
        return self.excute_req(interface, scope=self.scope)

    # 通过id获取广告组及扩展信息
    def get_adgroup_ex(self, adgroup_id):
        interface = 'sp/adGroups/extended/{}'.format(adgroup_id)
        return self.excute_req(interface, scope=self.scope)

    # 创建广告组
    def create_adgroups(self, params):
        interface = 'sp/adGroups'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    # 更新广告组
    def update_adgroups(self, params):
        interface = 'sp/adGroups'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    # 通过id删除广告组
    def delete_adgroup(self, adgroup_id):
        interface = 'sp/adGroups/{}'.format(adgroup_id)
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    # 过滤条件返回广告组列表
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

    # 过滤条件返回广告组列表及扩展信息
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