from data.builder import builderVirtualAccount
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testVAFixedOpenDepositInq:
    bodyVAFixedOpenDepositInq = (
        builderVirtualAccount.BuildVAFixedOpenDepositInq()
        .setVacctNo("7007216100202208")
        .setStartDt("20230727")
        .setEndDt("20230727")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenDepositInq(DataGenerator
                                                           .getVAFixedOpenDepositInq(bodyVAFixedOpenDepositInq
                                                                                     .jsonVAFixedOpenDepositInq()))
