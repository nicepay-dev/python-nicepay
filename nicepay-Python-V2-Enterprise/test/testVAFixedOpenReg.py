from data.builder import builderVirtualAccount
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testVAFixedOpenReg:
    bodyVAFixedOpen = (
        builderVirtualAccount.BuildVAFixedOpenReg()
        .setCustomerId("00202208")
        .setCustomerNm("SONNY")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenRegist(DataGenerator.getVAFixedOpenReg(bodyVAFixedOpen
                                                                                       .jsonVAFixedOpenReg()))
