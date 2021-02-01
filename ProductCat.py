class ProductCat:
    productList = ['Select', 'Mask', 'Face Shield', 'Surgical Gloves', 'Infrared Thermometer',
                   'Pulse Oximeter', 'Air Filter', 'Bedpan Washer Disinfector']
    productDict = [{"Product Category": "Select"}, {"Product Category": "Mask"}, {"Product Category": "Face Shield"},
                   {"Product Category": "Surgical Gloves"},
                   {"Product Category": "Infrared Thermometer"}, {"Product Category": "Pulse Oximeter"},
                   {"Product Category": "Air Filter"}, {"Product Category": "Bedpan Washer Disinfector"}]
    productSelect = {
        1: {"Select": "Select"},
        2: {"Mask": "Mask"},
        3: {"Face Shield": "Face Shield"},
        4: {"Surgical Gloves": "Surgical Gloves"},
        5: {"Infrared Thermometer": "Infrared Thermometer"},
        6: {"Pulse Oximeter": "Pulse Oximeter"},
        7: {"Air Filter": "Air Filter"},
        8: {"Bedpan Washer Disinfector": "Bedpan Washer Disinfector"}
    }

    def __init__(self, productcat):
        self.__productcat = productcat

    def set_productcat(self, productcat):
        if productcat == "" or productcat == " ":
            pass
        else:
            self.__productcat = productcat

    def get_productcat(self):
        return self.__productcat

    def set_productcat_id(self, productcat_id):
        self.__productcat_id = productcat_id

    def get_productcat_id(self):
        return self.__productcat_id
