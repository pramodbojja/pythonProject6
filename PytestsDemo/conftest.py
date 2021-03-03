import pytest


# The conftest.py file serves as a means of providing fixtures for an entire directory.
# Fixtures defined in a conftest.py
# can be used by any test in that package without needing to import them (pytest will automatically discover them).
# fixture contain all common fucntions like invoking browsers that are used by other test cases
# fixtures make required functions for all other test cases
# if you want to run setup function only once before the class then you can use scope
# if you dont put scope in calss it will be in method level
# fixture will also help you load the data: for example you dont have to fillout data every time for user log in.
#when you put yield it will print last foreample if u apply for class it will print at the end of class

@pytest.fixture(scope="class")
def setup():
    print("Execute this function first")
    yield
    print("Execute this after")


def test_fixtureDemo(setup):
    print("I will execute steps in fixture demo method")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["pramod", "reddy", "automechanize.com"]

# request is one of the instance of the fixture
# request is usaable when you have some values in fixture
# here parameters has to be in list
@pytest.fixture(params=["Chrome","Firefox","IE"])
def crossbrowser(request):
    return request.param

#in case of multipple data in every run how to pass
#here we are running fixture for one single method with param multiple data
@pytest.fixture(params=[("Chrome","auto","Mechanize"),("Firefox","rana","run"),("IE","RR")])
def multipledata(request):
    return request.param