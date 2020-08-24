import pytest, sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.genre import Genre

def test_init():
    genre1 = Genre("Horror")
    assert repr(genre1) == "<Genre Horror>"
    genre2 = Genre("")
    assert repr(genre2) == "<Genre None>"

def test_equal():
    genre1 = Genre("Horror")
    genre2 = Genre("")
    genre3 = Genre("Horror")

    assert (genre1 == genre2) == False
    assert (genre1 == genre3) == True

def test_less_than():
    genre1 = Genre("Horror")
    genre2 = Genre("Comedy")

    assert (genre1 < genre2) == False

def test_hash():
    genre1 = Genre("Horror")
    assert hash(genre1) == hash("Horror")
    genre2 = Genre("Comedy")
    assert hash(genre2) == hash("Comedy")