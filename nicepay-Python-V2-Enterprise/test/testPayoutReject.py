from data.builder import builderPayout
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayoutReject:
    bodyPayoutReject = (
        builderPayout.BuildPayoutReject()
        .setTxid("IONPAYTEST07202307201024191946")
        .build()
    )

    response = ServiceNicepay.servicePayoutReject(DataGenerator.getPayoutReject(
        bodyPayoutReject.jsonPayoutReject()))
