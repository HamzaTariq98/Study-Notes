from fastapi import FastAPI
from pydantic import BaseModel, Field
from prediction_model.predict import perform_predictions
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Survival Prediction with FastAPI",
    description="CI CD tranining example",
    version='1.0'
)


origins = ['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


class Data(BaseModel):
    pclass: list[int]
    sex: list[str]
    age: list[int]
    sibsp: list[int]
    parch: list[int]
    fare: list[float]
    embarked: list[str]
    class_: list[str] = Field(alias="class")  # 1) fix python class keyword
    who: list[str]
    adult_male: list[bool]
    deck: list[str]
    embark_town: list[str]
    alone: list[bool]


@app.get("/")
def read_root():
    print('hi')
    return {"Status": "The app is running",
            "Items":[1,2,5,4,6,5]}



@app.post("/")
def read_root(data:Data):

    data = data.model_dump()
    data['class'] = data.pop('class_') # 2) fix python class keyword

    predictions = perform_predictions(data)

    predictions = [int(num) for num in predictions ] # Fix API cannt return ndarray response


    return {"predictions": predictions}
    




if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8005)

