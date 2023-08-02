class ConstantsGeneral:
    _SANDBOX_BASE_URL = "https://dev.nicepay.co.id/nicepay"
    _STAGING_BASE_URL = "https://staging.nicepay.co.id/nicepay"
    _PRODUCTION_BASE_URL = "https://www.nicepay.co.id/nicepay"
    _PRIVATE_KEY = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAInJe1G22R2fMchIE6BjtYRqyMj6lurP" \
                   "/zq6vy79WaiGKt0Fxs4q3Ab4ifmOXd97ynS5f0JRfIqakXDcV/e2rx9bFdsS2HORY7o5At7D5E3tkyNM9smI" \
                   "/7dk8d3O0fyeZyrmPMySghzgkR3oMEDW1TCD5q63Hh/oq0LKZ/4Jjcb9AgMBAAECgYA4Boz2NPsjaE" \
                   "+9uFECrohoR2NNFVe4Msr8/mIuoSWLuMJFDMxBmHvO" \
                   "+dBggNr6vEMeIy7zsF6LnT32PiImv0mFRY5fRD5iLAAlIdh8ux9NXDIHgyera" \
                   "/PW4nyMaz2uC67MRm7uhCTKfDAJK7LXqrNVDlIBFdweH5uzmrPBn77foQJBAMPCnCzR9vIfqbk7gQa" \
                   "A0hVnXL3qBQPMmHaeIk0BMAfXTVq37PUfryo+80XXgEP1mN/e7f10GDUPFiVw6Wfwz38CQQC0L+xoxraftGnw" \
                   "FcVN1cK/MwqGS+DYNXnddo7Hu3+RShUjCz5E5NzVWH5yHu0E0Zt3sdYD2t7u7HSr9wn96OeDAkEApzB6eb0JD1kDd3P" \
                   "eilNTGXyhtIE9rzT5sbT0zpeJEelL44LaGa/pxkblNm0K2v/ShMC8uY6Bbi9oVqnMbj04uQJAJDIgTmfkla5bPZRR/zG6n" \
                   "kf1jEa/0w7i/R7szaiXlqsIFfMTPimvRtgxBmG6ASbOETxTHpEgCWTMhyLoCe54WwJATmPDSXk4APUQNvX5rr5OSfGWEOo67c" \
                   "KBvp5Wst+tpvc6AbIJeiRFlKF4fXYTb6HtiuulgwQNePuvlzlt2Q8hqQ=="
    _CLIENT_KEY = "IONPAYTEST"
    _CLIENT_SECRET = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="

    @staticmethod
    def getSandboxBaseUrl():
        return ConstantsGeneral._SANDBOX_BASE_URL

    @staticmethod
    def getStagingBaseUrl():
        return ConstantsGeneral._STAGING_BASE_URL

    @staticmethod
    def getProductionBaseUrl():
        return ConstantsGeneral._PRODUCTION_BASE_URL

    @staticmethod
    def getPrivateKey():
        return ConstantsGeneral._PRIVATE_KEY

    @staticmethod
    def getClientKey():
        return ConstantsGeneral._CLIENT_KEY

    @staticmethod
    def getClientSecret():
        return ConstantsGeneral._CLIENT_SECRET
