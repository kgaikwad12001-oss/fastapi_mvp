# Iris Classifier

A web application that predicts Iris flower species based on flower measurements using machine learning.

## Features

- FastAPI backend with machine learning model
- Browser-based UI for predictions
- RESTful API endpoint for programmatic access
- Random Forest Classifier trained on the Iris dataset

## Requirements

- Python 3.12
- Dependencies listed in requirements.txt

## Project Structure

```
.
├── app
│   ├── api
│   │   └── predict.py
│   ├── main.py
│   ├── model
│   │   ├── load_model.py
│   │   └── train_model.py
│   └── schemas
│       └── input_schema.py
├── requirements.txt
└── ui
    └── index.html
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Train the model:
```bash
python app/model/train_model.py
```

## Usage

1. Start the server:
```bash
uvicorn app.main:app --reload
```

2. Access the application:
- Web UI: Open `http://localhost:8080` in your browser. Depending on which port your application is running, make changes in `fetch()` in 'index.html' and your terminal command 

> `uvicorn app.main:app --reload --port 8080
`.
- API Documentation: Visit `http://localhost:8080/docs`

## API Reference

### Predict Endpoint

`POST /api/predict`

Request body:
```json
{
    "sepal_length": float,
    "sepal_width": float,
    "petal_length": float,
    "petal_width": float
}
```

Response:
```json
{
    "prediction": string
}
```

Example:
```bash
curl -X POST "http://localhost:8000/api/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

## Web Interface

The web interface provides input fields for:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Enter the measurements and click "Predict" to get the predicted Iris species.