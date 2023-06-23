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
            hashData = Signature.sha256EncodeHex(data)
            signature = Signature.getSignature(accessToken, hashData, url, timestamp, secretKey)
            headersMap["Authorization"] = f"Bearer {accessToken}"
            headersMap["X-TIMESTAMP"] = timestamp
            headersMap["X-CLIENT-KEY"] = clientKey
            headersMap["X-SIGNATURE"] = signature
            headersMap["X-EXTERNAL-ID"] = externalId
            headersMap["CHANNEL-ID"] = clientKey + "01"

        # log.logInfo("Request Header : " + json.dumps(headersMap))
        return headersMap

    @staticmethod
    def serviceSNAP(grantType, accessToken, data):

        # CALL TOKEN
        log.logInfo("[GENERATE ACCESS TOKEN]")

        response = postVirtualAccountReq.getToken(Constants.getSandboxBaseUrl(),
                                                  PostDeclare.getHeaders(grantType,
                                                                         accessToken,
                                                                         data,
                                                                         "/v1.0/access-token/b2b"),
                                                  {
                                                      "grantType": "client_credentials",
                                                      "additionalInfo": ""
                                                  })
        a = json.dumps(response[0])
        # getAccessToken = json.loads(response[0])
        # AccessToken = getAccessToken["accessToken"]
        log.logInfo("genAccessToken Endpoint : " + json.dumps(response[1]))
        log.logInfo("genAccessToken FullUrl : " + Constants.getSandboxBaseUrl() + response[1])
        log.logInfo("genAccessToken Headers : " + json.dumps(createToken.toString()))
        log.logInfo("genAccessToken Response : " + a)
        # log.logInfo("AccessToken : " + accessToken )

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

PostDeclare.serviceSNAP("client_credentials", "aaaaa", {})
# PostDeclare.getHeaders("blablabla", "", "", "")
