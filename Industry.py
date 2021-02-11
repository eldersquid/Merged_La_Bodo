class Industry:
    industryList = ["N/A", "Medical"]
    industryDict = [
        {"Industry": "N/A"},
        {"Industry": "Medical"}]

    def __init__(self,industry):
        self.__industry=industry

    def get_industry(self):
        return self.__industry

    def set_industry(self, industry):
        self.__industry = industry

    def get_industry_id(self):
        return self.__industry_id

    def set_industry_id(self, industry_id):
        self.__industry_id = int(industry_id)