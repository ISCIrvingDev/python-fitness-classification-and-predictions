"""
Esquemas Pydantic:

- Validaicon automatica
- Tipos claros
- Errores HTTP 422 si el input es invalido
"""

from typing import Literal
from pydantic import BaseModel, Field


class CaloriesPredictionRequest(BaseModel):
    """
    Docstring for CaloriesPredictionRequest
    """
    Age: int = Field(..., gt=0)
    Gender: Literal["Male", "Female"]
    Weight_kg: float = Field(..., gt=0)
    Height_m: float = Field(..., gt=0)
    Max_BPM: int = Field(..., gt=0)
    Avg_BPM: int = Field(..., gt=0)
    Resting_BPM: int = Field(..., gt=0)
    Session_Duration_hours: float = Field(..., gt=0)
    Workout_Type: Literal["Cardio", "Strength", "Yoga"]
    Fat_Percentage: float = Field(..., ge=0, le=100)
    Water_Intake_liters: float = Field(..., ge=0)
    Workout_Frequency_days_week: int = Field(..., ge=0, le=7)
    Experience_Level: int = Field(..., ge=1, le=3)
    BMI: float = Field(..., gt=0)


class CaloriesPredictionResponse(BaseModel):
    """
    Docstring for CaloriesPredictionResponse
    """
    predicted_calories: float
