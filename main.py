import fastapi

import uvicorn
import json
from datetime import datetime
import Names
import Bmi
import BostonHousing

# - name: Your own API
#   id: b4f5cc66-01ee-435b-8f41-66248d5e2424
#   description: |
#     - create a simple FastAPI with one route for the path ‘/’ which returns a stringified dictionary with a key ‘data’ and value ‘hello world’
#     - why does the data need to be serialised by `json.dumps`?
#     - Firstly, run the api locally by importing uvicorn into your python script✅
#     - Secondly, remove the code which runs your api and just run the api directly from the terminal, using the uvicorn CLI, as shown in [these docs](https://fastapi.tiangolo.com) ✅
#     - Done using: $  uvicorn main:api  # ✅
#     - test it with `curl` from the terminal ✅
#     - test it with `requests` from python ✅
api = fastapi.FastAPI()


@api.get("/")
def hello_world():
    return "hello!"


@api.get("/ping")
def current_date():
    # datetime object containing current date and time
    now = datetime.now()
    return f"Current time is: {now} !"


# - name: Sending query string data along with our GET requests
#   id: 31bfd7e0-29d6-4910-87f0-7972c7e41965
#   description: |
#     - Create a CSV file containing the `id` (should be uuid4), `first_name`, `age` and `last_name` of people in each row. This will represent our database. ✅
#     - Define a get method for which takes in a query string param `name` and uses this to read the corresponding entry of the CSV  ✅
@api.get("/person")
def get_person(name):
    result = Names.get_name(name)
    return result.to_csv(header=False)


# - name: POSTing
#   id: b4c3275a-4540-4521-9689-2e1069162c81
#   description: |
#     - Create a FastAPI with a resource which has a POST method defined and accepts a person’s height and weight ✅
#     - Save this data in a CSV file row, along with any other useful metadata (time, IP address etc)  ✅
#     - Return the BMI of the person  ✅
#     - Test locally and it will probably fail  ✅
#     - We need to create a data model to avoid a 422 error ✅
@api.post("/person")
def create_person(person: Bmi.BmiPerson, request: fastapi.Request):
    current_ip_address = request.client.host
    result = Bmi.create_person(person, current_ip_address)
    return result


# - name: My first ML API
#   id: 461fa84e-7eb8-4dd1-ac8f-a5bf5c279833
#   description: |
#     “- Fit a sklearn linear regression model to the boston housing dataset (dont worry about anything like validation or testing right now, just `fit` the model)
#     - Create a new API resource ‘/predict’ which calls this model on some data
#       - This resouce should only accept POST requests
#     - Test it locally using python with the `requests` library
#     - Extra: how can you make a POST request, with a payload using `curl` from terminal, to test this new method”
@api.post("/predict_boston")
def create_person(boston_house: BostonHousing.House):
    result = BostonHousing.predict(boston_house)
    return result


if __name__ == "__main__":
    uvicorn.run(api, port=8000, host="127.0.0.1")


# - name: Real database
#   id: b0a535e2-e8e8-4385-bcca-38128fc228b4
#   description: |
#     - Create an API that connects to a database you have set up
#     - Implement GET methods to get different entries from different tables using query string parameters
#     - Implement POST methods to create a new entry
#     - Implement PUT methods to update an existing entry
#     - Be careful what you do with this code if it contains your database credentials


# - name: Manual EC2 deployment
#   id: 85000c8c-a9ff-46b0-95bd-cb85efb479ae
#   description: |
#     - Spin up a new EC2 instance and download the keys
#     - SSH in
#       - make sure to specify the correct path to the keys
#       - don’t forget to allow inbound connections from your IP address on the port your api will listen for requests on
#     - Deploy a FastAPI on EC2
