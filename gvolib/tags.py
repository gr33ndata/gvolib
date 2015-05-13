from gvolib.dist import Dist 

class Tags(Dist):

    def __init__(self, feed):
        Dist.__init__(self,  feed) 
        self.data = {}
        for p in feed:
            for t in p.tags:
                self.data[t] = self.data.get(t, []) + [p]

    def __len__(self):
        'Returns number of tags'
        return len(self.data.keys)

    def __getitem__(self, tag_name):
        return self.data.get(tag_name, [])

    def __iter__(self):
        for t, posts in self.data.items():
            yield (t, len(posts))

    def distribution(self):
        return self._distribution(attr='tags')

    def time_distribution(self):
        return self._2d_distribution(attr1='date', attr2='tags')

    def author_distribution(self):
        return self._2d_distribution(attr1='author', attr2='tags')