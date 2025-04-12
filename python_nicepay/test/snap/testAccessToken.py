from python_nicepay.data.builder.snap import builderAccessToken
from python_nicepay.service.snapService import SnapService
from python_nicepay.constants.constantsGeneral import ConstantsGeneral
from python_nicepay.data.builder import builderEnvirontment

class testAccessToken:
    # Case if merchant using different config with the constant
    clientKey = "NORMALTEST"
    cientSecret = "ZbUKZmH1HAXnU6RfJrrCzrFQlLs+yKleriW92UPprqqW48Ms3KMeIYSNYBXG5OhNxBhSeOzVBKXnfRdopp3W1w=="
    privateKey="MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7tOz+E6GzN3RJA34CXoEtkVc7ghhqRfkX8F4Ck/Ty/kcPD/sZO1y+p0IqbHEuImZgEmPAcZoug3ho45OPn36rsLIKeJ4SJ7az+h1ut3NxMXGbP8chzSyxzsk/oQ7aqMmiT+R15WYKrjDPS8xH5UQfCHeq/vyjawwyjf4SFIU59ykzvh9l2YpVSMM+2h2TvgcrU/tigIP1Px5vkuzuOQlomFj0IzlJjLTbrHb5c1aI8baUuP6j2EfdQ8scKPhuJ9v5EHLBZDJjWhIoQvnrCrnPxUOMTwGljRVShYjKniFtNlU+mrH40ndNMmGg0pYjk2AsEhEz/xY4cRsARi4xwUQTAgMBAAECggEAAOIypWWJQtM1gGx8SN2SBRlkjDqqC8IFkKfIgYGZyxUIV5lPKMi/QISACrwU8k8mJTig8JR4UdS7md7MYIYzLfK4e9UihVpbgVBhmBZT/Enry3vK361cEwAysVJ8Q+o8fL+chzOLvewg/bDRJtt87Rp4mbz2inxkA87oTcR79hBiMjcZZjbTx56j26h2gf871bvcEJ6VKGIYreVOaIeYBKczSatEcxBqBp4wY0VUuy2cyuyWilaszpM0e7bytnMwNH5At4+c5yW051DTpmNnWxbjN4iJu8bOFC3v+qGPbw1g/9ZbPT4bq9GCFMRaAeDHLUK/KjAZ0BnbGUn9NpbVMQKBgQD/iUtbw6PfKFu+jez4Fhaw0bD0Z4obbCdE9JnwG/ik2374vBDAUoj/5xvOu49GYIwuS1eld+dC2mSdFckgbPUX5ZOcF0CaxDM72AevTxiFSI4mc/4QaQUP5K41dULvvgs9qO20NrHzAR6KHJJrl+A7DW6ck+LFqepQ3ZsvF7hdsQKBgQC8DB9Fp9SVpObQKjqY3orZEvDIWJwkhLuv/u0eJnoGk45uBP4LJ0Hea3dXyEohKVsvDOb6ogMnp/8UXfpAO14z85MRvIlGf4cN5JQcYCeGr6yxst3KY4BCBNrtn5e3m2h0wpsWJ+gpE+pvJUq56hAKHkl7UXjW0gRXf/MwaT6bAwKBgQCzfOtKxGuJZt6yRRxK0bEUd+V0dnmic2BN5gVuiycmHOrdqbOWcyK5pMp6dnHXvB8asV8Z4dO1uJLtZ40DUqUBKQd6nzaIvwFBqqcTM1qE3AbE6bpuKmYc2MKo1/mxTeq1X7+/Up/BkWqzFgievGoK8I9eOd4SexwTuuSyulWMsQKBgGayPBXfXULIRuFiXpQD3VJFfMf9VHDBKHsqPrbbjoKu7Pb6tP7EVr2wdQG0uX84xbqBUleISS7MGYs286dGhODcYfIqw9GDbe9RaO3COXPd1vNI2sVf57imTCW/pay5K6ewa+ACtVBRtxMyC4hS4qWT+s9lJBg1o/dhQh+rKmyfAoGAfgXCnBhTQ1+lAR2v+bB2J2U1LLL0KK3+sUAMuy+KRSgB72Pke0MC5f9Gj6YPett32Y7yPmy2YFJMyhaSHRwOgK5/nd2NjuenIbvOs/GQie2509rjsFCTPw7YFlmvEtAm0DglHYZfOo0y50Z/i/xwRNR88IHusl6yYbQH6qLgn+8="

    ConstantsGeneral.setSnapConfiguration(clientKey, cientSecret, privateKey)

    bodyCreateToken = (
        builderAccessToken.BuildAccessToken()
        .setGrantType("client_credentials")
        .setAdditionalInfo("")
        .build()
    )

    environment = (builderEnvirontment.BuildEnvirontment()
                   .isCloud(False)
                   .isProduction(False)
                   .build())

    result = SnapService.serviceOAUTH(bodyCreateToken.jsonAccessToken(), environment)
