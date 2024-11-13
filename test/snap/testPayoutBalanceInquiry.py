from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from constants.constantsGeneral import ConstantsGeneral
from data.builder.snap import builderPayout
from data.builder.snap import builderAccessToken
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
        "msId": ""
    }

    bodyPayoutApprove = (
        builderPayout.BuildPayoutBalanceInquiry()
        .setAccountNo("NORMALTEST")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyPayoutApprove.jsonPayoutBalanceInquiry(),
                                            ConstantsEndpoints.balanceInquiryPayout())
