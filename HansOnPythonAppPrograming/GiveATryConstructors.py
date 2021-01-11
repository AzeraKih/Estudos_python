##class WaifuCdDescriptor:
##    def __get__(self, obj, owner):
##        return self.__CD_WAIFU
##
##    def __set__(self, obj, value):
##        if hasattr(obj, 'CD_WAIFU'):
##            raise ValueError("'CD_WAIFU' is read only attribute")
##        if not isinstance(value, int):
##            raise TypeError("'CD_WAIFU' must be an integer.")
##        self.__CD_WAIFU = value
##
##class WaifuNmDescriptor:
##    def __get__(self, obj, owner):
##        return self.__NM_WAIFU
##
##    def __set__(self, obj, value):
##        if not isinstance(value, str):
##            raise TypeError("'NM_WAIFU' must be an string.")
##        self.__NM_WAIFU = value
##
##
##class Waifu:
##    CD_WAIFU = WaifuCdDescriptor()
##    NM_WAIFU = WaifuNmDescriptor()       
##
##
##    def __init__(self, CD_WAIFU, NM_WAIFU):
##        self.CD_WAIFU = CD_WAIFU
##        self.NM_WAIFU = NM_WAIFU
##
##
##
##w = Waifu(1, "3")
##w.NM_WAIFU = 123
##print(w.CD_WAIFU)




##class WaifuNmDescriptor:
##    def __get__(self, obj, owner):
##        return self.__NM_WAIFU
##
##    def __set__(self, obj, value):
##        if not isinstance(value, str):
##            raise TypeError("'NM_WAIFU' must be an string.")
##        self.__NM_WAIFU = value
##
##
##class Waifu:
##
##    NM_WAIFU = WaifuNmDescriptor()       
##
##    @property
##    def CD_WAIFU(self):
##        return self.__CD_WAIFU
##    
##    @CD_WAIFU.setter
##    def CD_WAIFU(self, value):
##        if not isinstance(value, int):
##            raise TypeError("'CD_WAIFU' must be an integer.")
##        self.__CD_WAIFU = value
##        
##    def __init__(self, CD_WAIFU, NM_WAIFU):
##        #self.CD_WAIFU = CD_WAIFU
##        self.NM_WAIFU = NM_WAIFU
##
##
##
##w = Waifu(1, "3")
##w.CD_WAIFU = 9
##print(w.CD_WAIFU)
##
##
