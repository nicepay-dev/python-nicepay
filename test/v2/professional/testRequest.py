from data.builder.v2.professional import builderCartData, builderSellers, builderRequest
from data.builder.v2.professional.dataGenerator import DataGenerator
from service.v2ProfessionalService import ServiceNicepay


class testRequest:
    amt = 10000
    itemCartData = {
        "goods_id": "GOODS001",
        "goods_name": "iPhone13ProMax",
        "goods_detail": "1TB-White",
        "goods_amt": amt,
        "goods_quantity": "1",
        "goods_type": "others",
        "goods_url": "https://cdn.eraspace.com/pub/media/catalog/product/i/p/iphone_13_pro_max_silver_1_5.jpg",
        "goods_sellers_id": "SEL123",
        "goods_sellers_name": "Sellers"
    }
    itemSellersAddress = {
        "sellerNm": "SEL123",
        "sellerLastNm": "One",
        "sellerAddr": "Jln.Jend.Sudirman",
        "sellerCity": "Central Jakarta",
        "sellerPostCd": "10202",
        "sellerCountry": "Indonesia",
        "sellerPhone": "08123456789"
    }

    bodyCartData = (
        builderCartData.BuildCartData()
        .setCount("1")
        .setItem(itemCartData)
        .build()
    )

    bodySellers = (
        builderSellers.BuildSellers()
        .setSellerId("SEL123")
        .setSellerNm("Sellers")
        .setSellerEmail("sellers@example.com")
        .setSellerUrl("https://www.sellers.com")
        .setSellerAddress(itemSellersAddress)
        .build()
    )

    bodyRequest = (
        builderRequest.BuildRequest()
        .setPayMethod("00")
        .setInstmntType("1")
        .setInstmntMon("1")
        .setRecurrOpt("1")
        .setBankCd("CENA")
        .setMitraCd("")
        .setVacctValidDt("")
        .setVacctValidTm("")
        .setMerFixAcctId("")
        .setPayValidDt("")
        .setPayValidTm("")
        .setPaymentExpDt("")
        .setPaymentExpTm("")
        .setAmt(amt)
        .build()
    )

    response = ServiceNicepay.serviceRedirect(DataGenerator.getTransactionBody(bodyRequest.jsonRequest(),
                                                                               bodyCartData.jsonCartData(),
                                                                               bodySellers.jsonSellers()))
