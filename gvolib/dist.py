# Author: Tarek Amr <@gr33ndata> 

class Dist:

    def __init__(self, feed):
        self.feed = feed

    def _to_attr_items(self, post, attr):
        attr_items = ''
        if isinstance(getattr(post, attr), str):
            attr_items = [getattr(post, attr)]
        if isinstance(getattr(post, attr), unicode):
            attr_items = [getattr(post, attr)]
        elif isinstance(getattr(post, attr), list):
            attr_items = getattr(post, attr)
        else:
            attr_items [str(getattr(post, attr))]
        return attr_items

    def _distribution(self, attr='author', attr_processor=None):
        if not attr_processor:
            attr_processor = self._to_attr_items
        authmap = {}
        for post in self.feed:
            attr_items = attr_processor(post, attr)
            for attr_item in attr_items:
                authmap[attr_item] = authmap.get(attr_item, 0) + 1
        return authmap

    def _time_distribution(self, attr='author', attr_processor=None):
        if not attr_processor:
            attr_processor = self._to_attr_items
        authmap = {}
        for post in self.feed:
            authmap[post.date] = authmap.get(post.date, {})
            attr_items = attr_processor(post, attr)
            for attr_item in attr_items:
                authmap[post.date][attr_item] = authmap[post.date].get(attr_item, 0) + 1
        return authmap