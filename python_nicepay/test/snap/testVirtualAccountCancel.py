from python_nicepay.data.builder.snap import builderAccessToken, builderVirtualAccount
from python_nicepay.constants.constantsEndpoint import ConstantsEndpoints
from python_nicepay.service.snapService import SnapService
from python_nicepay.util.utilLogging import Log
from python_nicepay.data.builder import builderEnvirontment

log = Log()

class testVirtualAccountCancel:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    totalAmount = {"value": "10000.00",
                   "currency": "IDR"
                   }

    additionalInfo = {
            "tXidVA": "DPRSOLOTES02202501221717512009",
            "totalAmount": totalAmount,
            "cancelMessage": "Cancel Virtual Account"
                      }

    bodyCancelVA = (
        builderVirtualAccount.BuildCancelVA()
        .setPartnerServiceId("")
        .setCustomerNo("")
        .setVirtualAccountNo("9912304000063000")
        .setTrxId("123")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    environment = (builderEnvirontment.BuildEnvirontment()
                   .isCloud(True)
                   .isProduction(False)
                   .build())

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyCancelVA.jsonVACancel(),
                                            ConstantsEndpoints.cancelVA(),
                                            environment,
                                            "DELETE")