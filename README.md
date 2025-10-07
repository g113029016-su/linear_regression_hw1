# HW1 - Simple Linear Regression (CRISP-DM Framework)

## 1. Business Understanding
本專案目的在於示範如何利用簡單線性回歸 (y = ax + b + noise) 進行資料分析與建模，並讓使用者互動式地調整參數，以了解模型與資料的關係。

## 2. Data Understanding
使用者可自訂：
- a（斜率）
- b（截距）
- noise（雜訊強度）
- number of points（資料點數）

這些參數影響資料生成的線性分布與擬合效果。

## 3. Data Preparation
資料由 numpy 隨機生成，包含 x 與 y 兩個變數，透過指定參數產生 y = ax + b + noise。

## 4. Modeling
使用 sklearn 的 `LinearRegression` 建立模型，並計算迴歸係數、截距與 R² 分數。

## 5. Evaluation
比較模型預測線與真實線之間的差距，並以散點圖與回歸線可視化結果。

## 6. Deployment
使用 Streamlit 部署應用，可於本地或 Streamlit Cloud 執行。

## streamlit
https://linear-regression-hw1.streamlit.app/

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
