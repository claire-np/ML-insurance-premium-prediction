# Predicting Medical Insurance Costs
*A regression-based approach to understanding and explaining what drives medical insurance premiums.*

**Project Overview:**

This project is the second entry in my data science portfolio, building on my previous HR Attrition analysis. It represents a clear progression — moving from classification (predicting who will leave) to regression (predicting how much something will cost).

The objective was to design a complete, end-to-end machine learning workflow that predicts individual medical insurance costs based on personal and lifestyle factors. Beyond prediction, the project focuses on explainability and business relevance — uncovering what drives these costs and how insurers could act on those insights.

**Results:**
- Best Model: Tuned Gradient Boosting Regressor
- Performance: Mean Absolute Error = $1,970 | R² = 0.864
- Key Drivers: Age, Smoking Status, and BMI
- Critical Finding: The cost impact of high BMI multiplies dramatically for smokers, revealing a strong interaction effect that boosted model accuracy.

The final model doesn’t just predict — it explains.
It identifies age as the most influential feature, followed closely by smoking behavior and body mass index, giving insurers data-driven clarity on the cost structure behind premiums.

<img width="874" height="525" alt="image" src="https://github.com/user-attachments/assets/49099c60-9307-458a-b761-af5e8221ac2c" />




**A deeper business question for the future**

While the model successfully predicts current medical costs, its real potential lies in shaping future outcomes. The next step is to move from prediction to prescription — turning insights into business action.

*How can we design a dynamic wellness program that offers personalized premium discounts for measurable health improvements?*

*For instance:*
- *What would be the financial impact of giving a 15% premium reduction to a high-risk individual who quits smoking for a year?*
- *How much could we further reduce costs by offering 5% off for every 2-point drop in BMI?*

Answering these questions would elevate the project from a predictive model to a strategic decision-support tool — one that aligns customer wellness incentives with long-term cost reduction and healthier portfolios.
