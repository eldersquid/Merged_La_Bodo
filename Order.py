class Order:
    count_id = 0

    def __init__(self, item_name, product_name, supplier,  quantity, remarks):
        Order.count_id += 1
        self.__order_id = Order.count_id
        self.__item_name = item_name
        self.__product_name = product_name
        self.__supplier = supplier
        self.__quantity = quantity
        self.__remarks = remarks

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_order_id(self):
        return self.__order_id

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def get_item_name(self):
        return self.__item_name

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def set_supplier(self, supplier):
        self.__supplier = supplier

    def get_supplier(self):
        return self.__supplier

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def get_remarks(self):
        return self.__remarks
