class Post:

    def __init__(self, feed_item):
        self.data = feed_item

    @property
    def title(self):
        return self.data.title.strip()

    @property
    def author(self):
        return self.data.author

    @property
    def link(self):
        return self.data.link

    @property
    def tags(self):
        return [tag['term'].strip() for tag in self.data.tags]

    @property
    def date(self):
        return '%d-%02d' % (
            self.data.published_parsed[0], 
            self.data.published_parsed[1]
        )
