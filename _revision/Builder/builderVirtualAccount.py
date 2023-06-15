class builderVirtualAccount:
    def __init__(self):
        self._partnerServiceId = None
        self._customerNo = None
        self._virtualAccountNo = None
        self._virtualAccountName = None
        self._trxId = None
        self._totalAmount = None
        self._additionalInfo = None

    def virtualAccount(self, partnerServiceId, customerNo, virtualAccountNo, virtualAccountName,
                       trxId, totalAmount, additionalInfo):
        self._partnerServiceId = partnerServiceId
        self._customerNo = customerNo
        self._virtualAccountNo = virtualAccountNo
        self._virtualAccountName = virtualAccountName
        self._trxId = trxId
        self._totalAmount = totalAmount
        self._additionalInfo = additionalInfo

    def toString(self):
        return "{" + \
            "partnerServiceId =" + self._partnerServiceId \
            + ", customerNo = " + self._customerNo \
            + ", virtualAccountNo = " + self._virtualAccountNo \
            + ", virtualAccountName = " + self._virtualAccountName \
            + ", trxId = " + self._trxId \
            + ", totalAmount = " + self._totalAmount \
            + ", additionalInfo = " + self._additionalInfo \
            + \
            "}"

builderVirtualAccount.virtualAccount("0","0001","XXX","GEB","TRX","A","B","XX")
print(builderVirtualAccount.toString())
