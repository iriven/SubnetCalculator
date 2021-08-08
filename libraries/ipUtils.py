
class ipValidator(object):

    def __init__(self,address: str):
        self.__address = address

    def isValidIPV4(self):
        parts = self.__address.split('.')
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        return True

    def isValidIPV6(self):
        parts = self.__address.split(':')
        if len(parts) != 7:
            return False
        for item in parts:
            if not(int(item, 16) >= 0 ) or item[0] == '-' or len(item) > 4:
                return False
        return True

    def isValidIP(self):
        try : 
            if self.isValidIPV4(self.__address):
                return True
            return self.isValidIPV6(self.__address)
        except:
            return False
