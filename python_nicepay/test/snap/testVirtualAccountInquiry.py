from python_nicepay.constants.constantsGeneral import ConstantsGeneral
from python_nicepay.data.builder.snap import builderAccessToken, builderVirtualAccount
from python_nicepay.constants.constantsEndpoint import ConstantsEndpoints
from python_nicepay.service.snapService import SnapService
from python_nicepay.util.utilLogging import Log
from python_nicepay.data.builder import builderEnvirontment

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
        "tXidVA": "IONPAYTEST02202504161014301308",
        "totalAmount": totalAmount,
        "trxId": "123",
    }

    bodyInquiryVA = (
        builderVirtualAccount.BuildInquiryVA()
        .setPartnerServiceId("")
        .setCustomerNo("")
        .setVirtualAccountNo("70014000091014301308")
        .setInquiryRequestId("")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    environment = (builderEnvirontment.BuildEnvirontment()
                   .isCloud(True)
                   .isProduction(False)
                   .build())

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyInquiryVA.jsonVAInquiry(),
                                            ConstantsEndpoints.inquiryVA(),
                                            environment)
