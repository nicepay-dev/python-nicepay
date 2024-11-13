from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder.snap import builderDirectDebit
from data.builder.snap import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testDirectDebitRefund:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    refundAmount = {
        "value": "1.00",
        "currency": "IDR"
    }

    additionalInfo = {
        "refundType": "1"
    }

    bodyDirectDebitRefund = (
        builderDirectDebit.BuildDirectDebitRefund()
        .setPartnerRefundNo("RefundNo" + timestamp)
        .setMerchantId("IONPAYTEST")
        .setSubMerchantId("")
        .setOriginalPartnerReferenceNo("OrdNo20241113140616")
        .setOriginalReferenceNo("IONPAYTEST05202411131406163958")
        .setExternalStoreId("NICE")
        .setReason("Testing Refund OVOE SNAP")
        .setRefundAmount(refundAmount)
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyDirectDebitRefund.jsonDirectDebitRefund(),
                                            ConstantsEndpoints.refundDirectDebit())
