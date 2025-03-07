from data.builder.v2.enterprise import builderPayout
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testPayoutInquiry:
    bodyPayoutInquiry = (
        builderPayout.BuildPayoutInquiry()
        .setAccountNo("5345000060")
        .setTxid("IONPAYTEST07202411031722390627")
        .build()
    )

    response = ServiceNicepay.servicePayoutInquiry(DataGenerator.getPayoutInquiry(bodyPayoutInquiry.jsonPayoutInquiry()
                                                                                  ))
