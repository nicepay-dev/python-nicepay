from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderPayout
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    bodyPayoutInquiry = (
        builderPayout.BuildPayoutInquiry()
        .setMerchantId("IONPAYTEST")
        .setOriginalPartnerReferenceNo("OrdNo20241016163626")
        .setOriginalReferenceNo("IONPAYTEST07202410161636267454")
        .setBeneficiaryAccountNo("12355874912")
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyPayoutInquiry.jsonPayoutInquiry(),
                                            ConstantsEndpoints.inquiryPayout())
