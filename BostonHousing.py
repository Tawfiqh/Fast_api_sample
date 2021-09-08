# %%
import pandas as pd
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from sklearn import datasets, model_selection
from sklearn import linear_model
import joblib


SAVED_MODEL_NAME = "linear_regressor_boston.joblib"


def train_model():
    X, y = datasets.load_boston(return_X_y=True)

    boston_model = linear_model.LinearRegression(normalize=True)
    boston_model.fit(X, y)

    joblib.dump(boston_model, SAVED_MODEL_NAME)

    return boston_model


def load_moodel():
    try:
        boston_model = joblib.load(SAVED_MODEL_NAME)
        print("Loaded model from file")
    except:
        print("Couldn't load from file -- training model from scratch")
        boston_model = train_model()

    return boston_model


class House(BaseModel):
    Crim: float
    Zn: float
    Indus: float
    Chas: float
    Nox: float
    Rm: float
    Age: float
    Dis: float
    Rad: float
    Tax: float
    Ptratio: float
    B: float
    Lstat: float

    def to_numpy(self):
        return [
            self.Crim,
            self.Zn,
            self.Indus,
            self.Chas,
            self.Nox,
            self.Rm,
            self.Age,
            self.Dis,
            self.Rad,
            self.Tax,
            self.Ptratio,
            self.B,
            self.Lstat,
        ]


model = load_moodel()


def predict(house_to_predict: House):
    prediction = model.predict([house_to_predict.to_numpy()])
    return prediction[0]


# - name: My first ML API
#   id: 461fa84e-7eb8-4dd1-ac8f-a5bf5c279833
#   description: |
#     “- Fit a sklearn linear regression model to the boston housing dataset
#       (dont worry about anything like validation or testing right now, just `fit` the model)
#     - Test it locally using python with the `requests` library
#     - Extra: how can you make a POST request, with a payload using `curl` from terminal, to test this new method”
if __name__ == "__main__":
    # X, y = datasets.load_boston(return_X_y=True)
    # print(y[10])

    house = House(
        Crim=1.3444,
        Zn=1.3444,
        Indus=1.3444,
        Chas=1.3444,
        Nox=1.3444,
        Rm=1.3444,
        Age=1.3444,
        Dis=1.3444,
        Rad=1.3444,
        Tax=1.3444,
        Ptratio=1.4,
        B=1.3444,
        Lstat=1.3444,
    )

    result = predict(house)
    print("Result:", result)

# %%
