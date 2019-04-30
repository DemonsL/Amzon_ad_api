# encoding: utf-8
from AdApi.ad_client import AdClient


class Targets(AdClient):

    def __init__(self, client_id, client_secret, access_token, refresh_token, scope):
        self.scope = scope
        super().__init__(client_id, client_secret, access_token, refresh_token)

    def get_targeting_clause(self, target_id):
        interface = 'sp/targets/{}'.format(target_id)
        return self.excute_req(interface, scope=self.scope)

    def get_targeting_clause_ex(self, target_id):
        interface = 'sp/targets/extended/{}'.format(target_id)
        return self.excute_req(interface, scope=self.scope)

    def list_targeting_clause(self, params):
        interface = 'sp/targets'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_targeting_clause_ex(self, params):
        interface = 'sp/targets/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'campaignType': params.get('campaignType'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def create_targeting_clause(self, params):
        interface = 'sp/targets'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_targeting_clause(self, params):
        interface = 'sp/targets'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    def delete_targeting_clause(self, target_id):
        interface = 'sp/targets/{}'.format(target_id)
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    def create_target_recommendations(self, params):
        interface = 'sp/targets/productRecommendations'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def get_targeting_categories(self, params):
        interface = 'sp/targets/categories'
        payload = {
            'asins': params.get('asins')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_brand_recommendations(self, params):
        interface = 'sp/targets/brands'
        payload = {
            'keyword': params.get('keyword'),
            'categoryId': params.get('categoryId')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_negative_targeting_clause(self, target_id):
        interface = 'sp/negativeTargets/{}'.format(target_id)
        return self.excute_req(interface, scope=self.scope)

    def get_negative_targeting_clause_ex(self, target_id):
        interface = 'sp/negativeTargets/extended/{}'.format(target_id)
        return self.excute_req(interface, scope=self.scope)

    def create_negative_targeting_clauses(self, params):
        interface = 'sp/negativeTargets'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_negative_targeting_clauses(self, params):
        interface = 'sp/negativeTargets'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    def list_negative_targeting_clauses(self, params):
        interface = 'sp/negativeTargets'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_negative_targeting_clauses_ex(self, params):
        interface = 'sp/negativeTargets/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'campaignType': params.get('campaignType'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def delete_negative_targeting_clause(self, target_id):
        interface = 'sp/negativeTargets/{}'.format(target_id)
        return self.excute_req(interface, scope=self.scope)

