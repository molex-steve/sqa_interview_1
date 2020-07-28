##########################################################################
#
#   MOLEX Ltd. Test Library
#   developed by Steve Korber
#   Steve.Korber@molex.com
#
#   Test Library for Test Automation
#
##########################################################################

##########################################################################
# import libraries
###
import requests
import logging

##########################################################################
# constants
###
WEATHER_TOKEN = "c8f59d2781e8cd7f9190c61682d75ec0"

##########################################################################
# test controller class - used for interview question
###
class TestController:
    ######################################################################
    # constructor
    ###
    def __init__(self, level=logging.DEBUG):
        # logger setup
        loggerFormat = logging.Formatter('%(asctime)-15s [%(name)s] [%(levelname)s] %(message)s')
        loggerFilename = "test_library.log"
        handler = logging.FileHandler(loggerFilename)
        handler.setFormatter(loggerFormat)
        self.logger = logging.getLogger("Test Library")
        self.logger.setLevel(level)
        if not self.logger.handlers:
            self.logger.addHandler(handler)
        self.logger.info("started logging")
    ######################################################################
    # methods
    ###
    # get weather
    ###
    def getWeather(self, city=""):
        returnObj = {
            "result": -1,
            "description": "",
            "data": {}
        }
        self.logger.info("getWeather called")
        # send request
        try:
            response = requests.post(
                url="http://api.openweathermap.org/data/2.5/weather?q={},ca&appid={}".format(city, WEATHER_TOKEN)
            )
            if response.status_code == 200:
                results = response.json()
            else:
                returnObj["result"] = -1
                returnObj["description"] = "getWeather:: error from server with status {}".format(response.status_code)
                self.logger.error(returnObj["description"])
                self.logger.error(response.text)
                return returnObj
        except Exception as exc:
            returnObj["result"] = -1
            returnObj["description"] = "getWeather:: {} - {}".format(type(exc).__name__, exc)
            self.logger.error(returnObj["description"])
            return returnObj
        # return temp
        returnObj["result"] = 0
        returnObj["description"] = "getWeather successful"
        returnObj["data"]["temp"] = results["main"]["temp"] - 273.15
        self.logger.info(returnObj["description"])
        self.logger.info(returnObj["data"])
        return returnObj

##########################################################################
# main - this will run if the file isn't being called as a lib
###
if __name__ == "__main__":
    testObj = TestController()
    x = testObj.getWeather("Waterloo")
    print(x)
    x = testObj.getWeather("Blahsndjnsjadnsa")
    print(x)
