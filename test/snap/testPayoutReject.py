from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderPayout
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testPayoutReject:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    bodyPayoutReject = (
        builderPayout.BuildPayoutReject()
        .setOriginalPartnerReferenceNo("OrdNo20241109192849")
        .setOriginalReferenceNo("IONPAYTEST07202411091928492328")
        .setMerchantId("IONPAYTEST")
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyPayoutReject.jsonPayoutReject(),
                                            ConstantsEndpoints.rejectPayout())
