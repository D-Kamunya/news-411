from flask import render_template
from app import app
from .requests import get_sources,get_top_headlines,get_source_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources()
    top_headlines=get_top_headlines()[0:15]
    return render_template('index.html',sources = news_sources,headlines = top_headlines)


@app.route('/category/<category_name>')
def category_news(category_name):

    '''
    View category news page function that returns the category-news page and its data for the category selected
    '''
    return render_template('category-news.html',category_name=category_name)    


@app.route('/source/<source_id>')
def source_news(source_id):

    '''
    View source news page function that returns the source-news page and its data for the source selected
    '''
    source_articles=get_source_news(source_id)
    return render_template('source-news.html',articles=source_articles,source=source_id)        