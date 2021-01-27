class Guest:
    def __init__(self,name,industry,occupation,location,transport):
        self.__name= name
        self.__industry=industry
        self.__occupation=occupation
        self.__location=location
        self.__transport=transport
        self.__grade=""
        self.__priority=""
        self.__room_number=""
        self.__room_type=""
        self.__check_in=""
        self.__check_out = ""
        self.__request_type=""
        self.__request_topic=""
        self.__request_details=""

    def get_guest_id(self):
        return self.__guest_id

    def set_guest_id(self,guest_id):
        self.__guest_id=int(guest_id)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_industry(self):
        return self.__industry

    def set_industry(self, industry):
        self.__industry = industry

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self, occupation):
        self.__occupation = occupation

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_transport(self):
        return self.__transport

    def set_transport(self, transport):
        self.__transport = transport

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_priority(self):
        return self.__priority

    def set_priority(self, priority):
        self.__priority = priority

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_check_in(self):
        return self.__check_in

    def set_check_in(self, check_in):
        self.__check_in = check_in

    def get_check_out(self):
        return self.__check_out

    def set_check_out(self, check_out):
        self.__check_out = check_out

    def get_request_type(self):
        return self.__request_type

    def set_request_type(self,request_type):
        self.__request_type=request_type

    def get_request_topic(self):
        return self.__request_topic

    def set_request_topic(self,request_topic):
        self.__request_topic=request_topic

    def get_request_details(self):
        return self.__request_details

    def set_request_details(self,request_details):
        self.__request_details=request_details

    def get_request_id(self):
        return self.__request_id

    def set_request_id(self,request_id):
        self.__request_id=int(request_id)

    # def __str__(self):
    #     s=" Guest ID : {}\n Name : {} \n".format(self.__guest_id,self.__name)
    #     print(s)






