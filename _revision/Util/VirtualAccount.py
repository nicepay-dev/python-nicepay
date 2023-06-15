
class VirtualAccount :
    def __init__(self, partnerServiceId, customerNo, virtualAccountNo, virtualAccountName, trxId, totalAmount, additionalInfo) :
        self._partnerServiceId = partnerServiceId
        self._customerNo = customerNo
        self._virtualAccountNo = virtualAccountNo
        self._virtualAccountName = virtualAccountName
        self._trxId = trxId
        self._totalAmount = totalAmount
        self._additionalInfo = additionalInfo

        