from data.builder import builderInquiry
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testInquiry:
    bodyInquiry = (
        builderInquiry.BuildInquiry()
        .setTxid("NORMALTEST02202307170909395340")
        .setReferenceNo("OrdNo20230717090938")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.serviceInquiry(DataGenerator.getInquiryBody(bodyInquiry.jsonInquiry()))
