import requests

def get_books():
    response = requests.get('https://allosaurus.delahayeyourself.info/api/books/')
    
    if response.status_code == 200:
        return response.json()
    return None
