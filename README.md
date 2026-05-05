# House Price Predictor

A machine learning web application that predicts house prices based on property features using a trained regression model and a Flask-based web interface.

## Overview

This project implements a house price prediction system that uses a pre-trained machine learning model to estimate residential property prices. The application provides a user-friendly web interface where users can input property characteristics and receive instant price predictions.

## Features

- **ML-Powered Predictions**: Uses a trained regression model with feature selection (SelectKBest)
- **Web Interface**: Clean, intuitive HTML form for easy input
- **Feature Engineering**: Handles both numerical and categorical features with preprocessing
- **Scalable Architecture**: Includes scaler and model persistence using joblib

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn, joblib
- **Data Processing**: pandas, numpy
- **Deployment**: Gunicorn WSGI server, Azure App Service
- **Python**: 3.11.6

## Project Structure

```
house-price-predictor/
├── app.py                 # Flask application and prediction logic
├── model.pkl              # Pre-trained model with scaler and selector
├── requirements.txt       # Python dependencies
├── runtime.txt           # Python version specification
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Web interface
└── .github/              # GitHub configuration
```

## Installation

### Prerequisites
- Python 3.11.6 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/shaiksuhail-824/house-price-predictor.git
cd house-price-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Locally

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Making Predictions

1. Navigate to the home page
2. Fill in the property details:
   - **Numerical Features**: Lot Frontage, Lot Area, Overall Quality, Year Built, etc.
   - **Categorical Features**: Zone, Lot Shape, Neighborhood, Exterior Quality, etc.
3. Submit the form to receive the predicted sale price

## Model Details

### Features Used
The model uses 50 key features selected through SelectKBest feature selection:

**Numerical Features** (14):
- LotFrontage, LotArea, OverallQual, YearBuilt, YearRemodAdd
- MasVnrArea, TotalBsmtSF, GrLivArea, FullBath, HalfBath
- Fireplaces, GarageCars, WoodDeckSF, OpenPorchSF

**Categorical Features** (36):
- Zone (MSZoning), Lot Shape, Neighborhood, Exterior Quality
- Foundation, Basement Quality, Heating Quality, Central Air
- Kitchen Quality, Fireplace Quality, Garage Type/Quality/Condition
- and more...

### Preprocessing
- **Numerical Features**: Log transformation (log1p) applied to skewed features
- **Categorical Features**: One-hot encoding for selected categories
- **Scaling**: StandardScaler applied during training and prediction

### Model Output
- Predictions are in log scale
- Output is converted back to original price scale using inverse transformation (expm1)
- Results are returned as integer values in USD

## Dependencies

| Package | Purpose |
|---------|---------|
| flask | Web framework |
| gunicorn | WSGI HTTP Server |
| scikit-learn | Machine learning algorithms |
| joblib | Model serialization |
| numpy | Numerical computing |
| pandas | Data manipulation |

## API Endpoints

### GET `/`
Returns the home page with the prediction form.

### POST `/predict`
Accepts form data with property features and returns a prediction.

**Form Parameters**:
- Numerical: `LotFrontage`, `LotArea`, `OverallQual`, `YearBuilt`, etc.
- Categorical: `MSZoning`, `LotShape`, `Neighborhood`, etc.

**Response**:
- HTML page with predicted sale price or error message

## Error Handling

The application includes error handling for:
- Invalid input values (non-numeric where numeric expected)
- Missing form fields (defaults are provided)
- Model prediction errors

Error messages are displayed on the result page.

## Deployment on Azure

This application is configured for deployment on Azure App Service:

### Prerequisites
- Azure subscription
- Azure CLI installed
- GitHub repository connected to Azure

### Deployment Steps

1. **Create Resource Group** (optional):
```bash
az group create --name myResourceGroup --location eastus
```

2. **Create App Service Plan**:
```bash
az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1 --is-linux
```

3. **Create Web App**:
```bash
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name house-price-predictor --runtime "PYTHON|3.11"
```

4. **Configure Startup Command** (in Azure Portal):
   - Go to Configuration → General settings
   - Set Startup Command: `gunicorn --workers 4 --worker-class sync --bind 0.0.0.0:8000 app:app`

5. **Deploy from GitHub**:
   - Go to Deployment Center in Azure Portal
   - Connect your GitHub repository
   - Select the main branch
   - Azure will automatically deploy on push

6. **Verify Deployment**:
   - Check the Application Insights for logs
   - Visit your app URL: `https://<app-name>.azurewebsites.net`

### Configuration Files for Azure
Ensure these files are in your repository:
- `requirements.txt` - All Python dependencies
- `runtime.txt` - Python version (3.11.6)
- `app.py` - Flask application entry point

### Environment Variables (if needed)
Set in Azure Portal → Configuration → Application settings:
```
FLASK_ENV=production
```

### Monitoring & Logs
- View logs in Azure Portal: **App Service → Log stream**
- Use Application Insights for performance monitoring
- Check diagnostic logs for troubleshooting

## Language Composition

- **HTML**: 55% (16,228 bytes)
- **Python**: 45% (7,391 bytes)

## Future Improvements

- Add data validation and constraints
- Implement batch prediction capability
- Add model interpretability features (SHAP values)
- Create API endpoint for programmatic access
- Add unit tests
- Implement input logging for model improvements
- Add CI/CD pipeline with GitHub Actions

## License

This project is open source and available for educational and personal use.

## Author

[shaiksuhail-824](https://github.com/shaiksuhail-824)

## Repository

- **URL**: https://github.com/shaiksuhail-824/house-price-predictor
- **Created**: May 2026
- **Status**: Active
- **Deployment**: Azure App Service
