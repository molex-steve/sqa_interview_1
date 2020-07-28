# Embedded Automation Interview Question 1

* [Test Library](#test-library)
* [Test Library API](#test-library-api)

<a name="test-library"></a>

## Test Library

This project is developed to be used as an interview question for Embedded Automation.<br/><br/>
The library uses the requests library to grab specifc data and return it.<br/><br/>
The purpose of the test is to do the following:

* Clone the repo (or download zip)
* Install Python3 (if not installed, Python 3.7 recommended)
* Install requirements using `pip install -r requirements.txt`
* Create a Python script at the root level without editing this repo folder
* Import/create the class object from the code
* Use the class to do the following:
    * Print weather data from the city Molex is in (ie. Waterloo)
    * Perform test to be certain the Library returned the data successfully
    * Perform test using unittest?

### Return Object

---

The return object is the same for all Libraries. 

It is a dictionary object of the same structure:

```json
{
    "result": 0,
    "description": "successful",
    "data": {}
}
```

`description` is a string with a simple message about the status of the result.

`result` is an integer: 0 is successful, -1 is failure, and 1 is try again.

`data` is an embedded dictionary object that can have any data that is needed on return.


### Log Files

---

| Filename | Description | 
| --- | --- |
| test_library.log | Logging from TestController obj |

### Example Usage

---

```python
from TestLibrary import TestController

testObj = TestController()
```

<a name="test-library-api"></a>

## Test Library API

* [Constructor](#constructor)
* [Get Weather](#get-weather)

<a name="constructor"></a>

### Constructor

```python
TestController()
```

| Attribute | Type | Description | Required |
| --- | --- | --- | --- |
| `none` |  |  |  |

Example usage:

```python
testObj = TestController()
```

<sub><sup>[back](#test-library-api)</sup></sub>

<a name="get-weather"></a>

### Get Weather

Gets the current temperature from the given city.

```python
def getWeather(self)
```
| Attribute | Type | Description | Required |
| --- | --- | --- | --- |
| `city` | string | Current city in Ontario, Canada. | `True` |

Example usage:

```python
results = testObj.getWeather("Waterloo")
```

Example response:

```json
{
	"result": 0, 
	"description": "getWeather successful", 
	"data": 
		{
			"temp": 27.32000000000005
		}
}
```

<sub><sup>[back](#test-library-api)</sup></sub>
