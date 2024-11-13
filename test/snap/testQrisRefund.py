from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderQris
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
class testQrisRefund:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    refundAmount = {
        "value": "1000.00",
        "currency": "IDR"
    }

    additionalInfo = {
        "cancelType": "1"
    }

    bodyQrisInquiry = (
        builderQris.BuildQrisRefund()
        .setMerchantId("IONPAYTEST")
        .setExternalStoreId("NICEPAY")
        .setOriginalReferenceNo("IONPAYTEST08202411091931532481")
        .setOriginalPartnerReferenceNo("OrdNo20241109193152")
        .setPartnerRefundNo("51")
        .setRefundAmount(refundAmount)
        .setReason("Test Refund QRIS SNAP")
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyQrisInquiry.jsonQrisRefund(),
                                            ConstantsEndpoints.refundQris())
    