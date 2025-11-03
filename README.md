# 💰 Insurance Charges Prediction App

## 🧩 Overview  
This project is a **Streamlit web application** that predicts **medical insurance charges** based on a person’s **age**, **BMI (Body Mass Index)**, and **smoking status**.  
It uses a **machine learning model** trained on the **Insurance dataset** to provide real-time cost predictions.

---

## 🧠 Problem Statement  
Medical insurance costs vary significantly across individuals depending on health-related factors.  
The goal is to build a predictive model that estimates insurance charges given input features like:
- Age  
- BMI  
- Smoking status  

This helps users understand how these factors impact premiums and assists insurance companies in cost estimation.

---

## 🎯 Objective  
To develop an **interactive and user-friendly web app** that:
1. Accepts user inputs for `Age`, `BMI`, and `Smoker` status.  
2. Predicts the **estimated insurance cost** using a trained regression model.  
3. Provides a clean, responsive interface using **Streamlit**.

---

## 📊 Dataset  
**Source:** [Kaggle - Medical Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)  

| Feature | Description |
|----------|--------------|
| `age` | Age of the individual |
| `bmi` | Body Mass Index |
| `smoker` | Whether the person is a smoker (`yes`/`no`) |
| `charges` | Medical insurance cost (Target Variable) |

---

## 🛠️ Tools & Libraries  
- **Python 3.x**  
- **Streamlit** – For building the web application  
- **NumPy** – For numerical operations  
- **Pandas** – For data manipulation  
- **Scikit-learn** – For training and saving the ML model (`insurance_pickle.pkl`)  
- **Pickle** – For model serialization  

---

## 🧮 Model Architecture  
The model is a **Linear Regression** (or any regression model you trained) that takes the following features:
- `age`
- `bmi`
- `smoker_yes` (encoded as 1 for Yes, 0 for No)

**Equation:**
\[
\text{Predicted Charges} = β_0 + β_1 \times \text{Age} + β_2 \times \text{BMI} + β_3 \times \text{Smoker\_Yes}
\]

---

## 🔧 Data Preprocessing  
1. Loaded the dataset using Pandas.  
2. Converted categorical variable `smoker` into binary columns (`smoker_yes`, `smoker_no`).  
3. Cleaned missing data (if any).  
4. Selected features: `['age', 'bmi', 'smoker_yes']`.  
5. Target variable: `charges`.  
6. Trained and saved model using:
   ```python
   import pickle
   with open('insurance_pickle.pkl', 'wb') as f:
       pickle.dump(model, f)
