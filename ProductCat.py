class ProductCat:
    def __init__(self, product_name):
        self.__product_name = product_name

    def set_product_name(self, product_name):
        if product_name == "" or product_name == " ":
            pass
        else:
            self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name
