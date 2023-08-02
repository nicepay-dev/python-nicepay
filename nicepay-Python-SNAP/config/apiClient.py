import requests


class apiClient:

    @staticmethod
    def send(host, header, request, endpoint):
        response = requests.post(url=host + endpoint, headers=header, json=request)
        return response.json()

    # @staticmethod
    # def createVA(url, header, request):
    #     endpoint = "/api/v1.0/transfer-va/create-va"
    #     response = requests.service(url=url + endpoint, headers=header, json=request)
    #     return response.json(), endpoint
    # 
    # @staticmethod
    # def inquiryVA(url, header, request):
    #     endpoint = "/api/v1.0/transfer-va/status"
    #     response = requests.service(url=url + endpoint, headers=header, json=request)
    #     return response.json(), endpoint
    # 
    # @staticmethod
    # def getEndpoint(method):
    #     if method == 'getToken':
    #         def getToken(url, header, request):
    #             endpoint = "/v1.0/access-token/b2b"
    #             response = requests.service(url=url + endpoint, headers=header, json=request)
    #             return response.json(), endpoint
    #         return "/v1.0/access-token/b2b"
    #     elif method == 'createVA':
    #         return "/api/v1.0/transfer-va/create-va"
    #     else:
    #         return "/api/v1.0/transfer-va/status"
