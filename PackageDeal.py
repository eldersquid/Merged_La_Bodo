class PackageDeal:

    def __init__(self, attraction, transport, price, code):

        self.__attraction = attraction
        self.__transport = transport
        self.__price = price
        self.__code = code





    def set_attraction(self, attraction):
        self.__attraction = attraction

    def get_attraction(self):
        return self.__attraction

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


