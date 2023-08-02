from data.builder import builderAccessToken
from service.snapService import SnapService
from util.utilLogging import Log

log = Log()


class testAccessToken:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    Result = SnapService.serviceOAUTH(bodyCreateToken.jsonAccessToken())
