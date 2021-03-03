# Any pytest should start with test or end with test
#pytest method names should start with test
#any code must wrap in method
# in pytest there is a concept called mark, in cucumber we call tagging, in test NG we called them as group

import pytest

def test_fixureDemo(setup):
    print("I will execute steps in fixture demo method")


@pytest.mark.xfail # this method will run but doesnt report pass or fail
def test_Programfirst():
    print("Hello")

@pytest.mark.smoke
def test_greet():
    print("Good Morning")

# self is not required because we are not wrapping all this test methods in class

def test_crossbrowser(crossbrowser):
    print(crossbrowser)


def test_multipledata(multipledata):
    #print(multipledata)
    print(multipledata[2])





