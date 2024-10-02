from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the response
class SumResponse(BaseModel):
    sum: int

@app.get("/test_addition", response_model=SumResponse)
async def test_addition(num1: int, num2: int):
    result = num1 + num2
    return {"sum": result}
