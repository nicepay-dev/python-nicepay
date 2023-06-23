class Response :
    def __init__(self,
                 responseCode,
                 responseMessage,
                 accessToken = None,
                 tokenType = None,
                 expiresIn = None) :
        self.responseCode = responseCode
        self.responseMessage = responseMessage
        self.accessToken = accessToken
        self.tokenType = tokenType
        self.expiresIn = expiresIn

    #GETTING ACCESS TOKEN RESPONSE
    @staticmethod
    def withAccessToken (responseCode,
                         responseMessage,
                         accessToken,
                         tokenType,
                         expiresIn) :
        return Response(responseCode,
                        responseMessage,
                        accessToken,
                        tokenType,
                        expiresIn)

    #GETTING VIRTUAL ACCOUNT RESPONSE
    @staticmethod
    def withVirtualAccount (responseCode,
                            responseMessage,
                            virtualAccountData,
                            totalAmount,
                            additionalInfo) :
        response = Response(responseCode, responseMessage)
        # response = Response()
        # response.responseCode = responseCode
        # response.responseMessage = responseMessage
        response.virtualAccountData = virtualAccountData
        response.totalAmount = totalAmount
        response.additionalInfo = additionalInfo

    #GETTING NO VIRTUAL ACCOUNT RESPONSE
    @staticmethod
    def withoutVirtualAccount (responseCode,
                               responseMessage) :
        return Response(responseCode,
                        responseMessage)