from post.ApiClient import ApiClient
from util.utilLogging import LoggerPrint


class serviceVirtualAccount:
    log = LoggerPrint()

    @staticmethod
    def callServiceVA(data, accessToken):
        gson = Gson()
        request = ApiClient.createService(PostRequest, TokenUtil.builder().build().getGrantType(), accessToken,
                                          gson.toJson(data))
        callSync = request.createVa(data)
        response = None
        nicePayResponse = None
        errorResponse = None
        resClient = None
        jsonObject = None

        try:
            response = callSync.execute()
            nicePayResponse = response.body()
            errorResponse = response.errorBody()

            if nicePayResponse is None:
                resClient = errorResponse.string()
            else:
                resClient = gson.toJson(nicePayResponse)

            mapper = ObjectMapper()
            jsonObject = JsonParser.parseString(resClient).getAsJsonObject()
            print.logInfoResponse("Response getVA: " + str(jsonObject))
        except Exception as ex:
            ex.printStackTrace()

        return nicePayResponse