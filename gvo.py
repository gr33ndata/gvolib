from gvolib.feed import Feed

def main(u=''):
    f = Feed(u)
    f.load(max_pages=2)
    print 'Loaded posts: ', len(f)

if __name__ == '__main__':
    main(u='http://es.globalvoicesonline.org/feed/')