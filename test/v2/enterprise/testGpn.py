from constants.constantsGeneral import ConstantsGeneral
from data.builder.v2.enterprise import builderCartData, builderGpn
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testGpn:
    amt = 10000
    itemCartData = {
        "img_url": "https://cdn.eraspace.com/pub/media/catalog/product/i/p/iphone_13_pro_max_silver_1_5.jpg",
        "goods_name": "iPhone13ProMax",
        "goods_detail": "1TB-White",
        "goods_amt": amt,
        "goods_quantity": "1"
    }

    bodyCartData = (
        builderCartData.BuildCartData()
        .setCount("1")
        .setItem(itemCartData)
        .build()
    )

    bodyGpn = (
        builderGpn.BuildGpn()
        .setPayMethod(ConstantsGeneral.getPayMethodGpn())
        .setAmt(amt)
        .build()
    )

    response = ServiceNicepay.serviceRequest(DataGenerator.getTransactionBody(bodyGpn.jsonGpn(),
                                                                              bodyCartData.jsonCartData()))
