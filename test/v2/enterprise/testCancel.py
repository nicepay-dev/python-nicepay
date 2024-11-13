from constants.constantsGeneral import ConstantsGeneral
from data.builder.v2.enterprise import builderCancel
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testCancel:
    bodyCancel = (
        builderCancel.BuildCancel()
        .setPayMethod(ConstantsGeneral.getPayMethodVirtualAccount())
        .setTxid("NORMALTEST02202411031620357492")
        .setCancelType("1")
        .setCancelMsg("Testing Cancellation - n1tr0")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.serviceCancel(DataGenerator.getCancelBody(bodyCancel.jsonCancel()))
