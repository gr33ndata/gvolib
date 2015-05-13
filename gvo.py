import sys

import pandas as pd
from argparse import ArgumentParser

from gvolib.feed import Feed
from gvolib.post import Post
from gvolib.authors import Authors
from gvolib.tags import Tags
from gvolib.progress import Progress 

def parse_cli():

    parser = ArgumentParser(description='Global Voices Scrapper')

    parser.add_argument(
        '-u', '--url', 
        nargs='?', default='es', const='es', 
        metavar='es',
        help='Specify the feed URL'
    )

    parser.add_argument(
        '-p', '--pages', 
        nargs='?', default=5, const=5, 
        metavar=5,
        help='Specify the number of pages to retrieve'
    )

    parser.add_argument(
        '-v', '--verbose', 
        action='store_true', 
        help='Print debug messages'
    )

    return parser.parse_args()

def dump_distribution(dist, filename='', index_label=''): 
    for key in dist:
        dist[key] = pd.Series(dist[key])
    dist_df = pd.DataFrame(dist).fillna(0)
    dist_df.to_csv(
        filename, 
        index_label=index_label, 
        encoding='utf-8'
    )

def print_debug(msg, silent=False):
    if not silent: print msg

def main(args):

    max_pages = int(args.pages)
    silent = not args.verbose

    f = Feed(args.url)
    prgrs = Progress(n=max_pages, percent=10, silent=silent)
    f.load(max_pages=max_pages,prgrs=prgrs)
    print_debug('Loaded posts: {0}'.format(len(f)), silent=silent)

    for p in f:
        print 'Post: {0}'.format(p.link)
        print 'tweeps:'
        print set(p.twitter_users)
        print 'hashtags:'
        print set(p.twitter_hashtags)
    return

    #print Authors(f).distribution()
    auth_dist = Authors(f).time_distribution()
    dump_distribution(auth_dist, filename='auth_date_dist.csv', index_label='author')
    
    #print Tags(f).distribution()
    tags_dist = Tags(f).time_distribution()
    dump_distribution(tags_dist, filename='tags_date_dist.csv', index_label='tag')

    #print Authors(f).distribution()
    tags_dist = Tags(f).author_distribution()
    dump_distribution(tags_dist, filename='tags_auth_dist.csv', index_label='author')
    

if __name__ == '__main__':

    args = parse_cli()
    main(args)