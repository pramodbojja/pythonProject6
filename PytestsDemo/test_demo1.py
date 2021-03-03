# Any pytest should start with test or end with test
#pytest method names should start with test
#any code must wrap in method
# to run all test at once , first you must do it in edit configure
#To run specific test u must select method unique name. -k is for unique words,-v is for detailed report like meta data
# -s to print logs
#you can run individula file py.test test.demo1.py -v -s
# in pytest there is a concept called mark, in cucumber we call tagging, in test NG we called them as group
# for group test we put py.test -m smoke -v -s in terminal;here m is used for smoke or regression
# to skip you can use skip method as shown below
# fixtures meaning in some test cases you need to run a function before the test or after the test
#def setup(): # if you want to run this function first in test then you should pass this function as an argument in
#test_fixuredemo

#html report = pip install pytest-html, to get html report pytest --html=report.html(here you get full report)
import pytest


def test_thirdmethod():
    msg = "Hello"
    assert msg == "HI", "Test is failed"


@pytest.mark.smoke
@pytest.mark.skip
def test_Programfour():
    a = 2
    b =4
    assert a+b ==6 , "Addition do not match"

