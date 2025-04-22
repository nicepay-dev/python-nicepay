from python_nicepay.data.builder.snap import builderAccessToken
from python_nicepay.service.snapService import SnapService
from python_nicepay.constants.constantsGeneral import ConstantsGeneral
from python_nicepay.data.builder import builderEnvirontment

class testAccessToken:
    # Case if merchant using different config with the constant
    clientKey = "IONPAYTEST"
    cientSecret = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
    privateKey="MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC2QB0PXu3lJszdsTgGIS7PIImQABpqWxnhl9Fde+CTmkDqqKea9LAWcTgpOtr2Gtw5r6ovOwZdl5J8KGsY+XE3QolUeNQTiSy2pjcYl/wL1aSm9n2XkIUqeEtY9Ft2PBFD9DGScTkN3mJyhvt4kkLaDjQiLDXBnBvl+wBJzzNOKpnEdhFxsBnpQo1955QWltBBUtedGB70IyPNZEIB7gVYXZ4/o2CxM7KGjC1Jlqb0uWGSzDSE44pVVSkCtokfw3LDtV0e7D8SlHvVmxXaef/ft6Nhv3xdOkaMiiRDFNC6bdOYiy1tljDrm2MZVV/nV5QCgUgAulTJcIdNQSBaPhZHAgMBAAECggEAWuCyfPEpsCv+WQefN5NBW6BOaCNdCK6/w5moGTUFwaRX/Ys29FJSIga36ftCpxiyuwMo2h9VJ8NGlKm06cGsnlEL2LbdjZZH2RYeACH9WUthrK3Z54N1m71bWRKULut58ogoVe0mdY9wSMqdR7yrID+X6HhiH9Z/pNjaBnQPEcjddaYtas77gaP5WqMwe/I8MlUPY5VEWpFVDx4LG8Uetlh4zdYEEPc70crFovDoKshrRnimABwIGoWAuX9PHYY5Lo29PzN3Tk25APcaaoSLBK2vCZALiQ3tAZizFo+qQLjC5UKzVzLtN/cJ86sktKHnK6TRsYcx/izPhdmj48hlkQKBgQDnJ7rLu4vWjHAPxsl4PNyV/JS56yb8fmFVvUmH+ackUOguQHkwY/hXwEP6OJ7+lo4oL7a+CBvo7RNHQvaq4yK3PzNMMU/YAdQLM/tW8VrFHMQZhc+u8bam3NWce92wWHW3y8zjJKmLnAhsXfHffyXXQt+Dbk9TGXwilE17MCllFwKBgQDJ1sMfAWiA6iI73FzF7w2IlMDsMW335ajNhdTrULmDUr0eQgjIZm4tV9GkPMnefjY03S0H1sLHoJObw1xMKvfYVeD79DqNZbcgk+YKwFEZK0hFAteJclFn2A0DlkvMC+KPqs+jE4QvQCnLLt0mxKp0m6jq1y7F//IXvGa0PKf2UQKBgQCEcig+ufw694byEzW3FjBSJEJXcNyKyiMdTHMIXUyeq1kNv1VxG6bdKMYKZkz7lOppLkWoBt9vDAAC0eSiL7jhhG3xF0QngYysyqEVxP78eCoIcbp5A/hjDZ+7pOF2PIlewYBpGcWnv8S3yvBe3eyhtah6F0eOVsjgy1bF4eemCwKBgQCAG/U678zhzjouXn7wDvw7DZeqEvGmn7lVwbVUKqelB9YLp4QlloYl95CTuxWyR8+mHCBh0llNFcm62vPxUHCBenjT0r97Ue07G0Su3ERdQlCbpOMjVVEAJWyVM0cm2wBRiexCqLeEuigM09EAs2ExpD9B15TTjdGeaTGTAtDlEQKBgQCurHorA6cAttCiiE8Z1CROjSOhv185gvL58tDS/pcMieik0zKyRV8gfnb5Kv8Z6njfE/6zlP5jp2gRAUgS+jCMpDDgd8cRwQoZqdIDxfsaes9SrBCl1XcDS4YO5NXLK3+BhEHlG+/eStPE4emKYpi7tIDS4TdnTIqka0k/l47+gQ=="

    ConstantsGeneral.setSnapConfiguration(clientKey, cientSecret, privateKey)

    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    environment = (builderEnvirontment.BuildEnvirontment()
                   .isCloud(True)
                   .isProduction(False)
                   .build())

    result = SnapService.serviceOAUTH(bodyCreateToken.jsonAccessToken(), environment)
