# from typing import Any
import requests


class postVirtualAccountReq:

    @staticmethod
    def getToken(url, header, request):
        endpoint = "/v1.0/access-token/b2b"
        response = requests.post(url=url + endpoint, headers=header, json=request)
        return response.json(), endpoint

    @staticmethod
    def createVA(url, header, request):
        endpoint = "/api/v1.0/transfer-va/create-va"
        response = requests.post(url=url + endpoint, headers=header, json=request)
        return response.json(), endpoint

    @staticmethod
    def inquiryVA(url, header, request):
        endpoint = "/api/v1.0/transfer-va/status"
        response = requests.post(url=url + endpoint, headers=header, json=request)
        return response.json(), endpoint

    @staticmethod
    def getEndpoint(method):
        if method == 'getToken':
            return "/v1.0/access-token/b2b"
        elif method == 'createVA':
            return "/api/v1.0/transfer-va/create-va"
        else:
            return "/api/v1.0/transfer-va/status"
