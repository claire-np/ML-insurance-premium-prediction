# Predicting Medical Insurance Costs  
*A practical machine learning workflow for understanding what drives healthcare premiums.*

<p>
  <img src="https://img.shields.io/badge/last%20update-today-brightgreen" />
  <img src="https://img.shields.io/badge/python-3.10-blue" />
  <img src="https://img.shields.io/badge/notebook-Jupyter-orange" />
  <img src="https://img.shields.io/badge/status-Completed-brightgreen" />
</p>

Medical insurance pricing is often viewed as a black box. This project aims to open that box — using data to explain why certain individuals face higher medical costs than others, and how insurers can translate these insights into more effective pricing and wellness strategies.

This repository is part of my data science portfolio. Before this project, I focused on HR Attrition modeling (classification). Here, I shift into regression, where the challenge is not predicting *who*, but predicting *how much* — introducing new modeling assumptions, evaluation metrics, and business implications.

---

## Project Overview

The goal of this project is twofold:

1. **Predict** individual medical insurance charges using demographic and lifestyle factors.  
2. **Explain** the cost structure by quantifying how strongly each factor contributes to healthcare spending.

To achieve this, I built a fully end-to-end ML workflow:

- Exploratory data analysis (EDA)  
- Feature engineering, including interaction terms  
- Log transformation to correct the skewed cost distribution
- Gradient Boosting modeling with hyperparameter tuning  
- SHAP analysis for model transparency  
- Business framing around insurance pricing and wellness incentives  

This mirrors the analytic workflow used inside health insurers and actuarial teams.

---

## Final Model Performance

After evaluating several baseline models, the **tuned Gradient Boosting Regressor** achieved the best balance of accuracy and interpretability.

**Model Summary**
- **R²:** 0.864  
- **MAE:** \$1,970  
- **Algorithm:** Gradient Boosting (with RandomizedSearchCV)  
- **Key engineered feature:** `bmi_smoker` (BMI × Smoking interaction)

The model captures underlying cost patterns well while maintaining stability and generalization.

---

## What Drives Medical Costs?

Three signals consistently stand out across the analysis.

### 1. **Age — the most reliable predictor**
Healthcare spending increases steadily with age. SHAP shows a near-linear rise in contribution, matching well-known actuarial and clinical patterns.

### 2. **Smoking × BMI — a powerful interaction effect**
This was the most economically meaningful discovery.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6ef3032d-c26b-4e58-bfb3-fe585055ef0a" width="650" alt="BMI vs Charges by Smoking Status">
</p>

Smokers with high BMI incur **disproportionately higher** medical costs than non-smokers at the same BMI level. Engineering this interaction produced a measurable improvement in predictive performance.

This non-linear pattern is exactly the effect later captured by the engineered `bmi_smoker` feature and validated through SHAP interaction values.

### 3. **Lifestyle & demographic variables — secondary but useful**
- Number of children  
- Sex  
- Region  

These support localized pricing adjustments but do not dominate the risk profile.

---

## SHAP: Ensuring Transparency and Fairness

Insurance pricing requires models that are not only accurate but explainable.

SHAP analysis helped validate:

- The model’s behavior aligns with real medical risk patterns  
- High-risk groups are identified for legitimate reasons  
- Demographic variables contribute in a stable, non-biased way  
- Actuaries can trust the model’s internal logic  

SHAP rankings were also stable across random seeds, increasing confidence that the model is capturing **true cost structure**, not noise — crucial for pricing decisions and regulatory review.

**SHAP Feature Importance Illustration:**

<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/e1715f5e-7b7d-4ed9-b23b-b80836772fcc" 
    alt="SHAP Feature Importance Illustration"
    width="650"
  >
</p>

---

## Business Perspective: Beyond Prediction

Predicting current medical costs is valuable, but the model’s real potential lies in shaping the **future**.

This work forms the analytical foundation for **dynamic wellness-based pricing**, where premiums adjust based on measurable health improvements.

### Questions this model enables:

- *If a high-risk individual quits smoking for a year, how much does their expected cost drop?*  
- *What is the financial return of offering a 5% discount for every 2-point BMI reduction?*  
- *How can insurers nudge healthier behavior while managing long-term portfolio risk?*

These questions transform the model from a predictive tool into a **decision-support engine** for product design, underwriting, and risk management.

---

## Source Acknowledgment

This repository builds upon the [Medical Insurance Premium Prediction with Machine Learning (Coursera)](https://www.coursera.org/projects/medical-insurance-premium-prediction-with-machine-learning), with original datasets and project framework utilized under Coursera’s Educational Use Policy.

I took full ownership of advancing this project from a course-level exercise to a **production-grade regression analysis** focused on **statistical validity** and **business applicability**. Key contributions include:
- Reframing the modeling pipeline to address real-world data distribution issues.  
- Applying a logarithmic transformation to the target variable `charges` to correct skewness and satisfy regression assumptions.  
- Designing and implementing a robust evaluation framework with extended metrics (R², MAE, RMSE) for deeper model diagnostics.  
- Interpreting results through the perspective of **budgeting, cost control, and risk management**, aligning statistical insights with business decision-making.

> *This repository reflects an independently led, methodologically enhanced version of the original Coursera project, maintained solely for educational and portfolio demonstration purposes.*
