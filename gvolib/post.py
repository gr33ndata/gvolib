class Post:

    def __init__(self, feed_item):
        self.data = feed_item

    def __str__(self):
        return '\nTitle: {title}' \
               '\nAuthor: {author}' \
               '\nTags: {tags}' \
               '\nLink: {link}' \
               ''.format(
            title=self.encoder(self.title),
            author=self.encoder(self.author),
            tags=self.encoder(self.tags),
            link=self.encoder(self.link)
        )

    def encoder(self, field):
        ''' UTF-8 encoding shit
            Let's encode when writing to file or screen
        '''
        if isinstance(field, list):
            return ', '.join([
                item.encode('utf-8')
                for item in field
            ])
        elif isinstance(field, str):
            return field.encode('utf-8')
        elif isinstance(field, unicode):
            return field.encode('utf-8')
        else:
            print type(field)
            return field

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
        return [
            tag['term'].strip() 
            for tag in self.data.tags
        ]

    @property
    def date(self):
        return '%d-%02d' % (
            self.data.published_parsed[0], 
            self.data.published_parsed[1]
        )
