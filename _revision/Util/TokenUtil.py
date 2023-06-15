
class TokenUtil :
    def __init__(self, grantType, additionalInfo) :
        self._grantType = grantType
        self._additionalInfo = additionalInfo

    def get_grantType (self) :
        return self._grantType
    def set_grantType (self, grantType) :
        self._grantType = grantType

    def get_additionalInfo (self) :
        return self._additionalInfo
    def set_additionalInfo (self, additionalInfo) :
        self._additionalInfo = additionalInfo