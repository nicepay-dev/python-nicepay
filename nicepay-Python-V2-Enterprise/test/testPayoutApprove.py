from data.builder import builderPayout
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayoutApprove:
    bodyPayoutApprove = (
        builderPayout.BuildPayoutApprove()
        .setTxid("IONPAYTEST07202307201024191946")
        .build()
    )

    response = ServiceNicepay.servicePayoutApprove(DataGenerator.getPayoutApproveBody(
        bodyPayoutApprove.jsonPayoutApprove()))
