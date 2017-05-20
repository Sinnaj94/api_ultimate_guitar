from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
import requests
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


app = Flask(__name__)
api = Api(app, '/api')


base_url = 'https://ultimate-guitar.com'
tabs_base_url = 'https://tabs.ultimate-guitar.com'
class Default(Resource):
	def get(self):
		return {'version': '1.0'}

class Tab(Resource):
	def get(self, url):
		return 'abc'

class SearchTabs(Resource):
	def get(self, searchterm):
		raw = requests.get('https://www.ultimate-guitar.com/search.php?search_type=title&value=' + searchterm)
		#print(raw)
		soup = BeautifulSoup(raw.text, 'html.parser')
		results = soup.find_all("a", { "class" : "result-link" })
		_return = []
		for result in results:
			_current = {'name' : innerHTML(result), 'url' : result['href']}
			_return.append(_current)
		return _return

def innerHTML(element):
    return element.decode_contents(formatter="html").strip()

def getTextFromUrl(url):
	return None

@app.route('/')
def index():
	return render_template('index.html')

api.add_resource(SearchTabs, '/search/<searchterm>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')