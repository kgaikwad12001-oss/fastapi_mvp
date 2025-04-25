from fastapi import APIRouter
from app.schemas.input_schema import PredictRequest
from app.model.load_model import predict

router = APIRouter()

@router.post("/predict")
def get_prediction(req: PredictRequest):
    features = [
        req.sepal_length,
        req.sepal_width,
        req.petal_length,
        req.petal_width
    ]
    prediction = predict(features)
    return {"prediction": prediction}
