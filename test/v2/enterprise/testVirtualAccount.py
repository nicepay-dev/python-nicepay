from constants.constantsGeneral import ConstantsGeneral
from data.builder.v2.enterprise import builderCartData, builderVirtualAccount
from data.builder.v2.enterprise.dataGenerator import DataGenerator
from service.v2EnterpriseService import ServiceNicepay


class testVirtualAccount:
    amt = 10000
    itemCartData = {
        "goods_id": "BB12345678",
        "goods_detail": "BB12345678",
        "goods_name": "Market",
        "goods_amt": amt,
        "goods_type": "Nice",
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

    bodyVirtualAccount = (
        builderVirtualAccount.BuildVirtualAccount()
        .setPayMethod(ConstantsGeneral.getPayMethodVirtualAccount())
        .setBankCd("BMRI")
        .setVacctValidDt("")
        .setVacctValidTm("")
        .setMerFixAcctId("")
        .setAmt(amt)
        .build()
    )

    response = ServiceNicepay.serviceRequest(DataGenerator.getTransactionBody(bodyVirtualAccount.jsonVirtualAccount(),
                                                                              bodyCartData.jsonCartData()))