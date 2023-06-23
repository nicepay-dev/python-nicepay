class variableVirtualAccount:
    def __init__(self,
                 partnerServiceId,
                 customerNo,
                 virtualAccountNo,
                 virtualAccountName,
                 trxId,
                 totalAmount,
                 additionalInfo):
        self.partnerServiceId = partnerServiceId
        self.customerNo = customerNo
        self.virtualAccountNo = virtualAccountNo
        self.virtualAccountName = virtualAccountName
        self.trxId = trxId
        self.totalAmount = totalAmount
        self.additionalInfo = additionalInfo

    def toString(self):
        return ({
            "partnerServiceId": self.partnerServiceId,
            "customerNo": self.customerNo,
            "virtualAccountNo": self.virtualAccountNo,
            "virtualAccountName": self.virtualAccountName,
            "trxId": self.trxId,
            "totalAmount": self.totalAmount,
            "additionalInfo": self.additionalInfo
        })



class virtualAccountBuilder:
    def __init__(self):
        self.partnerServiceId = None
        self.customerNo = None
        self.virtualAccountNo = None
        self.virtualAccountName = None
        self.trxId = None
        self.totalAmount = None
        self.additionalInfo = None

    def setPartnerServiceId(self, partnerServiceId):
        self.partnerServiceId = partnerServiceId
        return self

    def setCustomerNo(self, customerNo):
        self.customerNo = customerNo
        return self

    def setVirtualAccountNo(self, virtualAccountNo):
        self.virtualAccountNo = virtualAccountNo
        return self

    def setVirtualAccountName(self, virtualAccountName):
        self.virtualAccountName = virtualAccountName
        return self

    def setTrxId(self, trxId):
        self.trxId = trxId
        return self

    def setTotalAmount(self, totalAmount):
        self.totalAmount = totalAmount
        return self

    def setAdditionalInfo(self, additionalInfo):
        self.additionalInfo = additionalInfo
        return self
