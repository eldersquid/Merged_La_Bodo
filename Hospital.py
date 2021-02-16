class Hospital:
    hospitalList=["N/A","Changi General Hospital",
                "KK Women's and Children's Hospital",
                "Sengkang General Hospital",
                "Singapore General Hospital",
                "Khoo Teck Puat Hospital",
                "Tan Tock Seng Hospital",
                "Alexandra Hospital",
                "National University Hospital",
                "Ng Teng Fong General Hospital",
                "Institute of Mental Health",
                "Bright Vision Hospital",
                "Outram Community Hospital",
                "Sengkang Community Hospital",
                "Yishun Community Hospital",
                "Jurong Community Hospital",
                "Mount Alvernia Hospital",
                 "Others"
                  ]
    hospitalDict=[{"Name": "N/A","Address": "", "Contact" : "", "Beds" : ""},
                  { "Name": "Changi General Hospital","Address": "2 Simei Street 3, Singapore 529889", "Contact" : "67888833", "Beds" : 1000},
                  { "Name": "KK Women's and Children's Hospital","Address": "100 Bukit Timah Rd, Singapore 229899", "Contact" : "62255554", "Beds" : 830},
                  { "Name": "Sengkang General Hospital","Address": "110 Sengkang E Way, Singapore 544886", "Contact" : "69305000", "Beds" : 1000},
                  { "Name": "Singapore General Hospital","Address": "Outram Rd, Singapore 169608", "Contact" : "62223322", "Beds" : 1785},
                  { "Name": "Khoo Teck Puat Hospital","Address": "90 Yishun Central, Singapore 768828", "Contact" : "65558000", "Beds" : 761},
                  { "Name": "Tan Tock Seng Hospital","Address": "11 Jln Tan Tock Seng, Singapore 308433", "Contact" : "62566011", "Beds" : 1700},
                  { "Name": "Alexandra Hospital","Address": "378 Alexandra Rd, Singapore 159964", "Contact" : "64722000", "Beds" : 300},
                  { "Name": "National University Hospital","Address": "5 Lower Kent Ridge Rd, Singapore 119074", "Contact" : "67795555", "Beds" : 1239},
                  { "Name": "Ng Teng Fong General Hospital","Address": "1 Jurong East Street 21, Singapore 609606", "Contact" : "67162000", "Beds" : 700},
                  { "Name": "Institute of Mental Health","Address": "10 Buangkok View, Buangkok Green, Medical Park, 539747", "Contact" : "63892000", "Beds" : 2010},
                  { "Name": "Bright Vision Hospital","Address": "5 Lor Napiri, Singapore 547530", "Contact" : "62485755", "Beds" : 318},
                  { "Name": "Outram Community Hospital","Address": "10 Hospital Blvd, Singapore 168582", "Contact" : "63422338", "Beds" : 545},
                  { "Name": "Sengkang Community Hospital","Address": "Sengkang General Hospital, 110 Sengkang E Way, Singapore 544886", "Contact" : "69306000", "Beds" : 400},
                  { "Name": "Yishun Community Hospital","Address": "2 Yishun Central 2, Singapore 768024", "Contact" : "68078800", "Beds" : 428},
                  { "Name": "Jurong Community Hospital","Address": "1 Jurong East Street 21, Singapore 609606", "Contact" : "67162000", "Beds" : 400},
                  { "Name": "Mount Alvernia Hospital","Address": "820 Thomson Rd, Singapore 574623", "Contact" : "63476688", "Beds" : 319},
                  {"Name": "Others","Address": "Others", "Contact" : "", "Beds" : ""}]


    def __init__(self,name,address,contact,beds):
        self.__name= name
        self.__address= address
        self.__contact=contact
        self.__beds=beds
        self.__transport_vehicles=0

    def get_hospital_id(self):
        return self.__hospital_id

    def set_hospital_id(self,hospital_id):
        self.__hospital_id = int(hospital_id)

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address

    def get_contact(self):
        return self.__contact

    def set_contact(self,contact):
        self.__contact = contact

    def get_beds(self):
        return self.__beds

    def set_beds(self,beds):
        self.__beds = beds

    def coordinates(self):
        pass

    def transport_route(self):
        pass

    def assign_vehicles(self):
        pass

    def remove_vehicles(self):
        pass

    def add_hospital(hospital):
        return Hospital.hospitalList.append(hospital)

    def __str__(self):
        s= "Name : {} \n Address : {} ".format(self.get_name(),self.get_address())
        return s


# test_dict={}
# id=0
# for x in Hospital.hospitalDict:
#     hospital=Hospital(x["Name"],x["Address"])
#     test_dict[id]=hospital
#     id+=1
# print(test_dict)

# for key,value in Hospital.hospitalDict3.items():
#     id=0
#     hospital = Hospital(Hospital.hospitalDict3[id][key],Hospital.hospitalDict3[id][value])
#     id+=1
#     print(hospital)

