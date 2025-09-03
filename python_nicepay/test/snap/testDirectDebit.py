from datetime import datetime

from python_nicepay.constants.constantsEndpoint import ConstantsEndpoints
from python_nicepay.data.builder.snap import builderAccessToken, builderDirectDebit
from python_nicepay.service.snapService import SnapService
from python_nicepay.util.utilLogging import Log
from python_nicepay.data.builder import builderEnvirontment

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testDirectDebit:

    # TNICEEW051
    # clientKey = "JANGKAU001"
    # cientSecret = "ZbUKZmH1HAXnU6RfJrrCzrFQlLs+yKleriW92UPprqqW48Ms3KMeIYSNYBXG5OhNxBhSeOzVBKXnfRdopp3W1w=="
    # privateKey = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7tOz+E6GzN3RJA34CXoEtkVc7ghhqRfkX8F4Ck/Ty/kcPD/sZO1y+p0IqbHEuImZgEmPAcZoug3ho45OPn36rsLIKeJ4SJ7az+h1ut3NxMXGbP8chzSyxzsk/oQ7aqMmiT+R15WYKrjDPS8xH5UQfCHeq/vyjawwyjf4SFIU59ykzvh9l2YpVSMM+2h2TvgcrU/tigIP1Px5vkuzuOQlomFj0IzlJjLTbrHb5c1aI8baUuP6j2EfdQ8scKPhuJ9v5EHLBZDJjWhIoQvnrCrnPxUOMTwGljRVShYjKniFtNlU+mrH40ndNMmGg0pYjk2AsEhEz/xY4cRsARi4xwUQTAgMBAAECggEAAOIypWWJQtM1gGx8SN2SBRlkjDqqC8IFkKfIgYGZyxUIV5lPKMi/QISACrwU8k8mJTig8JR4UdS7md7MYIYzLfK4e9UihVpbgVBhmBZT/Enry3vK361cEwAysVJ8Q+o8fL+chzOLvewg/bDRJtt87Rp4mbz2inxkA87oTcR79hBiMjcZZjbTx56j26h2gf871bvcEJ6VKGIYreVOaIeYBKczSatEcxBqBp4wY0VUuy2cyuyWilaszpM0e7bytnMwNH5At4+c5yW051DTpmNnWxbjN4iJu8bOFC3v+qGPbw1g/9ZbPT4bq9GCFMRaAeDHLUK/KjAZ0BnbGUn9NpbVMQKBgQD/iUtbw6PfKFu+jez4Fhaw0bD0Z4obbCdE9JnwG/ik2374vBDAUoj/5xvOu49GYIwuS1eld+dC2mSdFckgbPUX5ZOcF0CaxDM72AevTxiFSI4mc/4QaQUP5K41dULvvgs9qO20NrHzAR6KHJJrl+A7DW6ck+LFqepQ3ZsvF7hdsQKBgQC8DB9Fp9SVpObQKjqY3orZEvDIWJwkhLuv/u0eJnoGk45uBP4LJ0Hea3dXyEohKVsvDOb6ogMnp/8UXfpAO14z85MRvIlGf4cN5JQcYCeGr6yxst3KY4BCBNrtn5e3m2h0wpsWJ+gpE+pvJUq56hAKHkl7UXjW0gRXf/MwaT6bAwKBgQCzfOtKxGuJZt6yRRxK0bEUd+V0dnmic2BN5gVuiycmHOrdqbOWcyK5pMp6dnHXvB8asV8Z4dO1uJLtZ40DUqUBKQd6nzaIvwFBqqcTM1qE3AbE6bpuKmYc2MKo1/mxTeq1X7+/Up/BkWqzFgievGoK8I9eOd4SexwTuuSyulWMsQKBgGayPBXfXULIRuFiXpQD3VJFfMf9VHDBKHsqPrbbjoKu7Pb6tP7EVr2wdQG0uX84xbqBUleISS7MGYs286dGhODcYfIqw9GDbe9RaO3COXPd1vNI2sVf57imTCW/pay5K6ewa+ACtVBRtxMyC4hS4qWT+s9lJBg1o/dhQh+rKmyfAoGAfgXCnBhTQ1+lAR2v+bB2J2U1LLL0KK3+sUAMuy+KRSgB72Pke0MC5f9Gj6YPett32Y7yPmy2YFJMyhaSHRwOgK5/nd2NjuenIbvOs/GQie2509rjsFCTPw7YFlmvEtAm0DglHYZfOo0y50Z/i/xwRNR88IHusl6yYbQH6qLgn+8="


    # ConstantsGeneral.setSnapConfiguration(clientKey, cientSecret, privateKey)

    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    amount = {
        "value": "1.00",
        "currency": "IDR"
    }

    urlParam = [
        {
            "url": "https://webhook.site/f203206c-66ea-4a59-b9d5-a44a289416cf",
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
        "billingNm": "Testin Dev",
        "billingPhone": "6281363681274",
        "cartData": "{\"count\":\"2\",\"item\":[{\"img_url\":\"http://img.aaa.com/ima1.jpg\",\"goods_name\":\"Item 1 Name\",\"goods_detail\":\"Item 1 Detail\",\"goods_amt\":\"0.00\",\"goods_quantity\":\"1\"},{\"img_url\":\"http://img.aaa.com/ima2.jpg\",\"goods_name\":\"Item 2 Name\",\"goods_detail\":\"Item 2 Detail\",\"goods_amt\":\"1.00\",\"goods_quantity\":\"1\"}]}",
        "dbProcessUrl": "https://webhook.site/3a016c88-f09e-49ea-b2c8-eee63e45368d",
        "callBackUrl": "https://dev.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
        "msId": ""
    }

    bodyDirectDebit = (
        builderDirectDebit.BuildDirectDebit()
        .setPartnerReferenceNo("OrdNo" + timestamp)
        .setMerchantId("TNICEEW051")
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

    environment = (builderEnvirontment.BuildEnvirontment()
                   .isCloud(False)
                   .isProduction(False)
                   .build())

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyDirectDebit.jsonDirectDebit(),
                                            ConstantsEndpoints.directDebit(),
                                            environment)
