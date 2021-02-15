class User:
    def __init__(self, name,username, email, gender, phone_num, password, deals):
        self.__name = name
        self.__username = username
        self.__email = email
        self.__phone_num = phone_num
        self.__gender = gender
        self.__password = password
        self.__deals = deals


    def set_name(self, name):
        self.__name = name

    def set_username(self,username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def set_gender(self, gender):
        self.__gender = gender

    def set_password(self, password):
        self.__password = password

    def set_deals(self, deals):
        self.__deals = deals

    def get_name(self):
        return self.__name

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_phone_num(self):
        return self.__phone_num

    def get_gender(self):
        return self.__gender

    def get_password(self):
        return self.__password

    def get_deals(self):
        return self.__deals
