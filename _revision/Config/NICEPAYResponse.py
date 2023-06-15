
class NICEPAYResponse:
    def __init__(self):
        self._responseCode = None
        self._responseCode = None
        self._responseMessage = None
        self._accessToken = None
        self._expiresIn = None
        self._tokenType = None
        self._virtualAccountData = None
        self._additionalInfo = None
        self._totalAmount = None

    def NICEPAYResponse(self, responseCode, responseMessage, accessToken, expiresIn, tokenType, virtualAccountData,
                        additionalInfo, totalAmount):
        self._responseCode = responseCode
        self._responseMessage = responseMessage
        self._accessToken = accessToken
        self._expiresIn = expiresIn
        self._tokenType = tokenType
        self._virtualAccountData = virtualAccountData
        self._additionalInfo = additionalInfo
        self._totalAmount = totalAmount

