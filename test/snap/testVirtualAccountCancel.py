from data.builder.snap import builderAccessToken
from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderVirtualAccount
from service.snapService import SnapService
from util.utilLogging import Log

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
            "tXidVA": "IONPAYTEST02202411131349253102",
            "totalAmount": totalAmount,
            "cancelMessage": "Cancel Virtual Account"
                      }

    bodyCancelVA = (
        builderVirtualAccount.BuildCancelVA()
        .setPartnerServiceId("")
        .setCustomerNo("")
        .setVirtualAccountNo("884800041349253102")
        .setTrxId("123")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyCancelVA.jsonVACancel(),
                                            ConstantsEndpoints.cancelVA(),"DELETE")