import pytest
from pytest_bdd import scenario, given, when, then

@scenario('test_app.feature', 'Publishing the article')
def test_publish():
    pass


@given("I'm an author user")
def author_user():
    pass