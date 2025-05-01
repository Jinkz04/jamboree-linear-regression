import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

st.title("🎓 Jamboree Education - Linear Regression Model")
st.info("👋 Upload the CSV file to begin. It must be the same dataset used in your Colab notebook.")

st.write("Case Study by Ajinkya Nikam | DSML July23")

# Load data
uploaded_file = st.file_uploader("Upload the Jamboree dataset CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Dataset Preview")
    st.write(df.head())

    if st.checkbox("Show Summary Stats"):
        st.write(df.describe())

    if st.checkbox("Show Correlation Heatmap"):
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="YlGnBu", ax=ax)
        st.pyplot(fig)

    # Feature selection
    st.subheader("⚙️ Feature Selection")
    features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']
    target = 'Chance of Admit '

    X = df[features]
    y = df[target]

    # Split
    test_size = st.slider("Test Size (%)", 10, 50, 20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)

    # Model training
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.subheader("📈 Model Evaluation")
    st.write(f"R² Score: {r2_score(y_test, y_pred):.4f}")
    st.write(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

    # Prediction
    st.subheader("🎯 Predict Admission Chance")
    input_data = []
    for feature in features:
        min_val = float(df[feature].min())
        max_val = float(df[feature].max())
        mean_val = float(df[feature].mean())
        value = st.slider(f"{feature}", min_val, max_val, mean_val)
        input_data.append(value)

    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    st.success(f"Predicted Chance of Admit: {prediction:.4f}")
else:
    st.info("Please upload the dataset to get started.")
