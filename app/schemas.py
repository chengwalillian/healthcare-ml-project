from pydantic import BaseModel


class PredictRequest(BaseModel):
    Age: int
    Gender: str
    Blood_Type: str
    Medical_Condition: str
    Insurance_Provider: str
    Billing_Amount: float
    Admission_Type: str
    Medication: str


class PredictResponse(BaseModel):
    predicted_test_result: str
