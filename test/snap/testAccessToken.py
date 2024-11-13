from data.builder.snap import builderAccessToken
from service.snapService import SnapService

class testAccessToken:
    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    Result = SnapService.serviceOAUTH(bodyCreateToken.jsonAccessToken())
