class ConstantsGeneral:
    _SANDBOX_BASE_URL = "https://dev.nicepay.co.id"
    _STAGING_BASE_URL = "https://staging.nicepay.co.id"
    _PRODUCTION_BASE_URL = "https://www.nicepay.co.id"
    _I_MID = "IONPAYTEST"
    _MERCHANT_KEY = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
    _PAY_METHOD_CREDIT_CARD = "01"
    _PAY_METHOD_VIRTUAL_ACCOUNT = "02"
    _PAY_METHOD_CONVENIENCE_STORE = "03"
    _PAY_METHOD_DIRECT_DEBIT = "04"
    _PAY_METHOD_E_WALLET = "05"
    _PAY_METHOD_PAYLOAN = "06"
    _PAY_METHOD_PAYOUT = "07"
    _PAY_METHOD_QRIS = "08"
    _PAY_METHOD_GPN = "09"
    _CURRENCY = "IDR"
    _CALLBACK_URL = "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp"
    _DB_PROCESS_URL = "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3"
    _USER_IP = "127.0.0.1"
    _USER_SESSION_ID = ""
    _USER_AGENT = ""
    _USER_LANGUAGE = ""
    _SHOP_ID = "NICEPAY"

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
    def getImid():
        return ConstantsGeneral._I_MID

    @staticmethod
    def getMerchantKey():
        return ConstantsGeneral._MERCHANT_KEY

    @staticmethod
    def getPayMethodCreditCard():
        return ConstantsGeneral._PAY_METHOD_CREDIT_CARD

    @staticmethod
    def getPayMethodVirtualAccount():
        return ConstantsGeneral._PAY_METHOD_VIRTUAL_ACCOUNT

    @staticmethod
    def getPayMethodConvenienceStore():
        return ConstantsGeneral._PAY_METHOD_CONVENIENCE_STORE

    @staticmethod
    def getPayMethodDirectDebit():
        return ConstantsGeneral._PAY_METHOD_DIRECT_DEBIT

    @staticmethod
    def getPayMethodEWallet():
        return ConstantsGeneral._PAY_METHOD_E_WALLET

    @staticmethod
    def getPayMethodPayloan():
        return ConstantsGeneral._PAY_METHOD_PAYLOAN

    @staticmethod
    def getPayMethodPayout():
        return ConstantsGeneral._PAY_METHOD_PAYOUT

    @staticmethod
    def getPayMethodQris():
        return ConstantsGeneral._PAY_METHOD_QRIS

    @staticmethod
    def getPayMethodGpn():
        return ConstantsGeneral._PAY_METHOD_GPN

    @staticmethod
    def getCurrency():
        return ConstantsGeneral._CURRENCY

    @staticmethod
    def getCallbackUrl():
        return ConstantsGeneral._CALLBACK_URL

    @staticmethod
    def getDbProcessUrl():
        return ConstantsGeneral._DB_PROCESS_URL

    @staticmethod
    def getUserIp():
        return ConstantsGeneral._USER_IP

    @staticmethod
    def getShopId():
        return ConstantsGeneral._SHOP_ID