from constants.constantsGeneral import ConstantsGeneral
from data.dataGenerator import DataGenerator
from data.builder import builderCreditCard, builderCartData
from service.serviceNicepay import ServiceNicepay


class testCreditCard:
    amt = 10000
    itemCartData = {
        "goods_id": "BB12345678",
        "goods_detail": "BB12345678",
        "goods_name": "Pasar Modern",
        "goods_amt": amt,
        "goods_type": "Sembako",
        "goods_url": "https://merchant.com/cellphones/iphone5s_64g",
        "goods_quantity": "1",
        "goods_sellers_id": "SEL123",
        "goods_sellers_name": "Sellers 1"
    }

    bodyCartData = (
        builderCartData.BuildCartData()
        .setCount("1")
        .setItem(itemCartData)
        .build()
    )

    bodyCreditCard = (
        builderCreditCard.BuildCreditCard()
        .setPayMethod(ConstantsGeneral.getPayMethodCreditCard())
        .setRecurrOpt("1")
        .setInstmntMon("1")
        .setInstmntType("1")
        .setAmt(amt)
        .build()
    )

    response = ServiceNicepay.serviceRequest(DataGenerator.getTransactionBody(bodyCreditCard.jsonCreditCard(),
                                                                              bodyCartData.jsonCartData()))



