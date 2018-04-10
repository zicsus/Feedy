import feedparser
import re

class Parser:
    
    platforms = {
        "ign": {
            "all" : "http://feeds.ign.com/ign/games-all"
        },
        "gamespot": {
            "all" : "https://www.gamespot.com/feeds/mashup/"
        }
    }

    def __init__(self, url):
        self.url = url

    def update(self):
        self.__feeds = feedparser.parse(self.url).entries

    def top5(self):
        top5 = []
        for i in range(0, 5):
            feed = self.__feeds[i]
            title = feed.title
            description = self.cleanhtml(feed.description)
            media = feed.media_content[0]['url']
            top5.append({"title":title, "description":description, "media":media})

        return top5

    def cleanhtml(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext


