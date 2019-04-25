# encoding:utf-8
import pandas as pd
from Config.api_config import account
from AdApi.AdClient import AdClient

def create_client():
    client_id = account.get('client_id')
    client_secret = account.get('client_secret')
    access_token = account.get('access_token')
    refresh_token = account.get('refresh_token')
    return AdClient(client_id, client_secret, access_token, refresh_token)


def convert_json_to_csv(json_file, file_name):
    df = pd.read_json(json_file)
    to_file_path = 'ReportFile/{}_report.csv'.format(file_name)
    df.to_csv(to_file_path)