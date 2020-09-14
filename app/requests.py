from app import app
import urllib.request,json
from .models import source

Source = source.Source

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
