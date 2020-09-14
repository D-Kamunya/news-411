from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@app.route('/category/<category_name>')
def category_news(category_name):

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('category-news.html',category_name=category_name)    