from app import app
import urllib.request,json
from .models import source
from .models import article

Source = source.Source

Article = article.Article

# Getting news api key
api_key = app.config['NEWS_API_KEY']

# Getting the top headlines url
top_headlines_url = app.config["NEWS_API_HEADLINES_URL"]
# Getting the sources url
sources_url = app.config["NEWS_API_SOURCES_URL"]
# Getting headlines by source name url
headlines_by_source_url= app.config["NEWS_API_HEADLINES_BY_SOURCE_URL"]
# Getting headlines by search name url
headlines_by_search_url=app.config["NEWS_API_HEADLINES_BY_SEARCH_URL"]
#Getting headlines by category name url
headlines_by_category_url=app.config["NEWS_API_HEADLINES_BY_CATEGORY_URL"]

def get_sources():
    '''
    Function that gets the json response (i.e news sources) to our url request
    '''
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
            
    return sources_results



def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain source details

    Returns :
        sources_results: A list of source objects
    '''
    sources_results = []
    for source in sources_list:
      if source.get('id'):
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        
        source_object = Source(id,name,description)
        sources_results.append(source_object)

    return sources_results


def get_top_headlines():
    '''
    Function that gets the json response (i.e world top headlines news) to our url request
    '''
    get_headlines_url = top_headlines_url.format(api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_articles(headlines_results_list)
            
    return headlines_results


def process_articles(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for article in articles_list:
      if article.get('urlToImage'):
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        article_img = article.get('urlToImage')
        published_at = article.get('publishedAt')
        content = article.get('content')

        article_object = Article(author,title,description,url,article_img,published_at,content)
        articles_results.append(article_object)

    return articles_results    

