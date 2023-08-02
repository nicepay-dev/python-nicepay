from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder import builderPayout
from data.builder import builderAccessToken
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
        .setOriginalPartnerReferenceNo("OrdNo20230624233147")
        .setOriginalReferenceNo("IONPAYTEST07202306242331506933")
        .setMerchantId("IONPAYTEST")
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyPayoutReject.jsonPayoutReject(),
                                            ConstantsEndpoints.rejectPayout())
