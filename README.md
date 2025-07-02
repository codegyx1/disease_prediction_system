
# Disease Prediction System

This is a Streamlit web application for predicting the risk of three diseases:

- **Diabetes**
- **Parkinson's disease**
- **Heart disease**

The app uses pre-trained machine learning models to analyze user input and provide instant risk predictions for each condition.

## Features

- **Diabetes Prediction:**  
  Enter basic health info (pregnancies, glucose, BMI, etc.) and get a diabetes risk prediction.

- **Parkinson's Disease Prediction:**  
  Fill in vocal and jitter measurements to check for Parkinson’s risk.

- **Heart Disease Prediction:**  
  Input clinical and demographic data to assess the likelihood of heart disease.

- **Intuitive UI:**  
  Sidebar menu for easy navigation between prediction types.

## Getting Started

### Prerequisites

- Python 3.7 or higher

Required Python packages:
- `streamlit`
- `streamlit-option-menu`
- `pickle` (Python standard library)

Pre-trained model files needed:
- `dia_prediction.sav`
- `parkinsons_prediction.sav`
- `heart_prediction.sav`

> **Note:**  
> The models must be present in the correct path.  
> In the current code, they are loaded from a local directory (e.g., `C:\Users\Hp\Desktop\python project\`).  
> Update these paths in `app.py` as needed for your environment.

### Installation

Clone the repository:

```bash
git clone https://github.com/codegyx1/disease_prediction_system.git
cd disease_prediction_system
```

Install dependencies:

```bash
pip install streamlit streamlit-option-menu
```

Place the model files:  
Save your `.sav` model files in an accessible directory and update the file paths in `app.py` if needed.

## Usage

Run the app:

```bash
streamlit run app.py
```

Open your browser and visit the URL provided in your terminal (usually http://localhost:8501).

Choose a prediction type using the sidebar, fill in the required health parameters, and click the test button to get your prediction.

## Notes

- Ensure all input fields are filled with valid values for accurate predictions.
- The app is intended for educational/demo purposes and should not be used as medical advice.
- You may need to retrain or update the machine learning models for best results.


## Author

codegyx1

If you have questions or suggestions, feel free to open an issue or pull request.

---
