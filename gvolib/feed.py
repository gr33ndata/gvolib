import feedparser

from gvolib import feed_links
from gvolib.post import Post 

class Feed:

    def __init__(self, url=''):
        ''' Initialize Feed
            url can be name like 'en', 'es', etc.
            or real url 
        '''
        self.posts = []
        self.url = feed_links.get(url, url)

    def __len__(self):
        'Returns number of loaded posts'
        return len(self.posts)

    def __getitem__(self, idx):
        return self.posts[idx]

    def __iter__(self):
        for p in self.posts:
            yield p

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
            p = Post(item)
            if p.date == oldest_date:
                return
            self.posts.append(p) 
        self.load(page+1,max_pages=max_pages, oldest_date=oldest_date)
    
    def get_posts(self):
        ''' Get list of posts
            You better user __iter__ though
        '''
        return self.posts

