class Room:
    def __init__(self,floor,type,grade,guest,occupation):
        self.__floor = floor
        self.__type= type
        self.__grade = grade
        self.__guest = guest
        self.__occupation = occupation

    def get_floor(self):
        return self.__floor

    def set_floor(self,floor):
        self.__floor = floor

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_guest(self):
        return self.__guest

    def set_guest(self, guest):
        self.__guest = guest

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self, occupation):
        self.__occupation = occupation

