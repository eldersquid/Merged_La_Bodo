class Occupation:
    occupationList=["N/A","Doctor","Paramedic","Registered Nurse","Patient Care Assistant","Family and General Practitioner","Others"]
    occupationDict=[{"Occupation" : "N/A", "Industry" : "N/A" },
                    {"Occupation" : "Doctor", "Industry" : "Medical" },
                    {"Occupation": "Paramedic", "Industry" : "Medical"  },
                    {"Occupation": "Registered Nurse", "Industry" : "Medical"},
                    {"Occupation": "Patient Care Assistant", "Industry" : "Medical"},
                    {"Occupation": "Family and General Practitioner", "Industry" : "Medical"},
                    {"Occupation": "Others", "Industry" : "N/A"},
                    ]


    def __init__(self,occupation,industry):
        self.__occupation = occupation
        self.__industry = industry

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self,occupation):
        self.__occupation = occupation

    def get_occupation_id(self):
        return self.__occupation_id

    def set_occupation_id(self,occupation_id):
        self.__occupation_id= int(occupation_id)

    def get_industry(self):
        return self.__industry

    def set_industry(self,industry):
        self.__industry = industry