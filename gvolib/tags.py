from gvolib.dist import Dist 

class Tags(Dist):

    def distribution(self):
        return self._distribution(attr='tags')

    def time_distribution(self):
        return self._2d_distribution(attr1='date', attr2='tags')

    def author_distribution(self):
        return self._2d_distribution(attr1='author', attr2='tags')