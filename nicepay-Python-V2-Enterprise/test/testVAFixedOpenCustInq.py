from data.builder import builderVirtualAccount
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testVAFixedOpenCustInq:
    bodyVAFixedOpenInq = (
        builderVirtualAccount.BuildVAFixedOpenCustInq()
        .setCustomerId("00202208")
        .build()
    )

    response = ServiceNicepay.serviceVAFixedOpenCustInq(DataGenerator.getVAFixedOpenCustInq(bodyVAFixedOpenInq
                                                                                            .jsonVAFixedOpenCustInq()))
