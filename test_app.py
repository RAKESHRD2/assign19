import json
from app import app

def test_create_tweet_success():
    client = app.test_client()

    data = {'text': 'Hello, this is my first tweet!'}
    response = client.post('/tweets', json=data)

    assert response.status_code == 201
    assert 'message' in response.get_json()
    assert 'text' in response.get_json()

def test_create_tweet_missing_text():
    client = app.test_client()

    data = {'username': 'user123'}  
    response = client.post('/tweets', json=data)

    assert response.status_code == 400
    assert 'error' in response.get_json()

