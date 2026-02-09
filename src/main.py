"""Entry Point"""

# from fastapi import FastAPI
# import joblib, pandas as pd

# app = FastAPI()
# model = joblib.load("fitness_calorie_predictor.pkl")

# @app.post("/predict")
# def predict(data: dict):
#     df = pd.DataFrame([data])
#     prediction = model.predict(df)
#     return {"calorias_quemadas": prediction[0]}

from fastapi import FastAPI
from src.schemas.schemas import (
    CaloriesPredictionRequest,
    CaloriesPredictionResponse,
    FitnessLevelPredictionRequest,
    FitnessLevelPredictionResponse
)
from src.services.load_model import CaloriesModel, FitnessLevelModel

app = FastAPI(
    title="Fitness ML API",
    description="API para predicción de calorías quemadas y nivel de aptitud fisica",
    version="1.1.0"
)

# Cargar modelo al iniciar
calories_model = CaloriesModel()
fitness_model = FitnessLevelModel()

@app.get("/")
def health_check():
    """
    Docstring for health_check
    """
    return {"status": "ok"}


@app.post(
    "/predict/calories",
    response_model=CaloriesPredictionResponse
)
def predict_calories(
    request: CaloriesPredictionRequest
):
    """
    Docstring for predict_calories

    :param request: Description
    :type request: CaloriesPredictionRequest
    """
    prediction = calories_model.predict(request.dict())

    return CaloriesPredictionResponse(
        predicted_calories=round(prediction, 2)
    )

@app.post(
    "/predict/fitness-level",
    response_model=FitnessLevelPredictionResponse
)
def predict_fitness_level(request: FitnessLevelPredictionRequest):
    """
    Docstring for predict_fitness_level

    :param request: Description
    :type request: FitnessLevelPredictionRequest
    """
    level_code, level_name = fitness_model.predict(request.dict())

    return FitnessLevelPredictionResponse(
        level_code=level_code,
        level_name=level_name
    )

print("Servidor corriendo en: http://127.0.0.1:8000/docs")
