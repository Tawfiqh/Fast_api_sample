# %%
import pandas as pd
from pydantic import BaseModel
from pydantic.types import UUID4
from fastapi.encoders import jsonable_encoder


NAME_FILENAME = "names.csv"


def get_name(name):
    df = pd.read_csv(NAME_FILENAME)
    result = df[df["first_name"] == name]
    return result


if __name__ == "__main__":
    get_name("Ben")

# %%
