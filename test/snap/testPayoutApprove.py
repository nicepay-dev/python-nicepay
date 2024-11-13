from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderPayout
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutApprove:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    bodyPayoutApprove = (
        builderPayout.BuildPayoutApprove()
        .setOriginalPartnerReferenceNo("OrdNo20241109192751")
        .setOriginalReferenceNo("IONPAYTEST07202411091927512277")
        .setMerchantId("IONPAYTEST")
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyPayoutApprove.jsonPayoutApprove(),
                                            ConstantsEndpoints.approvePayout())
