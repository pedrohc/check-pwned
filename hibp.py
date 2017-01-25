import requests
import json

class hibp:
    """Class for the haveibeenpwned.com database API"""
    def __init__(self):
        self.site = "https://haveibeenpwned.com/api/v2/breachedaccount/"

    def get_account(self, account=""):
        """Makes the GET request to the database"""
        self.name=account
        self.url = self.site + self.name
        return requests.get(self.url)

    def check(self, account=""):
        self.name=account
        self.response = self.get_account(self.name)
        if self.response.text:
            self.t = json.loads(self.response.text)
            print(self.name +  ' - PWNED\n')
            print(self.t)
        else:
            print(self.name + ' - CLEAN')

