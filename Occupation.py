from Industry import *
class Occupation(Industry):
    occupationList=["N/A","Doctor","Paramedic","Registered Nurse","Patient Care Assistant","Family and General Practitioner","Others"]
    occupationDict=[{"Occupation" : "N/A", "Industry" : "N/A" },
                    {"Occupation" : "Doctor", "Industry" : "Medical" },
                    {"Occupation": "Paramedic", "Industry" : "Medical"  },
                    {"Occupation": "Registered Nurse", "Industry" : "Medical"},
                    {"Occupation": "Patient Care Assistant", "Industry" : "Medical"},
                    {"Occupation": "Family and General Practitioner", "Industry" : "Medical"},
                    {"Occupation": "Others", "Industry" : "N/A"},
                    ]


    occupationChoices={
                        1 : {"N/A" : "N/A"},
                        2: {"Doctor": "Medical"},
                        3: {"Paramedic": "Medical"},
                        4: {"Registered Nurse": "Medical"},
                        5: {"Patient Care Assistant": "Medical"},
                        6: {"Family and General Practitioner": "Medical"},
                        7: {"Others": "N/A"}

    }


    def __init__(self,occupation,industry):
        super().__init__(industry)
        self.__occupation = occupation
        self.__description=""

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self,occupation):
        self.__occupation = occupation

    def get_occupation_id(self):
        return self.__occupation_id

    def set_occupation_id(self,occupation_id):
        self.__occupation_id= int(occupation_id)

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description