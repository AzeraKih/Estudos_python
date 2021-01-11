class Temperature():

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        self.__fahrenheit = (value * 1.8) + 32
        self.__celsius = float(value)
    
    def __init__(self, f):
        self.__fahrenheit = f
        self.__celsius = (f - 32) /1.8

    @property
    def fahrenheit(self):
        return self.__fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) /1.8
        self.__fahrenheit = float(value)
