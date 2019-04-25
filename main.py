# encoding:utf-8
from Common.common import create_client



if __name__ == '__main__':
    params = {
        'scope': '1223366941512513', # us 1223366941512513 ca 4395156076169305
    }
    ad_client = create_client()

    # ad_client.do_refresh_token()  # 刷新Token
    # resp = ad_client.list_profiles()
    # print(resp.text)
    # if 'UNAUTHORIZED' in resp.text:
    #     ad_client.do_refresh_token()
    #     print(ad_client.list_profiles().text)
    # batch_download_reports(ad_client)
    # batch_reports_json_to_csv()