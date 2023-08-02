from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder import builderDirectDebit
from data.builder import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testDirectDebit:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    amount = {
        "value": "1000.00",
        "currency": "IDR"
    }

    urlParam = [
        {
            "url": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
            "type": "PAY_NOTIFY",
            "isDeeplink": "Y"
        },
        {
            "url": "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
            "type": "PAY_RETURN",
            "isDeeplink": "Y"
        }
    ]

    additionalInfo = {
        "mitraCd": "DANA",
        "goodsNm": "Merchant Goods 1",
        "billingNm": "John Doe",
        "billingPhone": "087788682224",
        "cartData": "{\"count\":\"2\",\"item\":[{\"img_url\":\"http://img.aaa.com/ima1.jpg\",\"goods_name\":\"Item 1 Name\",\"goods_detail\":\"Item 1 Detail\",\"goods_amt\":\"0.00\",\"goods_quantity\":\"1\"},{\"img_url\":\"http://img.aaa.com/ima2.jpg\",\"goods_name\":\"Item 2 Name\",\"goods_detail\":\"Item 2 Detail\",\"goods_amt\":\"1000.00\",\"goods_quantity\":\"1\"}]}",
        "dbProcessUrl": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
        "callBackUrl": "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
        "msId": "data"
    }

    bodyDirectDebit = (
        builderDirectDebit.BuildDirectDebit()
        .setPartnerReferenceNo("OrdNo" + timestamp)
        .setMerchantId("IONPAYTEST")
        .setSubMerchantId("")
        .setExternalStoreId("")
        .setValidUpTo("")
        .setValidUpTo("")
        .setPointOfInitiation("Mobile App")
        .setAmount(amount)
        .setUrlParam(urlParam)
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyDirectDebit.jsonDirectDebit(),
                                            ConstantsEndpoints.directDebit())
