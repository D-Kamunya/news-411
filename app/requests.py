from app import app
import urllib.request,json

# Getting news api key
api_key = app.config['NEWS_API_KEY']

# Getting the sources url
sources_url = app.config["NEWS_API_SOURCES_URL"]
# Getting headlines by source name url
headlines_by_source_url= app.config[" NEWS_API_HEADLINES_BY_SOURCE_URL"]
# Getting headlines by search name url
headlines_by_search_url=app.config["NEWS_API_HEADLINES_BY_SEARCH_URL"]
#Getting headlines by category name url
headlines_by_category_url=app.config["NEWS_API_HEADLINES_BY_CATEGORY_URL"]