from constants.constantsGeneral import ConstantsGeneral
from data.builder import builderCartData, builderDirectDebit
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testDirectDebit:
    amt = 10000
    itemCartData = {
        "img_url": "https://cdn.eraspace.com/pub/media/catalog/product/i/p/iphone_13_pro_max_silver_1_5.jpg",
        "goods_name": "iPhone13ProMax",
        "goods_detail": "1TB-White",
        "goods_amt": amt
    }

    bodyCartData = (
        builderCartData.BuildCartData()
        .setCount("1")
        .setItem(itemCartData)
        .build()
    )

    bodyDirectDebit = (
        builderDirectDebit.BuildDirectDebit()
        .setPayMethod(ConstantsGeneral.getPayMethodDirectDebit())
        .setMitraCd("JENC")
        .setMRefNo("")
        .setAmt(amt)
        .build()
    )

    response = ServiceNicepay.serviceRequest(DataGenerator.getTransactionBody(bodyDirectDebit.jsonDirectDebit(),
                                                                              bodyCartData.jsonCartData()))
