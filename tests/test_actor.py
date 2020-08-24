import pytest, sys, os

sys.path.insert(0, os.getcwd())

from domainmodel.actor import Actor

def test_init():
    actor1 = Actor("Angelina Jolie")
    assert repr(actor1) == "<Actor Angelina Jolie>"
    actor2 = Actor("")
    assert repr(actor2) == "<Actor None>"
    actor3 = Actor(42)
    assert repr(actor3) == "<Actor None>"

def test_equal():
    actor1 = Actor("Angelina Jolie")
    actor2 = Actor("Brad Pitt")
    actor3 = Actor("Angelina Jolie")

    assert (actor1 == actor2) == False
    assert (actor1 == actor3) == True

def test_less_than():
    actor1 = Actor("Angelina Jolie")
    actor2 = Actor("Brad Pitt")

    assert (actor1 < actor2) == True

def test_hash():
    actor1 = Actor("Angelina Jolie")
    assert hash(actor1) == hash("Angelina Jolie")
    actor2 = Actor("Brad Pitt")
    assert hash(actor2) == hash("Brad Pitt")

def test_add_colleague():
    actor1 = Actor("Angelina Jolie")
    actor2 = Actor("Brad Pitt")

    assert actor1.check_if_this_actor_worked_with(actor2) == False
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2) == True
    assert actor2.check_if_this_actor_worked_with(actor1) == True