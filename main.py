# coding:utf-8
import sys
sys.path.append('../')
from Config.api_config import account, ad_api_type
from AdApi.profiles import Profiles
from AdApi.portfolios import Portfolios
from AdApi.campaigns import Campaigns
from AdApi.adgroups import AdGroups
from AdApi.productads import ProductAds
from AdApi.keywords import Keywords
from AdApi.targets import Targets
from flask import Flask, request as flask_req

app = Flask(__name__)


def set_token(ad_type):
    client_id = account.get('client_id')
    client_secret = account.get('client_secret')
    access_token = account.get('access_token')
    refresh_token = account.get('refresh_token')
    scope = '1223366941512513'  # us 1223366941512513 ca 4395156076169305
    ad = ad_type(client_id, client_secret, access_token, refresh_token, scope)
    ad.do_refresh_token()
    return ad

def request_url(spon_type, ad_type, api_type, ad_id=None):
    params = {
        'spon': spon_type
    }
    ad_api = ad_api_type.get(ad_type)
    ad = set_token(eval(ad_api[0]))
    inter = ''
    if ('get' in api_type) or ('delete' in api_type):
        if ad_type in ['campaigns', 'keywords']:
            inter = 'ad.{}(ad_id, params).text'
        else:
            inter = 'ad.{}(ad_id).text'
    if 'list' in api_type:
        for k, v in flask_req.args.items():
            params[k] = v
            inter = 'ad.{}(params).text'
    if ('create' in api_type) or ('update' in api_type):
        payload = flask_req.form
        params['payload'] = payload
        inter = 'ad.{}(params).text'
    return eval(inter.format(ad_api[1].get(api_type)))

@app.route('/v2/<spon_type>/<ad_type>/<ad_id>/', methods=['DELETE', 'GET'])
def get_or_delete_ad(spon_type, ad_type, ad_id):
    if flask_req.method == 'DELETE':
        api_type = 'api_delete'
    else:
        api_type = 'api_get'
    return request_url(spon_type, ad_type, api_type, ad_id)

@app.route('/v2/<spon_type>/<ad_type>/extended/<ad_id>/')
def get_ad_ex(spon_type, ad_type, ad_id):
    api_type = 'api_get_ex'
    return request_url(spon_type, ad_type, api_type, ad_id)

@app.route('/v2/<spon_type>/<ad_type>/', methods=['POST', 'PUT', 'GET'])
def list_or_update_ads(spon_type, ad_type):
    if flask_req.method == 'POST':
        api_type = 'api_create'
    elif flask_req.method == 'PUT':
        api_type = 'api_update'
    else:
        api_type = 'api_list'
    return request_url(spon_type, ad_type, api_type)

@app.route('/v2/<spon_type>/<ad_type>/extended/')
def list_ads_ex(spon_type, ad_type):
    api_type = 'api_list_ex'
    return request_url(spon_type, ad_type, api_type)




if __name__ == "__main__":

    app.run(host='0.0.0.0', port=7003)