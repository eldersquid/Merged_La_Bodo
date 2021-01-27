class Supplier:
    productList = ['Select', 'Mask', 'Face Shield', 'Surgical Gloves', 'Infrared Thermometer',
                   'Pulse Oximeter', 'Air Filter', 'Bedpan Washer Disinfector']

    def __init__(self, company_name, uen_number, email, product_name, new_product_name):
        self.__company_name = company_name
        self.__uen_number = uen_number
        self.__email = email
        self.__product_name = product_name
        self.__new_product_name = new_product_name

    def set_company_name(self, company_name):
        self.__company_name = company_name

    def get_company_name(self):
        return self.__company_name

    def set_uen_number(self, uen_number):
        self.__uen_number = uen_number

    def get_uen_number(self):
        return self.__uen_number

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def get_product_name(self):
        return self.__product_name

    def set_new_product_name(self, new_product_name):
        if new_product_name == "" or new_product_name == " ":
            pass
        else:
            self.__new_product_name = new_product_name

    def get_new_product_name(self):
        return self.__new_product_name
