import sys

import pandas as pd
from argparse import ArgumentParser

from gvolib.feed import Feed
from gvolib.post import Post
from gvolib.authors import Authors
from gvolib.tags import Tags

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

    return parser.parse_args()

def dump_distribution(dist, filename=''): 
    for key in dist:
        dist[key] = pd.Series(dist[key])
    dist_df = pd.DataFrame(dist).fillna(0)
    dist_df.to_csv(filename)

def main(args):
    f = Feed(args.url)
    f.load(max_pages=int(args.pages))
    print 'Loaded posts: ', len(f)

    #print Authors(f).distribution()
    auth_dist = Authors(f).time_distribution()
    dump_distribution(auth_dist, filename='auth_dist.csv')
    
    #print Tags(f).distribution()
    tags_dist = Tags(f).time_distribution()
    dump_distribution(tags_dist, filename='tags_dist.csv')


if __name__ == '__main__':

    args = parse_cli()
    main(args)