from config.configConstants import Constants
from post.ApiClient import ApiClient
from post.postVirtualAccountReq import postVirtualAccountReq
from util.utilLogging import LoggerPrint


class serviceAccessToken:
    log = LoggerPrint()

    @staticmethod
    def callGetToken(util):
        print("")
        # request = ApiClient.createService(PostRequest, util.getGrantType(), None, None)
        # callSync = request.getToken(util)
        # response = None
        # nicePayResponse = None
        # errorResponse = None
        # resClient = None
        #
        # try:
        #     response = callSync.execute()
        #     nicePayResponse = response.body()
        #     errorResponse = response.errorBody()
        # except IOException as e:
        #     e.printStackTrace()
        #
        # if nicePayResponse is None:
        #     resClient = errorResponse.string()
        # else:
        #     resClient = nicePayResponse
        #
        # gson = GsonBuilder().setPrettyPrinting().create()
        # jsonResponse = gson.toJson(resClient)
        # serviceAccessToken.log.logInfoResponse("Response getToken: " + jsonResponse.replace("\\", ""))
        # return nicePayResponse
