from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ Backend is running!'

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/events')
def get_events():
    url = 'https://www.timeout.com/sydney/things-to-do'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    events = []
    for item in soup.select('.card-content')[:10]:
        title = item.select_one('a').text.strip()
        link = item.select_one('a')['href']
        date = "Date not found"
        location = "Sydney"

        events.append({
            'title': title,
            'date': date,
            'location': location,
            'link': link
        })

    return jsonify(events)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
