import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# Load the data
@st.cache
def load_data():
    data = pd.read_csv("data.csv")  # Replace with the actual path to your data
    return data

data = load_data()

# Data Preprocessing
st.header("Data Preprocessing")

# Drop unnecessary columns
data = data.drop(['Unnamed: 32', 'id'], axis=1)

# Map diagnosis labels 'M' and 'B' to binary values
data.diagnosis.replace(to_replace=dict(M=1, B=0), inplace=True)

# EDA
st.header("Exploratory Data Analysis")

# Display summary statistics
st.write("Summary Statistics:")
st.write(data.describe())

# Create a box plot
st.subheader("Box Plot for Dataset")
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, orient="h")
plt.title("Box Plot for Dataset")
plt.xlabel("Values")
st.pyplot(plt)

# Feature Selection
st.header("Feature Selection")

# Split the data into features and target
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Perform feature selection using chi-squared test (you can add other methods as well)
st.write("Selected Features:")
# ... (include the feature selection code here)
# st.write(selected_features)

# Model Selection
st.header("Model Selection")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train machine learning models (e.g., Random Forest, SVM, ANN)

# Random Forest Classifier
st.subheader("Random Forest Classifier")
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)
rf_y_pred = rf_classifier.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_y_pred)
rf_report = classification_report(y_test, rf_y_pred)
st.write("Random Forest Classifier Accuracy:", rf_accuracy)
st.write("Random Forest Classification Report:")
st.write(rf_report)

# Support Vector Machine (SVM)
st.subheader("Support Vector Machine (SVM)")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)
svm_classifier.fit(X_train_scaled, y_train)
svm_y_pred = svm_classifier.predict(X_test_scaled)
svm_accuracy = accuracy_score(y_test, svm_y_pred)
svm_report = classification_report(y_test, svm_y_pred)
st.write("SVM Classifier Accuracy:", svm_accuracy)
st.write("SVM Classification Report:")
st.write(svm_report)
