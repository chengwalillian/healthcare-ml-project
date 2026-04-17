```bash
uv venv && source .venv/Scripts/activate
uv pip install -e .
cp .env.example .env
```

## inputing Data from kaggle

```bash
python -m scripts.ingest
```

## Training the  Model

```bash
python -m ml.train
```

## Running the API

```bash
python -m app.main
```

## Example Request

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 45,
    "Gender": "Male",
    "Blood Type": "O+",
    "Medical Condition": "Diabetes",
    "Billing Amount": 2000.5,
    "Admission Type": "Emergency",
    "Insurance Provider": "Cigna",
    "Medication": "Aspirin"
  }'
```

## Example Response

```json
{ "predicted_test_result": "Abnormal"}
```
