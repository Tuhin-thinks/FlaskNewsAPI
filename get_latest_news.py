import requests
import json

COUNTRY_CODE = 'in'
API_KEY = "033995924bc541d59606eb6bbefeea16"

def getNews():
    
    query_url = f"https://newsapi.org/v2/top-headlines?country={COUNTRY_CODE}&apikey={API_KEY}"
    
    # make query
    resp = requests.get(query_url, timeout=10)
    content = json.loads(resp.text)
    
    urls, titles = [], []
    # collect urls
    for item in content['articles']:
        title = item['title']
        titles.append(title)
        url = item['url']
        urls.append(url)
    
    return urls