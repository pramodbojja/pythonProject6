import pytest
#This is runnning fixture for entire class then use @pytest,mark,usefixtures

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute steps in fixture demo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixture demo method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixture demo method")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixture demo method")

    def test_fixtureDemo5(self):
        print("I will execute steps in fixture demo method")