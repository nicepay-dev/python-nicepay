from data.builder import builderInquiry
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testInquiry:
    bodyInquiry = (
        builderInquiry.BuildInquiry()
        .setTxid("NORMALTEST00202307311113389734")
        .setReferenceNo("OrdNo20230731111338")
        .setAmt("10000")
        .build()
    )

    response = ServiceNicepay.serviceInquiry(DataGenerator.getInquiryBody(bodyInquiry.jsonInquiry()))
