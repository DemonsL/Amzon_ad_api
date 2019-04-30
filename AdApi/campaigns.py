# encoding: utf-8
from AdApi.ad_client import AdClient


class Campaigns(AdClient):

    def __init__(self, client_id, client_secret, access_token, refresh_token, scope):
        self.scope = scope
        super().__init__(client_id, client_secret, access_token, refresh_token)

    # 通过id获取广告活动
    def get_campaign(self, campaign_id, params):
        interface = '{spon}/campaigns/{campaign_id}'.format(
            spon = params.get('spon'),
            campaign_id = campaign_id
        )
        return self.excute_req(interface, scope=self.scope)

    # 通过id获取广告活动及扩展字段
    def get_campaign_ex(self, campaign_id, params):
        interface = '{spon}/campaigns/extended/{campaign_id}'.format(
            spon = params.get('spon'),
            campaign_id = campaign_id
        )
        return self.excute_req(interface, scope=self.scope)

    # 创建广告活动
    def create_campaigns(self, params):
        interface = 'sp/campaigns'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    # 更新广告活动
    def update_campaigns(self, params):
        interface = '{}/campaigns'.format(params.get('spon'))
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    # 通过id删除广告活动
    def delete_campaign(self, campaign_id, params):
        interface = '{spon}/campaigns/{campaign_id}'.format(
            spon=params.get('spon'),
            campaign_id=campaign_id
        )
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    # 过滤条件返回广告活动列表
    def list_campaigns(self, params):
        interface = '{}/campaigns'.format(params.get('spon'))
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'name': params.get('name'),
            'portfolioIdFilter': params.get('portfolioIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    # 过滤条件返回广告活动列表及扩展字段
    def list_campaigns_ex(self, params):
        interface = '{}/campaigns/extended'.format(params.get('spon'))
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'name': params.get('name'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)