from gvolib.dist import Dist 

class Tags(Dist):

    def distribution(self):
        return self._distribution(attr='tags')

    def time_distribution(self):
        return self._time_distribution(attr='tags')