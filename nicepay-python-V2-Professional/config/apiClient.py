import webbrowser

import requests


class ApiClient:

    @staticmethod
    def send(host, header, request, endpoint):
        response = requests.post(url=host + endpoint, headers=header, json=request)
        return response.json()

    @staticmethod
    def redirect(host, tXid, endpoint):
        url = f"{host}{endpoint}?tXid={tXid}"
        webbrowser.open(url)
        return url
