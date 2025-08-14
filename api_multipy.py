from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class multiplymodel(BaseModel):
    a:int
    b:int


def multiply(a:int, b:int):
    return a*b

@app.post("/multiply")
def multiply_numbers(model: multiplymodel):
    return multiply(model.a, model.b)

