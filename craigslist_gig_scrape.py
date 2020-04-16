from feedparser import parse
import dateutil.parser

# TODO Allow passing a command line arguement that defines a CSV of search keywords
SearchStringList = [
    "arcgis",
    "python",
    "linux"
    "programmer",
    "devops"
    ]


# TODO Allow passing a command line arguement that defines a CSV of CL sub-sites (cities) to query
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
    "logan"
    ]

filter_url_list = [
    "https://denver.craigslist.org/example/url"]


# TODO Allow passing a command line arguement that defines a CSV of search keywords to exclude
filter_keyword_list = [
    # "5 plus years",
    # "10 Years Experience",
]

#TODO Change this to be automatically chosen from 1 week, 1 month, 1 year back from current date
cutoff_date = dateutil.parser.parse("2020-03-01 00:00:00Z")

for SearchString in SearchStringList:
    for CityName in Cities:
        url = "http://"+CityName+".craigslist.org/search/ggg?format=rss&query="+SearchString
        feed = parse(url)
        for post in feed.entries:
            post['filtered'] = False
            dt_published = dateutil.parser.parse(post['published'])
            published_str = dt_published.strftime("%y-%m-%d %H:%M:%S")
            post_link = post['link']
            if dt_published > cutoff_date:
                if post_link not in filter_url_list:
                    for filter_keyword in filter_keyword_list:
                        filter_keyword = filter_keyword.lower()
                        if filter_keyword in post['summary_detail']['value'].lower():
                            post['filtered'] = True
                    if post['filtered'] is not True:
                        print("Keyword: "+SearchString)
                        print("City Name: "+CityName)
                        print("Post Date: " + published_str)
                        print(post['summary_detail']['value'])
                        print(post['link'])
                        print("\n")
