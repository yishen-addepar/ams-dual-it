import os

import requests

api_server_path = "public/master_accounts"


class AdminServer:
    def __init__(self, base_uri: str, headers: dict):
        self.base_uri = os.path.join(self.base_uri, api_server_path)
        self.headers = headers

    def get_all_master_accounts(self, cutodian_token):
        uri = os.path.join(self.base_uri, "?custodian=" + cutodian_token)
        response = requests.get(
            uri, headers=self.headers, verify=False
        )
        return response

    def create_master_accounts_for_firm(self, json):
        uri = os.path.join(self.base_uri, api_server_path)
        response = requests.post(
            uri, headers=self.headers, verify=False, json=json
        )
        return response

    def delete_master_accounts_for_firm(self, master_account_id):
        uri = os.path.join(self.base_uri, master_account_id)
        response = requests.delete(
            uri, headers=self.headers, verify=False
        )
        return response
