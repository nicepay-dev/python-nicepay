import json
import urllib.parse
import webbrowser

import requests
from bs4 import BeautifulSoup


class apiClient:

    @staticmethod
    def send(host, header, request, endpoint):
        response = requests.post(url=host + endpoint, headers=header, json=request)
        return response.json()

    @staticmethod
    def get(host, request, endpoint):
        data = urllib.parse.urlencode(request)
        webbrowser.open(f"{host}{endpoint}?{data}")

    @staticmethod
    def sendUrl(host, request, endpoint):
        response = requests.post(url=host + endpoint, data=request)
        return response.json()
