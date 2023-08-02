from data.builder import builderAccessToken
from constants.constantsEndpoint import ConstantsEndpoints
from data.builder import builderVirtualAccount
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()


class testVirtualAccountInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    totalAmount = {"value": "10000.00",
                   "currency": "IDR"
                   }

    additionalInfo = {"tXidVA": "IONPAYTEST02202306232221286791"
                      }

    bodyInquiryVA = (
        builderVirtualAccount.BuildInquiryVA()
        .setPartnerServiceId("")
        .setCustomerNo("")
        .setVirtualAccountNo("111111102221286791")
        .setInquiryRequestId("")
        .setTotalAmount(totalAmount)
        .setTrxId("IONPAYTEST1348844834384834")
        .setAdditionalInfo(additionalInfo)
        .build()
    )
    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyInquiryVA.jsonVAInquiry(),
                                            ConstantsEndpoints.inquiryVA())
