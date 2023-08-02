from constants.constantsGeneral import ConstantsGeneral
from data.builder import builderCancel
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testCancel:
    bodyCancel = (
        builderCancel.BuildCancel()
        .setPayMethod(ConstantsGeneral.getPayMethodVirtualAccount())
        .setTxid("NORMALTEST02202307141014464233")
        .setCancelType("1")
        .setCancelMsg("Testing Cancellation - n1tr0")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.serviceCancel(DataGenerator.getCancelBody(bodyCancel.jsonCancel()))
