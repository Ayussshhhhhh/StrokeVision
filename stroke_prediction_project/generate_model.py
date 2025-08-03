from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("/Users/ayush/Documents/stroke_prediction_project/healthcare-dataset-stroke-data.xls")

# Define features and target
X = data.drop(['id', 'stroke'], axis=1)
y = data['stroke']

# Define preprocessing for categorical and numerical columns
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
numerical_cols = ['age', 'avg_glucose_level', 'bmi']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ]), numerical_cols),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False))
        ]), categorical_cols)
    ])

# Define the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier(eval_metric='logloss'))  # Removed use_label_encoder
])

# Split data and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Save the pipeline
joblib.dump(pipeline, '/Users/ayush/Documents/stroke_prediction_project/stroke_app/models/stroke_prediction_pipeline.pkl')
print("Model saved successfully at /Users/ayush/Documents/stroke_prediction_project/stroke_app/models/stroke_prediction_pipeline.pkl")