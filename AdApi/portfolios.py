# encoding: utf-8
from AdApi.ad_client import AdClient


class Portfolios(AdClient):

    def __init__(self, client_id, client_secret, access_token, refresh_token, scope):
        self.scope = scope
        super().__init__(client_id, client_secret, access_token, refresh_token)

    # 获取广告组合列表
    def list_portfolios(self, params):
        interface = 'portfolios'
        payload = {
            'portfolioIdFilter': params.get('portfolioIdFilter'),
            'portfolioNameFilter': params.get('portfolioNameFilter'),
            'portfolioStateFilter': params.get('portfolioStateFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    # 获取广告组合列表及扩展
    def list_portfolios_ex(self, params):
        interface = 'portfolios/extended'
        payload = {
            'portfolioIdFilter': params.get('portfolioIdFilter'),
            'portfolioNameFilter': params.get('portfolioNameFilter'),
            'portfolioStateFilter': params.get('portfolioStateFilter')
        }
        return self.excute_req(interface, scope=self.scope, payload=payload)

    # 通过id获取广告组合
    def get_portfolio(self, portfolio_id):
        interface = 'portfolios/{}'.format(portfolio_id)
        return self.excute_req(interface, scope=self.scope)

    # 通过id获取广告组合及扩展
    def get_portfolio_ex(self, portfolio_id):
        interface = 'portfolios/extended/{}'.format(portfolio_id)
        return self.excute_req(interface, scope=self.scope)

    # 创建广告组合
    def create_portfolios(self, params):
        interface = 'portfolios'
        payload = params.get('payload')
        return self.excute_req(interface, method='POST', scope=self.scope, payload=payload)

    # 更新广告组合
    def update_portfolios(self, params):
        interface = 'portfolios'
        payload = params.get('payload')
        return self.excute_req(interface, method='PUT', scope=self.scope, payload=payload)