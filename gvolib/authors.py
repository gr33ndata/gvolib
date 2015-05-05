# Author: Tarek Amr <@gr33ndata> 

from gvolib.dist import Dist 

class Authors(Dist):

    def distribution(self):
        return self._distribution(attr='author')

    def time_distribution(self):
        return self._time_distribution(attr='author')
