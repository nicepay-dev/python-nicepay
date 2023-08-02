from constants.constantsEndpoint import ConstantsEndpoints
from util.utilLogging import Log

log = Log()


class General:
    infoClass = ""
    @staticmethod
    def endpointChecker(endpoint):
        if endpoint == ConstantsEndpoints.accessToken():

            infoClass = "genAccessToken"
            log.info("[GENERATE ACCESS TOKEN]")

        elif endpoint == ConstantsEndpoints.createVA():

            infoClass = "createVA"
            log.info("[CREATE VIRTUAL ACCOUNT]")

        elif endpoint == ConstantsEndpoints.inquiryVA():

            infoClass = "inquiryVA"
            log.info("[INQUIRY VIRTUAL ACCOUNT]")

        elif endpoint == ConstantsEndpoints.directDebit():

            infoClass = "directDebit"
            log.info("[DIRECT DEBIT]")

        elif endpoint == ConstantsEndpoints.inquiryDirectDebit():

            infoClass = "inquiryDirectDebit"
            log.info("[INQUIRY DIRECT DEBIT]")

        elif endpoint == ConstantsEndpoints.refundDirectDebit():

            infoClass = "refundDirectDebit"
            log.info("[REFUND DIRECT DEBIT]")

        elif endpoint == ConstantsEndpoints.qris():

            infoClass = "qris"
            log.info("[QRIS]")

        elif endpoint == ConstantsEndpoints.inquiryQris():

            infoClass = "inquiryQris"
            log.info("[INQUIRY QRIS]")

        elif endpoint == ConstantsEndpoints.refundQris():

            infoClass = "refundQris"
            log.info("[REFUND QRIS]")

        elif endpoint == ConstantsEndpoints.payout():

            infoClass = "payout"
            log.info("[PAYOUT]")

        elif endpoint == ConstantsEndpoints.approvePayout():

            infoClass = "approvePayout"
            log.info("[APPROVE PAYOUT]")

        elif endpoint == ConstantsEndpoints.balanceInquiryPayout():

            infoClass = "balanceInquiryPayout"
            log.info("[BALANCE INQUIRY PAYOUT]")

        elif endpoint == ConstantsEndpoints.cancelPayout():

            infoClass = "cancelPayout"
            log.info("[CANCEL PAYOUT]")

        elif endpoint == ConstantsEndpoints.rejectPayout():

            infoClass = "rejectPayout"
            log.info("[REJECT PAYOUT]")

        else:

            log.error("Error - Wrong Endpoint")

        return infoClass
