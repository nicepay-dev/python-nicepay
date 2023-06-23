from builder.builderAccessToken import variableAccessToken, AccessTokenBuilder
from post.postDeclare import PostDeclare
from post.postVirtualAccountReq import postVirtualAccountReq
from util.utilLogging import LoggerPrint
from config.configConstants import Constants

log = LoggerPrint()


class testAccessToken(AccessTokenBuilder):
    def build(self):
        return variableAccessToken(
            self.grantType,
            self.additionalInfo
        )


createToken = (
    testAccessToken()
    .setGrantType("client_credentials")
    .setAdditionalInfo("")
    .build()
)

Result = postVirtualAccountReq.getToken(Constants.getSandboxBaseUrl(),
                                        PostDeclare.getHeaders(None, None, None, ""),
                                        createToken.toString())

log.logInfo(Result)
