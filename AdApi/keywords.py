# encoding: utf-8
from AdApi.ad_client import AdClient


class Keywords(AdClient):

    def __init__(self, client_id, client_secret, access_token, refresh_token, scope):
        self.scope = scope
        super().__init__(client_id, client_secret, access_token, refresh_token)

    def get_biddable_keyword(self, keyword_id, params):
        interface = '{spon}/keywords/{kid}'.format(
            spon = params.get('spon'),
            kid = keyword_id
        )
        return self.excute_req(interface, scope=self.scope)

    def get_biddable_keyword_ex(self, keyword_id, params):
        interface = '{spon}/keywords/extended/{kid}'.format(
            spon = params.get('spon'),
            kid = keyword_id
        )
        return self.excute_req(interface, scope=self.scope)

    def create_biddable_keywords(self, params):
        interface = '{}/keywords'.format(params.get('spon'))
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_biddable_keywords(self, params):
        interface = '{}/keywords'.format(params.get('spon'))
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    def delete_biddable_keyword(self, keyword_id, params):
        interface = '{spon}/keywords/{kid}'.format(
            spon=params.get('spon'),
            kid=keyword_id
        )
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    def list_biddable_keywords(self, params):
        interface = 'sp/keywords'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_biddable_keywords_ex(self, params):
        interface = 'sp/keywords/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'campaignType': params.get('campaignType'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter'),
            'keywordIdFilter': params.get('keywordIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_negative_keyword(self, keyword_id):
        interface = 'sp/negativeKeywords/{}'.format(keyword_id)
        return self.excute_req(interface, scope=self.scope)

    def get_negative_keyword_ex(self, keyword_id):
        interface = 'sp/negativeKeywords/extended/{}'.format(keyword_id)
        return self.excute_req(interface, scope=self.scope)

    def create_negative_keywords(self, params):
        interface = 'sp/negativeKeywords'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_negative_keywords(self, params):
        interface = 'sp/negativeKeywords'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    def delete_negative_keyword(self, keyword_id):
        interface = 'sp/negativeKeywords/{}'.format(keyword_id)
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    def list_negative_keywords(self, params):
        interface = 'sp/negativeKeywords'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_negative_keywords_ex(self, params):
        interface = 'sp/negativeKeywords/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'stateFilter': params.get('stateFilter'),
            'campaignIdFilter': params.get('campaignIdFilter'),
            'adGroupIdFilter': params.get('adGroupIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_campaign_negative_keyword(self, keyword_id):
        interface = 'sp/campaignNegativeKeywords/{}'.format(keyword_id)
        return self.excute_req(interface, scope=self.scope)

    def get_campaign_negative_keyword_ex(self, keyword_id):
        interface = 'sp/campaignNegativeKeywords/extended/{}'.format(keyword_id)
        return self.excute_req(interface, scope=self.scope)

    def create_campaign_negative_keywords(self, params):
        interface = 'sp/campaignNegativeKeywords'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_campaign_negative_keywords(self, params):
        interface = 'sp/campaignNegativeKeywords'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)

    def delete_campaign_negative_keyword(self, keyword_id):
        interface = 'sp/campaignNegativeKeywords{}'.format(keyword_id)
        return self.excute_req(interface, method='DELETE', scope=self.scope)

    def list_campaign_negative_keywords(self, params):
        interface = 'sp/campaignNegativeKeywords/'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_campaign_negative_keywords_ex(self, params):
        interface = 'sp/campaignNegativeKeywords/extended'
        payload = {
            'startIndex': params.get('startIndex'),
            'count': params.get('count'),
            'matchTypeFilter': params.get('matchTypeFilter'),
            'keywordText': params.get('keywordText'),
            'campaignIdFilter': params.get('campaignIdFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_adgroup_suggested_keywords(self, adgroup_id, params):
        interface = 'adGroups/{}/suggested/keywords'.format(adgroup_id)
        payload = {
            'maxNumSuggestions': params.get('maxNumSuggestions'),
            'adStateFilter': params.get('adStateFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_adgroup_suggested_keywords_ex(self, adgroup_id, params):
        interface = 'adGroups/{}/suggested/keywords/extended'.format(adgroup_id)
        payload = {
            'maxNumSuggestions': params.get('maxNumSuggestions'),
            'adStateFilter': params.get('adStateFilter'),
            'suggestBids': params.get('suggestBids')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_asin_suggested_keywords(self, asin, params):
        interface = 'asins/{}/suggested/keywords'.format(asin)
        payload = {
            'maxNumSuggestions': params.get('maxNumSuggestions')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def bulk_get_asin_suggested_keywords(self, params):
        interface = 'asins/suggested/keywords'
        payload = {
            'maxNumSuggestions': params.get('maxNumSuggestions')
        }
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)





