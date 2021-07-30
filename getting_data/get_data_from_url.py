import requests
from bs4 import BeautifulSoup
class GetDataFromUrl:
    def __init__(self):
        self.soup = None
    """
    Gets the data from a url and returns it as a string.
    :param url: a url ex: (https://example.com/page.html')
    :return a string with html heads
    """
    def getHTMLText(self, url):
        raw_html = requests.get(url)
        print('Status code', raw_html.status_code)
        coverpage = raw_html.content
        return coverpage

    """
        Gets cleaned data and removes html tags, etc.
        :param url: a url ex: (https://example.com/page.html')
        :return a string with just body text
        """
    def cleanURLData(self, raw_html):
        self.soup = BeautifulSoup(raw_html, 'html5lib')
        title = self.soup.find_all('h1')
        title = str.join(' ', [w.getText() for w in title])
        text = self.soup.find_all('p')
        text = str.join(' ', [w.getText() for w in text])
        return title, text
    """
    Gets the data from a url and returns it as a string.
    :param url: a url ex: (https://example.com/page.html')
    :return a string with just body text.
    """
    def getDataFromURL(self, url):
        raw_html = self.getHTMLText(url)
        cleaned_text = self.cleanURLData(raw_html)
        return cleaned_text

"""
Testing it on a CNN article
"""
if __name__ == '__main__':
    url = 'https://www.cnn.com/2021/07/26/health/us-coronavirus-monday/index.html'
    print(GetDataFromUrl().getDataFromURL(url))