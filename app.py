import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("📈 Simple Linear Regression - CRISP-DM Demo")

st.markdown("### Step 1: Data Generation")
a = st.slider("Slope (a)", -5.0, 5.0, 2.0, 0.1)
b = st.slider("Intercept (b)", -10.0, 10.0, 1.0, 0.5)
noise = st.slider("Noise Level", 0.0, 10.0, 1.0, 0.5)
num_points = st.slider("Number of Points", 10, 200, 50)

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, num_points)
y = a * x + b + np.random.normal(0, noise, num_points)

st.markdown("### Step 2: Modeling")
X = x.reshape(-1, 1)
model = LinearRegression().fit(X, y)
pred_y = model.predict(X)

st.write(f"**Model Coefficient (â)**: {model.coef_[0]:.3f}")
st.write(f"**Intercept (b̂)**: {model.intercept_:.3f}")
st.write(f"**R² Score**: {model.score(X, y):.3f}")

# Visualization
fig, ax = plt.subplots()
ax.scatter(x, y, color='blue', label='Data')
ax.plot(x, pred_y, color='red', label='Fitted line')
ax.legend()
st.pyplot(fig)

st.markdown("### Step 3: Evaluation & Insights")
st.write("調整上方參數觀察模型的學習效果與 R² 變化。")

st.markdown("---")
st.caption("Created for HW1 | CRISP-DM Framework Demonstration")
