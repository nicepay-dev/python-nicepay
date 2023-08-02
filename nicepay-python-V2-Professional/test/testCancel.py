from data.builder import builderCancel
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testCancel:
    bodyCancel = (
        builderCancel.BuildCancel()
        .setPayMethod("02")
        .setTxid("NORMALTEST00202307311113389734")
        .setCancelType("1")
        .setCancelMsg("Test Cancel Python V2 Pro - n1tr0")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.serviceCancel(DataGenerator.getCancelBody(bodyCancel.jsonCancel()))
