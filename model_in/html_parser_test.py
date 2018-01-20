from html.parser import HTMLParser
from urllib import request


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('handle_starttag', tag)

    def handle_endtag(self, tag):
        print('handle_endtag', tag)

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag', tag)

    def handle_data(self, data):
        print('handle_data', data)

    def handle_comment(self, data):
        print('handle_comment', data)

    def handle_entityref(self, name):
        print('handle_entityref', name)

    def handle_charref(self, name):
        print('handle_charref', name)


parser = MyHTMLParser()

with request.urlopen("http://12306.com") as f:
    data = f.read()
    print(parser.feed(data.decode('utf-8')))
