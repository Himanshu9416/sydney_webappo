# Sydney Events Web App

This is a simple project I built as part of an internship test. It scrapes upcoming events in Sydney, Australia using Python and displays them on a webpage.

## Features
- Scrapes data from a real event website (Timeout Sydney).
- Displays event title, location, and a "GET TICKETS" button.
- Users must enter their email to proceed to the ticket site.
- Automatically updates events list by fetching latest data when the page loads.

## Tools Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, BeautifulSoup

## How to Run

### Backend:
```bash
cd backend
pip install -r ../requirements.txt
python server.py
```

### Frontend:
Just open `frontend/index.html` in your browser after starting the backend.

