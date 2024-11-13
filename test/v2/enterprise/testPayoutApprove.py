from data.builder.v2.enterprise import builderPayout
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testPayoutApprove:
    bodyPayoutApprove = (
        builderPayout.BuildPayoutApprove()
        .setTxid("IONPAYTEST07202411031722390627")
        .build()
    )

    response = ServiceNicepay.servicePayoutApprove(DataGenerator.getPayoutApproveBody(
        bodyPayoutApprove.jsonPayoutApprove()))
