class Request():
    def __init__(self,request_type,request_topic,request_details,guest_room_number,guest_name):
        self.__request_type = request_type
        self.__request_topic = request_topic
        self.__request_details= request_details
        self.__guest_room_number=guest_room_number
        self.__guest_name = guest_name
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

