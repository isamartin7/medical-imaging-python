import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = "https://api.duckduckgo.com/?q=python+programming&format=json"

    # Act
    response = requests.get(url)
    body = response.json()

    # Assert
    assert response.status_code == 202 #200 y 202 son OK code #to verify that the request was successful
    assert 'Python' in body['AbstractText'] #check tha actual content of the response, should have in the body something related with 'python'
