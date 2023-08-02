import json

from config.apiClient import ApiClient
from constants.constantsEndpoint import ConstantsEndpoints
from constants.constantsGeneral import ConstantsGeneral
from data.dataGenerator import DataGenerator
from util.utilLogging import Log

log = Log()

host = ConstantsGeneral.getSandboxBaseUrl()


class ServiceNicepay:
    log.headers("Initialization")

    @staticmethod
    def serviceRequest(body):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.registration()
        response = ApiClient.send(host,
                                  headers,
                                  body,
                                  endpoint)

        a = json.dumps(response)
        data = json.loads(a)
        tXid = data["tXid"]

        log.info("Request Registration Transaction")
        log.info("Request Headers : " + json.dumps(headers))
        log.info("Request Data    : " + json.dumps(body))
        log.info("Response Data   : " + json.dumps(response))

        return tXid

    @staticmethod
    def serviceRedirect(body):
        tXid = ServiceNicepay.serviceRequest(body)
        endpoint = ConstantsEndpoints.payment()
        response = ApiClient.redirect(host,
                                      tXid,
                                      endpoint)
        log.info("Request To Redirect NICEPAY Secure Payment Page")
        log.info("Full URL   : " + response)
        log.info("Redirect To NICEPAY Secure Payment Page")

    @staticmethod
    def serviceCancel(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.cancel()
        response = ApiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Request Cancel Transaction")
        log.info("Request Headers : " + json.dumps(headers))
        log.info("Request Data    : " + json.dumps(data))
        log.info("Response Data   : " + json.dumps(response))

        return response

    @staticmethod
    def serviceInquiry(data):
        headers = DataGenerator.getTransactionHeader()
        endpoint = ConstantsEndpoints.inquiry()
        response = ApiClient.send(host,
                                  headers,
                                  data,
                                  endpoint)
        log.info("Request Inquiry Transaction")
        log.info("Request Headers : " + json.dumps(headers))
        log.info("Request Data    : " + json.dumps(data))
        log.info("Response Data   : " + json.dumps(response))

        return response
