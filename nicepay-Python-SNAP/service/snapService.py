import json
from constants.constantsGeneral import ConstantsGeneral
from constants.constantsEndpoint import ConstantsEndpoints
from data.dataGenerator import dataGenerator
from config.apiClient import apiClient
from util.utilGeneral import General
from util.utilLogging import Log

log = Log()
host = ConstantsGeneral.getSandboxBaseUrl()  # ENVIRONMENT


class SnapService:
    log.headers("Initialization")
    @staticmethod
    def serviceOAUTH(body):

        headers = dataGenerator.getOAUTHHeader()
        endpoint = ConstantsEndpoints.accessToken()
        response = apiClient.send(host,
                                  headers,
                                  body,
                                  endpoint)
        infoClass = General.endpointChecker(endpoint)

        a = json.dumps(response)
        data = json.loads(a)
        accessToken = data["accessToken"]

        log.info(f"{infoClass} - Endpoint : " + endpoint)
        log.info(f"{infoClass} - FullUrl : " + host + endpoint)
        log.info(f"{infoClass} - Headers : " + json.dumps(headers))
        log.info(f"{infoClass} - Body : " + json.dumps(body))
        log.info(f"{infoClass} - Response : " + json.dumps(response))
        log.info(f"{infoClass} - AccessToken : " + accessToken)

        return accessToken

    @staticmethod
    def serviceTransaction(bodyAccessToken, body, endpoint):

        receiveAccessToken = SnapService.serviceOAUTH(bodyAccessToken)
        log.headers("Services Init")
        headerTransaction = dataGenerator.getTransactionHeader(receiveAccessToken,
                                                               body,
                                                               endpoint)

        infoClass = General.endpointChecker(endpoint)
        receiveResponse = apiClient.send(host,
                                         headerTransaction,
                                         body,
                                         endpoint)
        log.info(f"{infoClass} - Endpoint : " + endpoint)
        log.info(f"{infoClass} - FullUrl : " + host + endpoint)
        log.info(f"{infoClass} - Headers : " + json.dumps(headerTransaction))
        log.info(f"{infoClass} - Body : " + json.dumps(body))
        log.info(f"{infoClass} - Response : " + json.dumps(receiveResponse))

        return
