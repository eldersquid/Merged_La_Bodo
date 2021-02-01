class PackageDeal:

    def __init__(self, attractions, transport, price, code):

        self.__attractions = attractions
        self.__transport = transport
        self.__price = price
        self.__code = code





    def set_attractions(self, attractions):
        self.__attractions = attractions

    def get_attractions(self):
        return self.__attractions

    def set_transport(self, transport):
        self.__transport = transport

    def get_transport(self):
        return self.__transport

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_code(self, code):
        self.__code = code

    def get_code(self):
        return self.__code


