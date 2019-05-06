# encoding: utf-8
from AdApi.ad_client import AdClient


class Bid(AdClient):

    # 获取广告组出价建议
    def get_bid_recommendations_for_adgroups(self, adgroup_id):
        interface = 'adGroups/{}/bidRecommendations'.format(adgroup_id)
        return self.excute_req(interface, scope=self.scope)

    # 获取关键词出价建议
    def get_bid_recommendations_for_keywords(self, keyword_id):
        interface = 'keywords/{}/bidRecommendations'.format(keyword_id)
        return self.excute_req(interface, scope=self.scope)

    # 创建关键词出价建议
    def create_keywords_bid_recommendations(self, params):
        interface = 'keywords/bidRecommendations'
        payload = {
            'adGroupId': params.get('adGroupId'),
            'keywords': params.get('keywords')
        }
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    # 更新赞助品牌扩展位置的自动出价
    def update_campaign_adgroup(self, params):
        interface = 'hsa/campaigns'
        payload = {
            'startIndex': params.get('startIndex', 0),
            'count': params.get('count', 0),
            'bidMultiplier': params.get('bidMultiplier'),
            'placementGroupId': params.get('placementGroupId'),
            'primaryAdGroupId': params.get('primaryAdGroupId')
        }
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)