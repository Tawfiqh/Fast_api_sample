# %%
import pandas as pd
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime

NAME_FILENAME = "BMI.csv"


def get_name(name):
    df = pd.read_csv(NAME_FILENAME)
    result = df[df["first_name"] == name]
    return result


CSV_COLUMNS = ["height_m", "weight_kg", "bmi", "current_time", "IP_Address"]


class BmiPerson(BaseModel):
    height_m: float
    weight_kg: float
    bmi: float = None


def get_current_time():
    now = datetime.now()
    return now


#     - method defined and accepts a person’s height and weight ✅
#     - Save this data in a CSV file row, along with any other useful metadata (time, IP address etc)
#     - Return the BMI of the person
def create_person(person: BmiPerson, ip_address):
    # BMI - person's mass in kg divided by the square of their height in metres (kg/m2)
    # https://www.bbc.co.uk/news/health-43697948
    bmi = person.weight_kg / (person.height_m ** 2)
    person.bmi = bmi
    person_dict = jsonable_encoder(person)

    person_dict["current_time"] = get_current_time()
    person_dict["IP_Address"] = ip_address

    df_new_row = pd.DataFrame(person_dict, columns=CSV_COLUMNS, index=[1])
    df = pd.read_csv(NAME_FILENAME)

    df = df.append(df_new_row, ignore_index=True)
    df.to_csv(NAME_FILENAME, index=False)
    print(df)
    return person.bmi


if __name__ == "__main__":
    person = BmiPerson(height_m=1.65, weight_kg=65.2)
    bmi = create_person(person, "0.0.0.0")
    print(f"bmi:{bmi}")

# %%
