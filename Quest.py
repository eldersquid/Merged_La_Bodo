class Quest:
    def __init__(self,roomnum,name,grade,priority,type,topic,details):
        self.__roomnum=roomnum
        self.__name=name
        self.__grade=grade
        self.__priority=priority
        self.__type=type
        self.__topic=topic
        self.__details=details

    def get_quest_id(self):
        return self.__quest_id

    def set_quest_id(self,quest_id):
        self.__quest_id = int(quest_id)

    def get_room(self):
        return self.__room

    def set_roomnum(self, roomnum):
        self.__roomnum = roomnum

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_grade(self):
        return self.__grade

    def set_grade(self,grade):
        self.__grade = grade

    def get_priority(self):
        return self.__priority

    def set_priority(self,priority):
        self.__priority = priority

    def get_type(self):
        return self.__type

    def set_type(self,type):
        self.__type = type

    def get_topic(self):
        return self.__topic

    def set_topic(self,topic):
        self.__topic = topic

    def get_details(self):
        return self.__details

    def set_details(self,details):
        self.__details = details
