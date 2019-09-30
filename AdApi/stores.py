# coding: utf-8
from AdApi.ad_client import AdClient


class Stores(AdClient):
    """
    商店接口
    """

    def get_store(self, brand_entity_id):
        interface = 'stores/{brand_entity_id}'.format(
            brand_entity_id=brand_entity_id
        )
        return self.excute_req(interface)

    def list_stores(self, params):
        interface = 'stores'
        return self.excute_req(interface)