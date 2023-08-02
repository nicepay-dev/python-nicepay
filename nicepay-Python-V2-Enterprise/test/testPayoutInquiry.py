from data.builder import builderPayout
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayoutInquiry:
    bodyPayoutInquiry = (
        builderPayout.BuildPayoutInquiry()
        .setAccountNo("")
        .setTxid("")
        .build()
    )

    response = ServiceNicepay.servicePayoutInquiry(DataGenerator.getPayoutInquiry(bodyPayoutInquiry.jsonPayoutInquiry()
                                                                                  ))
