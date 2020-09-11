import pytest
# import sys
# import os

# sys.path.insert(0, os.getcwd())

from flix.domainmodel.director import Director

def test_init():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None

def test_equal():
    director1 = Director("Taika Waititi")
    director2 = Director("Peter Jackson")
    director3 = Director("Taika Waititi")

    assert (director1 == director2) == False
    assert (director1 == director3) == True

def test_less_than():
    director1 = Director("Taika Waititi")
    director2 = Director("Peter Jackson")

    assert (director1 < director2) == False

def test_hash():
    director1 = Director("Taika Waititi")
    assert hash(director1) == hash("Taika Waititi")
    director2 = Director("Peter Jackson")
    assert hash(director2) == hash("Peter Jackson")