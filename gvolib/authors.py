# Author: Tarek Amr <@gr33ndata> 

from gvolib.dist import Dist 

class Authors(Dist):

    def __init__(self, feed):
        Dist.__init__(self,  feed) 

    def distribution(self):
        return self._distribution(attr='author')

    def time_distribution(self):
        return self._2d_distribution(attr1='date', attr2='author')
