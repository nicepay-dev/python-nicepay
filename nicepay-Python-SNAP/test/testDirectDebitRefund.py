from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder import builderDirectDebit
from data.builder import builderAccessToken
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
        "value": "1000.00",
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
        .setOriginalPartnerReferenceNo("OrdNo20230624095145")
        .setOriginalReferenceNo("IONPAYTEST05202306240951476863")
        .setExternalStoreId("NICE")
        .setReason("Testing Refund QRIS SNAP")
        .setRefundAmount(refundAmount)
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyDirectDebitRefund.jsonDirectDebitRefund(),
                                            ConstantsEndpoints.refundDirectDebit())
