import feedparser
import dateutil.parser

SearchStringList = [
    "arcgis",
    "python",
    "linux",
    "programmer",
    "devops"]

Cities = [
    "Denver",
    "eastco",
    "cosprings",
    "albuquerque",
    "dallas",
    "houston",
    "amarillo",
    "boulder",
    "csd",
    "clovis",
    "farmington",
    "fortcollins",
    "grandisland",
    "rockies",
    "lincoln",
    "logan"]

filter_url_list = [
    "https://denver.craigslist.org/example/url"]

filter_keyword_list = [
    "5 plus years",
    "10 Years Experience",
]

cutoff_date = dateutil.parser.parse("2019-05-01 00:00:00Z")

for SearchString in SearchStringList:
    for CityName in Cities:
        url = "http://"+CityName+".craigslist.org/search/jjj?format=rss&query="+SearchString
        feed = feedparser.parse(url)
        for post in feed.entries:
            post['filtered'] = False
            dt_published = dateutil.parser.parse(post['published'])
            post_link = post['link']
            post['summary_detail']['value'] = post['summary_detail']['value'].lower()
            if dt_published > cutoff_date:
                if post_link not in filter_url_list:
                    for filter_keyword in filter_keyword_list:
                        filter_keyword = filter_keyword.lower()
                        if post['summary_detail']['value'].__contains__(filter_keyword):
                            post['filtered'] = True
                    if post['filtered'] is not True:
                        print("Keyword: "+SearchString)
                        print("City Name: "+CityName)
                        print(post['summary_detail']['value'])
                        print(post['link'])
                        print("\n")
