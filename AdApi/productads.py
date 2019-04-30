# encoding: utf-8
from AdApi.ad_client import AdClient


class ProductAds(AdClient):

    def __init__(self, client_id, client_secret, access_token, refresh_token, scope):
        self.scope = scope
        super().__init__(client_id, client_secret, access_token, refresh_token)

    # 通过id获取商品广告
    def get_productad(self, adid):
        interface = 'sp/productAds/{}'.format(adid)
        return self.excute_req(interface, scope=self.scope)

    # 通过id获取商品广告及扩展
    def get_productad_ex(self, adid):
        interface = 'sp/productAds/extended/{}'.format(adid)
        return self.excute_req(interface, scope=self.scope)

    # 创建商品广告
    def create_productad(self, params):
        interface = 'sp/productAds'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    # 更新商品广告
    def update_productad(self, params):
        interface = 'sp/productAds'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    # 删除商品广告
    def delete_productad(self, adid):
        interface = 'sp/productAds/{}'.format(adid)
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    # 过滤返回商品广告信息
    def list_productads(self, params):
        interface = 'sp/productAds'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'sku': params.get('sku'),
            'asin': params.get('asin'),
            'stateFilter': params.get('stateFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    # 过滤返回商品广告及扩展信息
    def list_productads_ex(self, params):
        interface = 'sp/productAds/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'adGroupId': params.get('adGroupId'),
            'sku': params.get('sku'),
            'asin': params.get('asin'),
            'stateFilter': params.get('stateFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)