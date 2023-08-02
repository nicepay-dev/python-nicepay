class ConstantsEndpoints:
    _REGISTRATION = "/nicepay/direct/v2/registration"
    _PAYMENT = "/nicepay/direct/v2/payment"
    _INQUIRY = "/nicepay/direct/v2/inquiry"
    _CANCEL = "/nicepay/direct/v2/cancel"
    _VA_FIXED_OPEN_REGISTRATION = "/nicepay/api/vacctCustomerRegist.do"
    _VA_FIXED_OPEN_CUSTOMER_INQUIRY = "/nicepay/api/vacctCustomerInquiry.do"
    _VA_FIXED_OPEN_DEPOSIT_INQUIRY = "/nicepay/api/vacctInquiry.do"
    _VA_FIXED_OPEN_CUSTOMER_UPDATE = "/nicepay/api/vacctCustomerUpdate.do"
    _PAYOUT_REGISTRATION = "/nicepay/api/direct/v2/requestPayout"
    _PAYOUT_APPROVE = "/nicepay/api/direct/v2/approvePayout"
    _PAYOUT_INQUIRY = "/nicepay/api/direct/v2/inquiryPayout"
    _PAYOUT_REJECT = "/nicepay/api/direct/v2/rejectPayout"
    _PAYOUT_CANCEL = "/nicepay/api/direct/v2/cancelPayout"
    _PAYOUT_BALANCE_INQUIRY = "/nicepay/api/direct/v2/balanceInquiry"
    _PAYOUT_TRANSACTION_HISTORY_INQUIRY = "/nicepay/direct/v2/historyInquiry"
    _PAYOUT_RECURRING_REQUEST = "/nicepay/api/direct/v2/recurringRequest"
    _PAYOUT_SELLER_BALANCE_TRANSFER = "/nicepay/api/direct/v2/sellerBalanceTransfer"
    _PAYOUT_MERCHANT_BALANCE_TRANSFER = "/nicepay/api/direct/v2/merchantBalanceTransfer"
    _PAYOUT_LIST_INQUIRY = "/nicepay/direct/v2/listInquiry"

    @staticmethod
    def registration():
        return ConstantsEndpoints._REGISTRATION

    @staticmethod
    def payment():
        return ConstantsEndpoints._PAYMENT

    @staticmethod
    def inquiry():
        return ConstantsEndpoints._INQUIRY

    @staticmethod
    def cancel():
        return ConstantsEndpoints._CANCEL

    @staticmethod
    def vaFixedOpenRegist():
        return ConstantsEndpoints._VA_FIXED_OPEN_REGISTRATION

    @staticmethod
    def vaFixedOpenCustInq():
        return ConstantsEndpoints._VA_FIXED_OPEN_CUSTOMER_INQUIRY

    @staticmethod
    def vaFixedOpenDepositInq():
        return ConstantsEndpoints._VA_FIXED_OPEN_DEPOSIT_INQUIRY

    @staticmethod
    def vaFixedOpenCustUpdate():
        return ConstantsEndpoints._VA_FIXED_OPEN_CUSTOMER_UPDATE

    @staticmethod
    def payoutRegistration():
        return ConstantsEndpoints._PAYOUT_REGISTRATION

    @staticmethod
    def payoutApprove():
        return ConstantsEndpoints._PAYOUT_APPROVE

    @staticmethod
    def payoutInquiry():
        return ConstantsEndpoints._PAYOUT_INQUIRY

    @staticmethod
    def payoutReject():
        return ConstantsEndpoints._PAYOUT_REJECT

    @staticmethod
    def payoutCancel():
        return ConstantsEndpoints._PAYOUT_CANCEL

    @staticmethod
    def payoutBalanceInq():
        return ConstantsEndpoints._PAYOUT_BALANCE_INQUIRY

    @staticmethod
    def payoutTransHistInq():
        return ConstantsEndpoints._PAYOUT_TRANSACTION_HISTORY_INQUIRY

    @staticmethod
    def payoutRecurringReq():
        return ConstantsEndpoints._PAYOUT_RECURRING_REQUEST

    @staticmethod
    def payoutSellerBalanceTransfer():
        return ConstantsEndpoints._PAYOUT_SELLER_BALANCE_TRANSFER

    @staticmethod
    def payoutMerchantBalanceTransfer():
        return ConstantsEndpoints._PAYOUT_MERCHANT_BALANCE_TRANSFER

    @staticmethod
    def payoutListInquiry():
        return ConstantsEndpoints._PAYOUT_LIST_INQUIRY
