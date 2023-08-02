from data.builder import builderPayout
from data.dataGenerator import DataGenerator
from service.serviceNicepay import ServiceNicepay


class testPayout:
    bodyPayout = (
        builderPayout.BuildPayout()
        .setAccountNo("5345000060")
        .setBenefNm("John Doe")
        .setBenefPhone("012345678910")
        .setBenefStatus("1")
        .setBenefType("1")
        .setBankCd("BMRI")
        .setPayoutMethod("1")
        .setReferenceNo("NITRO0001X")
        .setReservedDt("")
        .setReservedTm("")
        .setAmt("10000")
        .setDescription("Testing Payout - n1tr0")
        .build()
    )

    response = ServiceNicepay.servicePayoutReg(DataGenerator.getPayoutRegBody(bodyPayout.jsonPayout()))
