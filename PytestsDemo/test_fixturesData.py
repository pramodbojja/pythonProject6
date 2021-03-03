import pytest
#self is used when applying fixture for entire class
from PytestsDemo.BaseClass import BaseClass

pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):


    def test_editprofile(self,dataload):
        log = self.test_logs()
        log.info(dataload)
        # here it is mandatory to pass the parameter coz u enter data in return[] in confest
        print(dataload)
        log.info(dataload[0])
        print(dataload[0])
        log.info(dataload[1])
        print(dataload[1])