import os

import requests

admin_server_path = "admin2/master_accounts"


class AdminServer:
    def __init__(self, base_uri: str, headers: dict):
        self.base_uri = os.path.join(base_uri, admin_server_path)
        self.headers = headers

    def get_all_master_accounts(self, cutodian_token):
        uri = os.path.join(self.base_uri, "?custodian=" + cutodian_token)
        response = requests.get(
            uri, headers=self.headers, verify=False
        )
        return response

    def get_master_account(self, master_account_id):
        uri = os.path.join(self.base_uri, master_account_id)
        response = requests.get(
            uri, headers=self.headers, verify=False
        )
        return response

    def create_and_link_master_accounts(self, firm_id):
        uri = os.path.join(self.base_uri,
                           "create_and_link_master_accounts", firm_id)
        response = requests.post(
            uri, headers=self.headers, verify=False
        )
        return response

    def create_link(self):
        uri = os.path.join(self.base_uri, "firm_link")
        response = requests.post(
            uri, headers=self.headers, verify=False
        )
        return response

    def update_link(self, master_account_link_id):
        uri = os.path.join(self.base_uri, admin_server_path,
                           "firm_link", master_account_link_id)
        response = requests.put(
            uri, headers=self.headers, verify=False
        )
        return response

    def delete_link(self, master_account_link_id):
        uri = os.path.join(self.base_uri, "firm_link", master_account_link_id)
        response = requests.delete(
            uri, headers=self.headers, verify=False
        )
        return response

    def delete(self, master_account_id):
        uri = os.path.join(self.base_uri, master_account_id)
        response = requests.delete(
            uri, headers=self.headers, verify=False
        )
        return response
