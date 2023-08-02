class ConstantsEndpoints:
    _ACCESS_TOKEN = "/v1.0/access-token/b2b"
    _CREATE_VA = "/api/v1.0/transfer-va/create-va"
    _INQUIRY_VA = "/api/v1.0/transfer-va/status"
    _DIRECT_DEBIT = "/api/v1.0/debit/payment-host-to-host"
    _INQUIRY_DIRECT_DEBIT = "/api/v1.0/debit/status"
    _REFUND_DIRECT_DEBIT = "/api/v1.0/debit/refund"
    _QRIS = "/api/v1.0/qr/qr-mpm-generate"
    _INQUIRY_QRIS = "/api/v1.0/qr/qr-mpm-query"
    _REFUND_QRIS = "/api/v1.0/qr/qr-mpm-refund"
    _PAYOUT = "/api/v1.0/transfer/registration"
    _APPROVE_PAYOUT = "/api/v1.0/transfer/approve"
    _INQUIRY_PAYOUT = "/api/v1.0/transfer/inquiry"
    _CANCEL_PAYOUT = "/api/v1.0/transfer/cancel"
    _REJECT_PAYOUT = "/api/v1.0/transfer/reject"
    _BALANCE_INQUIRY_PAYOUT = "/api/v1.0/transfer/balance-inquiry"

    @staticmethod
    def accessToken():
        return ConstantsEndpoints._ACCESS_TOKEN

    @staticmethod
    def createVA():
        return ConstantsEndpoints._CREATE_VA

    @staticmethod
    def inquiryVA():
        return ConstantsEndpoints._INQUIRY_VA

    @staticmethod
    def directDebit():
        return ConstantsEndpoints._DIRECT_DEBIT

    @staticmethod
    def inquiryDirectDebit():
        return ConstantsEndpoints._INQUIRY_DIRECT_DEBIT

    @staticmethod
    def refundDirectDebit():
        return ConstantsEndpoints._REFUND_DIRECT_DEBIT

    @staticmethod
    def qris():
        return ConstantsEndpoints._QRIS

    @staticmethod
    def inquiryQris():
        return ConstantsEndpoints._INQUIRY_QRIS

    @staticmethod
    def refundQris():
        return ConstantsEndpoints._REFUND_QRIS

    @staticmethod
    def payout():
        return ConstantsEndpoints._PAYOUT

    @staticmethod
    def approvePayout():
        return ConstantsEndpoints._APPROVE_PAYOUT

    @staticmethod
    def cancelPayout():
        return ConstantsEndpoints._CANCEL_PAYOUT

    @staticmethod
    def rejectPayout():
        return ConstantsEndpoints._REJECT_PAYOUT

    @staticmethod
    def balanceInquiryPayout():
        return ConstantsEndpoints._BALANCE_INQUIRY_PAYOUT