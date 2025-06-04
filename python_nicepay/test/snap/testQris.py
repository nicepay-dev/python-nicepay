from datetime import datetime

from python_nicepay.constants.constantsEndpoint import ConstantsEndpoints
from python_nicepay.data.builder.snap import builderAccessToken, builderQris
from python_nicepay.service.snapService import SnapService
from python_nicepay.util.utilLogging import Log
from python_nicepay.data.builder import builderEnvirontment

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testQris:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    amount = {
        "value": "10000.00",
        "currency": "IDR"
    }

    additionalInfo = {
        "goodsNm": "Testing Nicepay",
        "billingNm": "testing",
        "billingPhone": "0813798872",
        "billingEmail": "testing@example.com",
        "billingAddr": "Jakarta",
        "billingCity": "South Jakarta",
        "billingState": "DKI Jakarta",
        "billingCountry": "Indonesia",
        "billingPostCd": "10200",
        "callBackUrl": "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
        "dbProcessUrl": "https://webhook.site/5cac2a81-5862-4734-95f4-e20887eef24b",
        "userIP": "127.0.0.1",
        "msfee": "",
        "msfeetype": "",
        "msId": "",
        "mbfee": "",
        "mbfeetype": "",
        "cartData": "{\"count\":1,\"item\":[{\"img_url\":\"https://d3nevzfk7ii3be.cloudfront.net/igi/vOrGHXlovukA566A.medium\",\"goods_name\":\"Nokia 3360\",\"goods_detail\":\"Old Nokia 3360\",\"goods_amt\":\"100\",\"goods_quantity\":\"1\"}]}",
        "mitraCd": "QSHP"
    }

    bodyQris = (
        builderQris.BuildQris()
        .setMerchantId("DPRSOLOTES")
        .setPartnerReferenceNo("OrdNo" + timestamp)
        .setStoreId("NICEPAY")
        .setValidityPeriod("")
        .setAmount(amount)
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    environment = (builderEnvirontment.BuildEnvirontment()
                   .isCloud(False)
                   .isProduction(False)
                   .build())

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyQris.jsonQris(),
                                            ConstantsEndpoints.qris(),
                                            environment)
