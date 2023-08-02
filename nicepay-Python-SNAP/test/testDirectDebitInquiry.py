from datetime import datetime

from constants.constantsEndpoint import ConstantsEndpoints
from data.builder import builderDirectDebit
from data.builder import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")


class testDirectDebitInquiry:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    amount = {
        "value": "1000.00",
        "currency": "IDR"
    }

    additionalInfo = {}

    bodyDirectDebitInquiry = (
        builderDirectDebit.BuildDirectDebitInquiry()
        .setMerchantId("IONPAYTEST")
        .setSubMerchantId("")
        .setOriginalPartnerReferenceNo("OrdNo20230624095145")
        .setOriginalReferenceNo("IONPAYTEST05202306240951476863")
        .setServiceCode("54")
        .setTransactionDate(timestamp)
        .setAmount(amount)
        .setAdditionalInfo(additionalInfo)
        .build()
    )

    result = SnapService.serviceTransaction(bodyCreateToken.jsonAccessToken(),
                                            bodyDirectDebitInquiry.jsonDirectDebitInquiry(),
                                            ConstantsEndpoints.inquiryDirectDebit())
