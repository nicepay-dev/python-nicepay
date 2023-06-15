import base64
import hashlib
import hmac
import logging

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256


class SignatureUtil:
    print("Testing")
    def __init__(self, xClientId, xTimestamp, privateKey):
        self.xClientId = xClientId
        self.xTimestamp = xTimestamp
        self.privateKey = privateKey

    def SignatureGenerator(self):
        print("Testing" + self.xClientId + self.xTimestamp + self.privateKey)
        # privateKey = self.privateKey
        # try :
        #     # ASSIGN STRING TO SIGN
        #     StringToSign = f"{self.xClientId}|{self.xTimestamp}"
        #     privateKeySigner = PKCS115_SigScheme(privateKey)
        #     logging.info(StringToSign)
        # except :
        #     print("X")
        # return
