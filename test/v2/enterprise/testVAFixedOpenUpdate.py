from data.builder.v2.enterprise import builderVirtualAccount
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testVAFixedOpenUpdate:
    bodyVAFixedOpenUpdate = (
        builderVirtualAccount.BuildVAFixedOpenCustomerUpdate()
        .setCustomerId("32270522")
        .setCustomerNm("HARFA2")
        .setUpdateType("3")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenUpdate(DataGenerator
                                                       .getVAFixedOpenUpdate(bodyVAFixedOpenUpdate
                                                                             .jsonVAFixedOpenCustomerUpdate()))
