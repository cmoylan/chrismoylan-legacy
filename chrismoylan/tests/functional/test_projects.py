from chrismoylan.tests import *

class TestPortfolioController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='portfolio', action='index'))
        # Test response...
