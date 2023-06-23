from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
# from Crypto.Signature.PKCS1_v1_5 import PKCS115_SigScheme
from Crypto.Hash import SHA256
from util.utilLogging import LoggerPrint
import base64
import hashlib
import hmac

class Signature :
    print = LoggerPrint()

    @staticmethod
    def signSHA256RSA(stringToSign, privateKey):
        try:
            # b1 = RSA.importKey(privateKey)
            # privateKeySigner = PKCS1_v1_5.PKCS115_SigScheme(b1)
            # Signature = privateKeySigner.sign(SHA256.new(stringToSign.encode()))
            b1 = base64.b64decode(privateKey)
            key = RSA.importKey(b1)
            signer = PKCS1_v1_5.new(key)
            digest = SHA256.new()
            digest.update(stringToSign.encode('utf-8'))
            signature = signer.sign(digest)
            hexSignature = base64.b64encode(signature).decode('utf-8')
            return hexSignature
        except Exception as e:
            print("Error Generate Signature:", e)
            return ''

    @staticmethod
    def getSignature(accessToken, requestBody, url, timestamp, staticKey):
        data = f"POST:{url}:{accessToken}:{requestBody}:{timestamp}"
        Signature.print.logInfo("String Data Sign: " + data)
        try:
            sign = Signature.hmacSHA512EncodeBase64(staticKey, data)
            Signature.print.logInfo("This Signature: " + sign)
            return sign
        except Exception as e:
            return ''

    @staticmethod
    def hmacSHA512EncodeBase64(key, data):
        hmacObj = hmac.new(key.encode('utf-8'), data.encode('utf-8'), hashlib.sha512)
        hmacBytes = hmacObj.digest()
        base64Encoded = base64.b64encode(hmacBytes).decode('utf-8')
        return base64Encoded

    @staticmethod
    def sha256EncodeHex(data):
        sha256Hash = hashlib.sha256(data.encode('utf-8')).digest()
        hexEncoded = sha256Hash.hex()
        return hexEncoded