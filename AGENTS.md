# AGENTS.md - Fitness ML Project Guide

## Project Overview
Python machine learning project for fitness calorie burn prediction using FastAPI, scikit-learn, and data analysis tools.

## Development Environment

### Virtual Environment
- Uses `.venv` virtual environment (Python 3.11)
- Activate: `.venv\Scripts\activate` (Windows)
- Key dependencies: pandas, numpy, scikit-learn, fastapi, jupyter

### Core Dependencies
```
pandas          # Data manipulation
numpy           # Numerical operations  
scikit-learn    # ML modeling and preprocessing
fastapi         # API framework
joblib          # Model serialization
jupyter         # Notebook development
matplotlib      # Data visualization
seaborn         # Statistical visualization
kagglehub       # Dataset downloading
```

## Commands

### Running Applications
```bash
# Start FastAPI server
python src/main.py
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Start Jupyter notebook
jupyter notebook

# Jupyter lab
jupyter lab
```

### Python Execution
```bash
# Run specific Python file
python src/main.py

# Run with virtual environment
.venv\Scripts\python.exe src/main.py
```

### Data Processing
```bash
# Notebooks should be run sequentially:
# 1. notebooks/1-data-exploration.ipynb - Data cleaning and analysis
# 2. notebooks/2-pipeline-calorie-burn-prediction.ipynb - Model training
```

## Project Structure

```
python-fitness/
├── src/
│   └── main.py                 # FastAPI application entry point
├── notebooks/
│   ├── 1-data-exploration.ipynb    # Data analysis and cleaning
│   └── 2-pipeline-calorie-burn-prediction.ipynb  # ML pipeline
├── datasets/
│   └── 1-fitness-tracker-dataset.csv   # Cleaned dataset
├── ref/                      # Documentation and references
├── .venv/                    # Virtual environment
└── AGENTS.md                 # This file
```

## Code Style Guidelines

### Python Code Style
- Follow PEP 8 formatting
- Use meaningful variable names in English or Spanish (consistent within project)
- Functions and variables use snake_case
- Classes use PascalCase
- Constants use UPPER_SNAKE_CASE
- Maximum line length: 88-100 characters

### Import Organization
```python
# Standard library imports first
import os
import sys

# Third-party imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from fastapi import FastAPI

# Local imports (if any)
```

### Documentation
- Use docstrings for functions and classes
- Include parameter descriptions and return types
- Use Spanish comments for business logic, English for technical comments
- Keep inline comments minimal and explanatory

### Error Handling
- Use specific exception types
- Log errors appropriately
- Provide meaningful error messages in Spanish for user-facing APIs

## Machine Learning Pipeline

### Data Processing
- Load data using pandas: `pd.read_csv()`
- Handle categorical variables with `astype("category").cat.codes`
- Split data: `train_test_split(X, y, test_size=0.2, random_state=42)`
- Scale features with `StandardScaler()` when needed

### Model Development
- Use `Pipeline` for preprocessing and modeling steps
- Hyperparameter tuning with `RandomizedSearchCV`
- Cross-validation with `cross_val_score()`
- Model persistence with `joblib.dump()` and `joblib.load()`

### Parameter Naming (RandomizedSearchCV)
When using Pipeline, prefix parameters with step name:
```python
param_dist = {
    'model__n_estimators': np.arange(50, 200, 50),  # Note the 'model__' prefix
    'model__max_depth': [3, 5, 7, 10, None],
    'model__min_samples_split': [2, 3, 4],
    'model__min_samples_leaf': [1, 2, 4],
    'model__max_features': [0.5, 'sqrt', 'log2']
}
```

## API Development

### FastAPI Patterns
- Use Pydantic models for request/response validation
- Return JSON responses with Spanish keys for user-facing data
- Load models once at startup for performance
- Handle errors with appropriate HTTP status codes

### Model Loading
```python
import joblib
from fastapi import FastAPI

app = FastAPI()
model = joblib.load("fitness_calorie_predictor.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"calorias_quemadas": prediction[0]}
```

## Testing

### Manual Testing
- Test API endpoints with tools like Postman or curl
- Validate predictions with known data points
- Check model performance metrics during development

### Model Validation
- Use hold-out test set for final evaluation
- Monitor MAE (Mean Absolute Error) for regression tasks
- Validate feature importance and model interpretability

## Development Workflow

1. **Data Exploration**: Run `1-data-exploration.ipynb` to understand and clean data
2. **Model Development**: Run `2-pipeline-calorie-burn-prediction.ipynb` to train and tune models
3. **API Integration**: Update `src/main.py` with new model features
4. **Testing**: Test API endpoints and model predictions
5. **Documentation**: Update relevant documentation

## File Naming Conventions

- Datasets: Use numbered prefix (e.g., `1-fitness-tracker-dataset.csv`)
- Notebooks: Use numbered prefixes for sequential execution order
- Models: Use descriptive names with version (e.g., `fitness_calorie_predictor_v1.pkl`)

## Common Issues and Solutions

### Pipeline Parameter Errors
When using `RandomizedSearchCV` with `Pipeline`, remember to prefix parameter names with the pipeline step name followed by double underscore (`__`).

### Memory Management
- For large datasets, consider using chunking or streaming
- Clean up intermediate variables in notebooks
- Use appropriate data types to reduce memory usage

### Model Persistence
- Save trained models using `joblib.dump()`
- Include version information in model filenames
- Test model loading before deploying to production

## Environment Variables
No specific environment variables are currently required for this project.