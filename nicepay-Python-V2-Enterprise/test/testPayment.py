from datetime import datetime

from data.builder import builderPayment
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayment:
    bodyPayment = (
        builderPayment.BuildPayment()
        .setTimestamp(datetime.now().strftime("%Y%m%d%H%M%S"))
        .setTxid("IONPAYTEST05202307271435343814")
        .setReferenceNo("OrdNo20230727143533")
        .setCashtag("")
        .setCardNo("5123450000000008")
        .setCardExpYymm("3901")
        .setCardCvv("100")
        .setRecurringToken("")
        .setPreAuthToken("11a5a8978dd3ef0cc5bf447864c49a80f9fd89103a368526505c56ee0ff486c5")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.servicePayment(DataGenerator.getPaymentBody(bodyPayment.dataPayment()))
