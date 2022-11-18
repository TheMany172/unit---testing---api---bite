from lib.Challenge import *
from unittest.mock import Mock

def test_catfacts():
    mock_response = Mock()
    fake_catfacts = Mock()
    fake_catfacts.get.return_value = mock_response
    mock_response.json.return_value = {"fact":"The first official cat show in the UK was organised at Crystal Palace in 1871."}

    catfacts1 = CatFacts(fake_catfacts)
    assert catfacts1.provide() == "Cat fact: The first official cat show in the UK was organised at Crystal Palace in 1871."



"""
{"fact":"The first official cat show in the UK was organised at Crystal Palace in 1871.","length":78}%
"""