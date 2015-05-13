import re

class Links:

    def __init__(self, feed_item):
        self.text = feed_item.content[0].value
        self.links = self.extract_links(self.text)

    def __len__(self):
        'Returns number of links found'
        return len(self.links)

    def __iter__(self):
        for l in self.links:
            yield l

    def extract_links(self, text):
        return re.findall(r'href=[\'"]?([^\'" >]+)', text)

    def twitter_links(self):
        tlinks = []
        for item in self.links:
            m = re.match(r'http[s]?://twitter.com/([^\'" >]+)', item)
            if m:
                tparams = m.group(1)
                if tparams.startswith('hashtag'):
                    hashtagm = re.match(r'hashtag/([^\'"?/]+)', tparams)
                    if hashtagm:
                        tlinks.append(('hashtag', hashtagm.group(1)))
                elif tparams.startswith('search'):
                    pass
                elif tparams.startswith('share'):
                    pass
                else:
                    userm = re.match(r'([^\'"?/]+)', tparams)
                    if userm:
                        tlinks.append(('user', userm.group(1)))
        return tlinks

    def twitter_hashtags(self):
        return [ 
            h[1] for h in self.twitter_links()
            if h[0] == 'hashtag'
        ]

    def twitter_users(self):
        return [ 
            t[1] for t in self.twitter_links()
            if t[0] == 'user'
        ]