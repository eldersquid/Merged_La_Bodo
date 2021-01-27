class Inventory:

    def __init__(self, item_name, supplier, product_name, quantity):
        self.__item_name = item_name
        self.__supplier = supplier
        self.__product_name = product_name
        self.__quantity = quantity

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def get_item_name(self):
        return self.__item_name

    def set_supplier(self, supplier):
        self.__supplier = supplier

    def get_supplier(self):
        return self.__supplier

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity
