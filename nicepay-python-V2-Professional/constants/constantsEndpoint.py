class ConstantsEndpoints:
    _REGISTRATION = "/nicepay/redirect/v2/registration"
    _PAYMENT = "/nicepay/redirect/v2/payment"
    _CANCEL = "/nicepay/direct/v2/cancel"
    _INQUIRY = "/nicepay/direct/v2/inquiry"

    @staticmethod
    def registration():
        return ConstantsEndpoints._REGISTRATION

    @staticmethod
    def payment():
        return ConstantsEndpoints._PAYMENT

    @staticmethod
    def cancel():
        return ConstantsEndpoints._CANCEL

    @staticmethod
    def inquiry():
        return ConstantsEndpoints._INQUIRY
