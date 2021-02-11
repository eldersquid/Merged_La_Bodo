class Vehicle:
    vehicle_brand_list=["Audi","Mercedes","Toyota","Honda","Mitsubishi","BMW","Tesla"]


    def __init__(self, name, model, car_plate, contact, location):
        self.__location = location
        self.__model = model
        self.__name = name
        self.__car_plate = car_plate
        self.__contact = contact

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_model(self):
        return self.__model

    def set_model(self,model):
        self.__model = model

    def get_car_plate(self):
        return self.__car_plate

    def set_car_plate(self, car_plate):
        self.__car_plate = car_plate

    def get_contact(self):
        return self.__contact

    def set_contact(self, contact):
        self.__contact = contact

    def get_location(self):
        return self.__location

    def set_location(self,location):
        self.__location = location

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id = vehicle_id