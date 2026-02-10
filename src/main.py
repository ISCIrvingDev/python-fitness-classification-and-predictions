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

from fastapi import FastAPI, Depends, Request

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

from src.schemas.schemas import (
    CaloriesPredictionRequest,
    CaloriesPredictionResponse,
    FitnessLevelPredictionRequest,
    FitnessLevelPredictionResponse
)
from src.services.load_model import CaloriesModel, FitnessLevelModel
from src.services.security import validate_api_key
from src.services.rate_limit import limiter

app = FastAPI(
    title="Fitness ML API",
    description="API para predicción de calorías quemadas y nivel de aptitud fisica",
    version="1.2.0"
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Cargar modelo al iniciar
calories_model = CaloriesModel()
fitness_model = FitnessLevelModel()

@app.get("/")
def health_check():
    """
    Docstring for health_check
    """
    return {"status": "ok"}

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded. Try again later."
        }
    )


@app.post(
    "/predict/calories",
    response_model=CaloriesPredictionResponse,
    dependencies=[Depends(validate_api_key)]
)
# The 'request' object must be passed to the endpoint for slowapi to work
# from fastapi import FastAPI, Request
# @limiter.limit("10/minute") # Limite en este endpoint
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
    response_model=FitnessLevelPredictionResponse,
    dependencies=[Depends(validate_api_key)]
)
# The 'request' object must be passed to the endpoint for slowapi to work
# from fastapi import FastAPI, Request
# @limiter.limit("5/minute") # Limite en este endpoint
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
