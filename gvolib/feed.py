import feedparser

class Feed:

    def __init__(self, url=''):
        self.posts = []
        self.url = url

    def __len__(self):
        'Returns number of loaded posts'
        return len(self.posts)

    def load(self, page=0, max_pages=10, oldest_date='2010-11'):
        ''' Load posts in self.posts
            page: Initial page to start with
            max_pages: Maximum number of pages to read
            oldest_date: oldest date for posts to read
            We stop when reaching max_pages or oldest_date
            For each page, we get 10 posts (depends on website rss)
        '''
        if page >= max_pages:
            return

        feedurl = '%s/?posts_per_page=15&paged=%d' % (self.url, page)               
        fp = feedparser.parse(feedurl)
        for item in fp.entries:
            #print item.keys()
            #print item
            tags = ''
            for tag in item.tags:
                tags = tags + tag['term'].strip() + '+'
            post = {'title': item.title.strip(),
                    'tags': tags,
                    'date': '%d-%02d' % (item.published_parsed[0], item.published_parsed[1]),
                    'authors': item.author,
                    'link': item.link
                    }
            print post
            if post['date'] == oldest_date:
                return
            self.posts.append(post)
        print page, len(self.posts) 
        self.load(page+1,max_pages=max_pages, oldest_date=oldest_date)
    
    def get_posts(self):
        return self.posts

