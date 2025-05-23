from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Root route to confirm backend is running
@app.route('/')
def home():
    return '✅ Backend is running!'

# Events scraping API
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

# Run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
