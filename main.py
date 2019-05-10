# coding:utf-8
import sys
sys.path.append('../')
from Config.api_config import account
from AdApi.campaigns import Campaigns


if __name__ == '__main__':
    client_id = account.get('client_id')
    client_secret = account.get('client_secret')
    access_token = account.get('access_token')
    refresh_token = account.get('refresh_token')
    scope = '1223366941512513'  # us 1223366941512513 ca 4395156076169305
    params = {
        'spon': 'sp',
        'record_type': 'campaigns',
        'payload': {
            'stateFilter': 'enabled'
        }
    }

    campaign = Campaigns(client_id, client_secret, access_token, refresh_token, scope)
    campaign.do_refresh_token()
    print(campaign.list_campaigns(params).text)