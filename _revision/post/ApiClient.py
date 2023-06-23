from config.configConstants import Constants
from util.utilLogging import LoggerPrint


class ApiClient:
    util = None
    log = LoggerPrint()
    builder = Retrofit.Builder().baseUrl(Constants.getSandboxBaseUrl()).addConverterFactory(GsonConverterFactory.create())
    retrofit = builder.build()
    httpClient = OkHttpClient.Builder()
    logging = HttpLoggingInterceptor().setLevel(HttpLoggingInterceptor.Level.BASIC)

    @staticmethod
    def createService(serviceClass, grandType, accessToken, data):
        ApiClient.httpClient.interceptors().clear()
        ApiClient.httpClient.addInterceptor(lambda chain: ApiClient.processInterceptor(chain, grandType, accessToken, data))
        ApiClient.builder.client(ApiClient.httpClient.build())
        ApiClient.retrofit = ApiClient.builder.build()
        return ApiClient.retrofit.create(serviceClass)

    @staticmethod
    def processInterceptor(chain, grandType, accessToken, data):
        original = chain.request()
        builder1 = None
        ApiClient.log.logInfo("generateVA " + "fullUrl :" + chain.request().url())
        url = chain.request().url().encodedPath().replace("/nicepay", "")
        Stream.of(grandType).ifPresentOrElse(
            lambda value: print.logInfo("getToken " + "pathUrl :" + url),
            lambda: print.logInfo("generateVA " + "pathUrl :" + url)
        )

        try:
            builder1 = original.newBuilder().headers(ApiClient.getHeaders(grandType, accessToken, data, url))
        except Exception as e:
            e.printStackTrace()

        response = chain.proceed(builder1.build())
        bodyString = response.body().string()
        contentType = response.body().contentType()
        responseBody = ResponseBody.create(bodyString, contentType)
        ApiClient.log.logInfoBody(
            "Request Data " + GsonBuilder().setPrettyPrinting().create().toJson(original.tag(Invocation).class_.arguments()[0])
        )
        return response.newBuilder().body(responseBody).build()

    @staticmethod
    def getHeaders(grandType, accessToken, data, pathUrl):
        headersMap = HashMap()

        f = SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssXXX")
        timeStamp = f.format(Date())
        clientKey = Constants.getClientKey()
        privateKey = Constants.getPrivatekey()
        secretKey = Constants.getSecretKey()
        rand = Random()
        random = rand.nextInt(100000000)
        externalID = "OrdNo" + timeStamp.substring(0, 10).replace("-", "") + timeStamp.substring(11, 19).replace(":", "") + random

        headersMap.put("Content-Type", "application/json")
        if grandType is not None:
            stringToSign = clientKey + "|" + timeStamp
            signatureAccessToken = SignatureUtils.signSHA256RSA(stringToSign, privateKey)
            headersMap.put("X-TIMESTAMP", timeStamp)
            headersMap.put("X-CLIENT-KEY", clientKey)
            headersMap.put("X-SIGNATURE", signatureAccessToken)
        else:
            hashData = SignatureUtils.sha256EncodeHex(data)
            signature = SignatureUtils.getSignature(accessToken, hashData, pathUrl, timeStamp, secretKey)
            headersMap.put("Authorization", "Bearer " + accessToken)
            headersMap.put("X-TIMESTAMP", timeStamp)
            headersMap.put("X-SIGNATURE", signature)
            headersMap.put("X-PARTNER-ID", clientKey)
            headersMap.put("X-EXTERNAL-ID", externalID)
            headersMap.put("CHANNEL-ID", clientKey + "01")

        ApiClient.log.logInfoHeader(
            "Request Header " + GsonBuilder().setPrettyPrinting().create().toJson(headersMap)
        )

        return Headers.of(headersMap)