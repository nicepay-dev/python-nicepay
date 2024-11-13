from data.builder.v2.enterprise import builderPayout
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testPayoutReject:
    bodyPayoutReject = (
        builderPayout.BuildPayoutReject()
        .setTxid("IONPAYTEST07202410110001153231")
        .build()
    )

    response = ServiceNicepay.servicePayoutReject(DataGenerator.getPayoutReject(
        bodyPayoutReject.jsonPayoutReject()))
