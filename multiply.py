from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/multiply")
async def multiply_numbers(numbers: Numbers):
    """
    Multiple 2 integers and return result
    """
    result = numbers.num1 * numbers.num2
    return {"result": result}