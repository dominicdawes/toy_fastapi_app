from fastapi import FastAPI
from pydantic import BaseModel
import uuid


app = FastAPI()


# ======== CLASS OBJECTS ======== #

# Define Pydantic models for the responses
class SumResponse(BaseModel):
    sum: int

class PDFCaptureResponse(BaseModel):
    uuid: str
    url: str


# ======== URL ENDPOINTS ======== #

# Root endpoint
@app.get("/")
async def root():
    return {"success": "Hello Server"}

# Endpoint for addition
@app.get("/test_addition", response_model=SumResponse)
async def test_addition(num1: int, num2: int):
    result = num1 + num2
    return {"sum": result}

# Endpoint for capturing PDF info
@app.get("/pdf_capture", response_model=PDFCaptureResponse)
async def pdf_capture(file: str):
    unique_id = str(uuid.uuid4())  # Generate a unique UUID
    return {"uuid": unique_id, "url": file}