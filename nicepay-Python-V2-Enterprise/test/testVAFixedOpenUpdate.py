from data.builder import builderVirtualAccount
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testVAFixedOpenUpdate:
    bodyVAFixedOpenUpdate = (
        builderVirtualAccount.BuildVAFixedOpenCustomerUpdate()
        .setCustomerId("00202208")
        .setCustomerNm("Testing VA - n1tr0")
        .setUpdateType("2")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenUpdate(DataGenerator
                                                       .getVAFixedOpenUpdate(bodyVAFixedOpenUpdate
                                                                             .jsonVAFixedOpenCustomerUpdate()))
