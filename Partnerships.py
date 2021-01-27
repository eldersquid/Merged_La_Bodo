class Partnerships:

    def __init__(self, company, resources, industry):

        self.__company = company
        self.__resources = resources
        self.__industry = industry

    def set_Partnerships_id(self, Partnerships_id):
        self.__Partnerships_id = int(Partnerships_id)

    def get_Partnerships_id(self):
        return self.__Partnerships_id

    def set_company(self, company):
        self.__company = company

    def get_company(self):
        return self.__company

    def set_resources(self, resources):
        self.__resources = resources

    def get_resources(self):
        return self.__resources

    def set_industry(self, industry):
        self.__industry = industry

    def get_industry(self):
        return self.__industry
