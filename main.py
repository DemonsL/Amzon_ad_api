# coding:utf-8
import sys
sys.path.append('../')
from Config.api_config import account, ad_api_type
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
    if ad_id:
        if ad_type in ['campaigns', 'keywords']:
            resp = eval('ad.{}(ad_id, params).text'.format(ad_api[1].get(api_type)))
        else:
            resp = eval('ad.{}(ad_id).text'.format(ad_api[1].get(api_type)))
    else:
        for k, v in flask_req.args.items():
            params[k] = v
        resp = eval('ad.{}(params).text'.format(ad_api[1].get(api_type)))
    return resp

@app.route('/v2/<spon_type>/<ad_type>/<ad_id>/')
def get_ad(spon_type, ad_type, ad_id):
    api_type = 'api_get'
    return request_url(spon_type, ad_type, api_type, ad_id)

@app.route('/v2/<spon_type>/<ad_type>/extended/<ad_id>/')
def get_ad_ex(spon_type, ad_type, ad_id):
    api_type = 'api_get_ex'
    return request_url(spon_type, ad_type, api_type, ad_id)

@app.route('/v2/<spon_type>/<ad_type>/')
def list_ads(spon_type, ad_type):
    api_type = 'api_list'
    return request_url(spon_type, ad_type, api_type)

@app.route('/v2/<spon_type>/<ad_type>/extended/')
def list_ads_ex(spon_type, ad_type):
    api_type = 'api_list_ex'
    return request_url(spon_type, ad_type, api_type)

# @app.route('/v2/<spon_type>/<ad_type>/', methods=['POST', 'PUT'])
# def update_ads(spon_type, ad_type):





if __name__ == "__main__":

    app.run(host='0.0.0.0', port=6666)