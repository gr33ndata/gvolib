from gvolib.feed import Feed
from gvolib.post import Post
from gvolib.authors import Authors
from gvolib.tags import Tags

def main(u=''):
    f = Feed(u)
    f.load(max_pages=2)
    print 'Loaded posts: ', len(f)
    #for p in f[0:5]:
    #    print p
    print Authors(f).time_distribution()
    print Authors(f).distribution()
    print Tags(f).time_distribution()
    print Tags(f).distribution()


if __name__ == '__main__':
    main(u='http://es.globalvoicesonline.org/feed/')