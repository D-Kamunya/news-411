import unittest
from app.models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("Manish Singh","Indian fantasy25M at over $2.5B valuation","Dream Sports, the headquartered firm builds what it calls…","https://techcrunch.com/2020/09/14/indian-fantasy-sports-app-dream11s-parent-firm-raises-225m-at-over-2-5b-valuation/","https://static.coindesk.com/wp-content/uploads/2020/09/claudio-schwarz-purzlbaum-htol9OLeW20-unsplash.jpg","2020-09-1413:47:13Z","The folks building the next generation of digital money in Switzerland understand the need to collaborate.Stablecoins, digital tokens pegged one i")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()