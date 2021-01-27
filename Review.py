
class Review():
    count_review_id = 0

    def __init__(self, reviewfirst_name, reviewlast_name, reviewfeedback):

        Review.count_review_id += 1
        self.__review_id = Review.count_review_id
        self.__reviewfeedback = reviewfeedback
        self.__reviewfirst_name = reviewfirst_name
        self.__reviewlast_name = reviewlast_name


    def get_review_id(self):
        return self.__review_id
    def set_review_id(self, review_id):
        self.__review_id = review_id

    def get_reviewfeedback(self):
        return self.__reviewfeedback
    def set_reviewfeedback(self, feedback):
        self.__feedback = feedback

    def get_reviewfirst_name(self):
        return self.__reviewfirst_name
    def set_reviewfirst_name(self, reviewfirst_name):
        self.__reviewfirst_name = reviewfirst_name

    def get_reviewlast_name(self):
        return self.__reviewlast_name
    def set_reviewlast_name(self, reviewlast_name):
        self.__reviewlast_name = reviewlast_name
