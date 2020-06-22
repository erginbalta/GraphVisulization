from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key='eb41a96d0c594b64aeb82c1db47254dd')

def getCountry():
    f = open('C:/repos/NewsSearcher/countries.txt','r')
    countries = f.readline()
    countryList = countries.split(' ')
    return countryList

def getNews(country):
    newsObj = []
    data = newsapi.get_top_headlines(q='corona',country=country,page_size=1)
    articles = data['articles']
    for article in articles:
        news = {}
        source = article['source']
        sourceName = source['name']
        title = article['title']
        description = article['description']
        publishedTime = article['publishedAt']
        news['country'] = country
        news['sourceName'] = sourceName
        news['title'] = title
        news['description'] = description
        news['publishedTime'] = publishedTime
        newsObj.append(news)
    return newsObj


def saveNewsToJson():
    jsonList = []
    countries = getCountry()
    for country in countries:
        liste = getNews(country)
        if liste != []:
            jsonList.append(liste[0])
    with open("data/news.json", "a") as fl:
        json.dump(jsonList,fl)

def readJson():
    jsonData = []
    jsonList = []
    with open("data/news.json","r") as fl:
        jsonData = json.load(fl)
        for news in jsonData:
            dct = {
                "country": news["country"],
                "news": news["description"]
            }
            jsonList.append(dct)
    return jsonList

"""
def saveNews():
    countries = getCountry()
    for country in countries:
        mongoList = getNews(country)
        if mongoList != []:
            inserted = collection.insert_many(mongoList)
            print(str(inserted.inserted_ids) +"    " +country.upper() +" Saved ...")

    print("News Saved Successfully")
"""

