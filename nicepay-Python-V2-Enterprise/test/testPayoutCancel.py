from data.builder import builderPayout
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayoutCancel:
    bodyPayoutCancel = (
        builderPayout.BuildPayoutCancel()
        .setTxid("")
        .build()
    )

    response = ServiceNicepay.servicePayoutCancel(DataGenerator.getPayoutCancel(bodyPayoutCancel.jsonPayoutCancel()))
