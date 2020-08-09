import feedparser
from threading import Thread
from multiprocessing import Pool

rssList  = [
    "http://rss.slashdot.org/Slashdot/slashdotMain",
    "https://feeds.twit.tv/floss.xml",
    "https://undeadly.org/cgi?action=rss",
    "http://www.NetBSD.org/changes/rss-netbsd.xml",
    "https://lobste.rs/t/programming.rss",
    "http://news.ycombinator.com/rss"
    ]

def parseNewsFeed(rssURL):
    feed = feedparser.parse(rssURL)
    print("\nTitle of the RSS feed is : " + feed.feed.title)
    feed_entries = feed.entries
    print("Number of items in feed is : " + str(len(feed_entries) ))
    cnt = 1
    for feed_entry in feed_entries:
        output_string = "({}) {}".format(str(cnt) , feed_entry.title)
        cnt = cnt +1
        print(output_string)

def main():
    process_pool = Pool(8)
    with process_pool:
        process_pool.map(parseNewsFeed,rssList)



if __name__ == "__main__":
    main()
