from data.builder.v2.enterprise import builderVirtualAccount
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testVAFixedOpenDepositInq:
    bodyVAFixedOpenDepositInq = (
        builderVirtualAccount.BuildVAFixedOpenDepositInq()
        .setVacctNo("7007216100123458")
        .setStartDt("20241102")
        .setEndDt("20241103")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenDepositInq(DataGenerator
                                                           .getVAFixedOpenDepositInq(bodyVAFixedOpenDepositInq
                                                                                     .jsonVAFixedOpenDepositInq()))
