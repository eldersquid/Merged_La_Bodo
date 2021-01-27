class Reservation:
    count_id = 0

    def __init__(self, first_name, last_name, email, contact, date, time_slot, remarks):
        Reservation.count_id += 1
        self.__reservation_id = Reservation.count_id
        self.__remarks = remarks
        self.__time_slot = time_slot
        self.__date = date
        self.__contact = contact
        self.__email = email
        self.__last_name = last_name
        self.__first_name = first_name

    def get_reservation_id(self):
        return self.__reservation_id
    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_date(self):
        return self.__date
    def set_date(self, date):
        self.__date = date

    def get_contact(self):
        return self.__contact
    def set_contact(self, contact):
        self.__contact = contact

    def get_time_slot(self):
        return self.__time_slot
    def set_time_slot(self, time_slot):
        self.__time_slot = time_slot

    def get_remarks(self):
        return self.__remarks
    def set_remarks(self, remarks):
        self.__remarks = remarks

