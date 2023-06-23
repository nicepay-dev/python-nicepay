from builder.builderVirtualAccount import virtualAccountBuilder, variableVirtualAccount
from util.utilLogging import LoggerPrint
from postVirtualAccountReq import postVirtualAccountReq
from config.configConstants import Constants
from builder.builderAccessToken import AccessTokenBuilder, variableAccessToken
from datetime import datetime
from util.utilSignature import Signature
import json
import random

log = LoggerPrint()


class PostDeclare:

    @staticmethod
    def getHeaders(grantType, accessToken, data, url):
        headersMap = {}
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + "+07:00"
        clientKey = Constants.getClientKey()
        privateKey = Constants.getPrivateKey()
        secretKey = Constants.getClientSecret()
        randomNumber = random.randint(0, 9999999)
        externalId = "ordNo" + datetime.now().strftime("%Y%m%d%H%M%S")

        headersMap["Content-Type"] = "Application/JSON"
        if grantType is not None:
            stringToSign = f"{clientKey}|{timestamp}"
            signatureAccessToken = Signature.signSHA256RSA(stringToSign, privateKey)
            headersMap["X-TIMESTAMP"] = timestamp
            headersMap["X-CLIENT-KEY"] = clientKey
            headersMap["X-SIGNATURE"] = signatureAccessToken
        else:
            hashData = Signature.sha256EncodeHex(json.dumps(data))
            signature = Signature.getSignature(accessToken, hashData, url, timestamp, secretKey)
            headersMap["Authorization"] = f"Bearer {accessToken}"
            headersMap["X-TIMESTAMP"] = timestamp
            # headersMap["X-CLIENT-KEY"] = clientKey
            headersMap["X-SIGNATURE"] = signature
            headersMap["X-EXTERNAL-ID"] = externalId
            headersMap["X-PARTNER-ID"] = clientKey
            headersMap["CHANNEL-ID"] = clientKey + "01"

        # log.logInfo("Request Header : " + json.dumps(headersMap))
        return headersMap

    @staticmethod
    def serviceSNAP(grantType, accessToken, data):

        # CALL TOKEN
        log.logInfo("[GENERATE ACCESS TOKEN]")
        headers = PostDeclare.getHeaders(grantType, accessToken, data, "/v1.0/access-token/b2b")
        response = postVirtualAccountReq.getToken(Constants.getSandboxBaseUrl(),
                                                  headers,
                                                  createToken.toString()
                                                  )
        a = json.dumps(response[0])
        data = json.loads(a)
        accessToken = data["accessToken"]
        # jsonData = response[0]
        # data = json.loads(jsonData)
        # access_token = data["accessToken"]
        # getAccessToken = json.loads(response[0])
        # AccessToken = getAccessToken["accessToken"]
        log.logInfo("genAccessToken Endpoint : " + json.dumps(response[1]))
        log.logInfo("genAccessToken FullUrl : " + Constants.getSandboxBaseUrl() + response[1])
        log.logInfo("genAccessToken Headers : " + json.dumps(headers))
        log.logInfo("genAccessToken Body : " + json.dumps(createToken.toString()))
        log.logInfo("genAccessToken Response : " + a)

        # CALL CREATE VA
        log.logInfo("[CREATE VIRTUAL ACCOUNT]")
        headers2 = PostDeclare.getHeaders(None, accessToken, createVA.toString(),
                                         "/api/v1.0/transfer-va/create-va")
        response2 = postVirtualAccountReq.createVA(Constants.getSandboxBaseUrl(),
                                                   headers2,
                                                   createVA.toString())
        b = json.dumps(response2[0])
        log.logInfo("createVA Endpoint : " + json.dumps(response2[1]))
        log.logInfo("createVA FullUrl : " + Constants.getSandboxBaseUrl() + response2[1])
        log.logInfo("createVA Headers : " + json.dumps(headers2))
        log.logInfo("createVA Body : " + json.dumps(createVA.toString()))
        log.logInfo("createVA Response : " + b)

        # StringURL = Constants.getSandboxBaseUrl()
        # a = postVirtualAccountReq.getToken(
        #     Constants.getSandboxBaseUrl(),
        #     {"ContentType": "Application/JSON"},
        #     {})
        # endPoint = a[1]
        # log.logInfo("Request Host : " + Constants.getSandboxBaseUrl())
        # log.logInfo("")
        # log.logInfo("Response : " + json.dumps(a))
        # log.logInfo(endPoint)


class testAccessToken(AccessTokenBuilder):
    def build(self):
        return variableAccessToken(
            self.grantType,
            self.additionalInfo
        )


createToken = (
    testAccessToken()
    .setGrantType("client_credentials")
    .setAdditionalInfo("")
    .build()

)


class testVirtualAccount(virtualAccountBuilder):
    def build(self):
        return variableVirtualAccount(
            self.partnerServiceId,
            self.customerNo,
            self.virtualAccountNo,
            self.virtualAccountName,
            self.trxId,
            self.totalAmount,
            self.additionalInfo
        )


totalAmount = {"value": "10000.00",
               "currency": "IDR"
               }

additionalInfo = {"bankCd": "CENA",
                  "goodsNm": "Merchant Goods 1",
                  "dbProcessUrl": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
                  "vacctValidDt": "",
                  "vacctValidTm": "",
                  "msId": "",
                  "msFee": "",
                  "msFeeType": "",
                  "mbFee": "",
                  "mbFeeType": ""
                  }
createVA = (
    testVirtualAccount()
    .setPartnerServiceId("IONPAYTEST")
    .setCustomerNo("")
    .setVirtualAccountNo("")
    .setVirtualAccountName("Hantu Kesorean")
    .setTrxId("IONPAYTEST1348844834384834")
    .setTotalAmount(totalAmount)
    .setAdditionalInfo(additionalInfo)
    .build()
)

PostDeclare.serviceSNAP("client_credentials", "aaaaa", {})
# PostDeclare.getHeaders("blablabla", "", "", "")
