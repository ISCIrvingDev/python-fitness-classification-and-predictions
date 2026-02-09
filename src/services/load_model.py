"""
Docstring for services.load_model

Servicio para cargar el modelo
"""

import joblib
import pandas as pd

MODEL_PATH = "./models/calories_burned_model.pkl"


class CaloriesModel:
    """
    Docstring for CaloriesModel
    """
    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, data: dict) -> float:
        """
        Docstring for predict

        :param self: Description
        :param data: Description
        :type data: dict
        :return: Description
        :rtype: float
        """
        df = pd.DataFrame([{
            "Age": data["Age"],
            "Gender": data["Gender"],
            "Weight (kg)": data["Weight_kg"],
            "Height (m)": data["Height_m"],
            "Max_BPM": data["Max_BPM"],
            "Avg_BPM": data["Avg_BPM"],
            "Resting_BPM": data["Resting_BPM"],
            "Session_Duration (hours)": data["Session_Duration_hours"],
            "Workout_Type": data["Workout_Type"],
            "Fat_Percentage": data["Fat_Percentage"],
            "Water_Intake (liters)": data["Water_Intake_liters"],
            "Workout_Frequency (days/week)": data["Workout_Frequency_days_week"],
            "Experience_Level": data["Experience_Level"],
            "BMI": data["BMI"]
        }])

        prediction = self.model.predict(df)[0]
        return float(prediction)
