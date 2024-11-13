from data.builder.snap import builderAccessToken
from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderVirtualAccount
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

    totalAmount = {
        "value": "10000.00",
        "currency": "IDR"
    }

    additionalInfo = {
        "tXidVA": "IONPAYTEST02202411130910178964",
        "totalAmount": totalAmount,
        "trxId": "123",
    }

    bodyInquiryVA = (
        builderVirtualAccount.BuildInquiryVA()
        .setPartnerServiceId("")
        .setCustomerNo("")
        .setVirtualAccountNo("884800040910178964")
        .setInquiryRequestId("")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyInquiryVA.jsonVAInquiry(),
                                            ConstantsEndpoints.inquiryVA())
