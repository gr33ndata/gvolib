# Author: Tarek Amr <@gr33ndata> 

from gvolib.dist import Dist 

class Authors(Dist):

    def __init__(self, feed):
        Dist.__init__(self,  feed) 
        self.data = {}
        for p in feed:
            self.data[p.author] = self.data.get(p.author, []) + [p]

    def __len__(self):
        'Returns number of authors'
        return len(self.data.keys)

    def __getitem__(self, author_name):
        return self.data.get(author_name, [])

    def __iter__(self):
        for a, posts in self.data.items():
            yield (a, len(posts))

    def distribution(self):
        return self._distribution(attr='author')

    def time_distribution(self):
        return self._2d_distribution(attr1='date', attr2='author')
