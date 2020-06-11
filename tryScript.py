from flask import (
    Flask,
    render_template,
    request
)
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from flask_cors import CORS
from textblob import TextBlob

# Create the application instance
app = Flask(__name__, template_folder="templates")
CORS(app)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    url = request.args.get('url')
    sauce = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup =BeautifulSoup(urlopen(sauce).read(), 'html.parser')
    result = ""
    for paragraph in soup.find_all('p'):
        result += paragraph.text
    print("request to " + url)  

    return result

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True) 