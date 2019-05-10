# coding: utf-8
from AdApi.ad_client import AdClient


class Portfolios(AdClient):
    """
    广告组合接口
    """

    def list_portfolios(self, params):
        interface = 'portfolios'
        payload = {
            'portfolioIdFilter': params.get('portfolioIdFilter'),
            'portfolioNameFilter': params.get('portfolioNameFilter'),
            'portfolioStateFilter': params.get('portfolioStateFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def list_portfolios_ex(self, params):
        interface = 'portfolios/extended'
        payload = {
            'portfolioIdFilter': params.get('portfolioIdFilter'),
            'portfolioNameFilter': params.get('portfolioNameFilter'),
            'portfolioStateFilter': params.get('portfolioStateFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    def get_portfolio(self, portfolio_id):
        interface = 'portfolios/{}'.format(portfolio_id)
        return self.excute_req(interface, scope=self.scope)

    def get_portfolio_ex(self, portfolio_id):
        interface = 'portfolios/extended/{}'.format(portfolio_id)
        return self.excute_req(interface, scope=self.scope)

    def create_portfolios(self, params):
        interface = 'portfolios'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    def update_portfolios(self, params):
        interface = 'portfolios'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)