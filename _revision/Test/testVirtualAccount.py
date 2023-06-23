from builder import builderAccessToken
from builder.builderAccessToken import variableAccessToken, AccessTokenBuilder
from builder.builderVirtualAccount import variableVirtualAccount, virtualAccountBuilder
# from service.serviceAccessToken import serviceAccessToken
# from service.serviceVirtualAccount import serviceVirtualAccount
# from post.postDeclare import PostDeclare
from util.utilLogging import LoggerPrint
import json

log = LoggerPrint()


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
    .setCustomerNo("CUST-00666")
    .setVirtualAccountNo("")
    .setVirtualAccountName("Hantu Kesorean")
    .setTrxId("IONPAYTEST1348844834384834")
    .setTotalAmount(totalAmount)
    .setAdditionalInfo(additionalInfo)
    .build()
)

log.logInfo("Body - " + json.dumps(createVA.toString()))

# class VirtualAccountTest:
#     print = LoggerPrint()
#
#     def getToken(self):
#         additionalInfo = {}
#         util = builderAccessToken.builder() \
#             .grantType("client_credentials") \
#             .additionalInfo(additionalInfo) \
#             .build()
#         return serviceAccessToken.callGetToken(util)
#
#     def vaCreate(self):
#         timeStamp = datetime.now().strftime("%Y%m%d%H%M%S")
#         randomValue = str(random.randint(1000, 9999))
#         trxId = timeStamp[11:19].replace(":", "") + randomValue
#
#         responseToken = self.getToken()
#         accessToken = responseToken.getAccessToken() if responseToken else None
#
#         if not accessToken:
#             raise ValueError("Token is null")
#
#         totalAmount = {"value": "200000.00", "currency": "IDR"}
#
#         additionalInfo = {
#             "bankCd": "BBBA",
#             "goodsNm": "TESTGoodsNm",
#             "dbProcessUrl": "https://merchant.com/test",
#             "vacctValidDt": "",
#             "vacctValidTm": "",
#             "msId": "",
#             "msFee": "",
#             "msFeeType": "",
#             "mbFee": "",
#             "mbFeeType": ""
#         }
#
#         virtualAccount = VirtualAccount.builder() \
#             .partnerServiceId("TESTPartner") \
#             .customerNo("") \
#             .virtualAccountNo("") \
#             .virtualAccountName("TESTVaName") \
#             .trxId(trxId) \
#             .totalAmount(totalAmount) \
#             .additionalInfo(additionalInfo) \
#             .build()
#
#         Result = serviceVirtualAccount.callServiceVA(virtualAccount, accessToken)
