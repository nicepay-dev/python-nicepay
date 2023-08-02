from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder import builderPayout
from data.builder import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutBalanceInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    additionalInfo = {

    }

    bodyPayoutApprove = (
        builderPayout.BuildPayoutBalanceInquiry()
        .setMerchantId("IONPAYTEST")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyPayoutApprove.jsonPayoutBalanceInquiry(),
                                            ConstantsEndpoints.balanceInquiryPayout())
