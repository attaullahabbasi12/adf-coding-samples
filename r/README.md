# 📊 Credit Card Default Analysis

### Author: Attaullah Abbasi  
**Repository:** [GitHub - ADF Coding Samples](https://github.com/attaullahabbasi12/adf-coding-samples)  

---

## 🚀 Project Overview

This project analyzes and models the likelihood of default among credit card clients using the **UCI Credit Card Default Dataset**. The primary objective is to predict default risk based on clients' historical payment behavior. The analysis employs data processing techniques, feature engineering, and machine learning to build a predictive model.

The code is optimized for clarity, reproducibility, and efficiency, ensuring it runs in approximately **1 minute** to facilitate smooth review while demonstrating core data science practices.

---

## 📁 Project Structure

├── data
│   └── credit_card_default
│       └── default_of_credit_card_clients.xls
├── R
│   └── credit_card_default_analysis.R
├── Python
│   └── sample_python_scripts/
├── Stata
│   └── sample_stata_scripts/
└── README.md

---

## 🔍 Methodology Overview

1. **Data Acquisition**: Dataset downloaded from GitHub if missing locally.  
2. **Data Cleaning**: Missing values handled; appropriate data types assigned.  
3. **Feature Engineering**: New features created to capture important trends (e.g., `age_limit_interaction`).  
4. **Class Imbalance Correction**: ROSE (Random Over-Sampling Examples) applied for balanced classes.  
5. **Model Training**: Random Forest model trained with hyperparameter tuning.  
6. **Evaluation**: Model evaluated using accuracy, ROC-AUC, and feature importance analysis.  
7. **Visualization**: Plots for exploratory analysis and feature importance included.

---

## 🛠️ Tools & Libraries

The project utilizes the following R libraries:

- `tidyverse` – Data manipulation and visualization  
- `readxl` – Excel file reading  
- `ggplot2` – Data visualization  
- `caret` – Data partitioning and model evaluation  
- `randomForest` – Model training  
- `ROSE` – Class imbalance correction  
- `pROC` – ROC curve analysis  

---

## 💾 Dataset Description

**Dataset Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)  

The dataset contains payment data for **30,000 clients** with **24 features** including:  

- **Demographic Info**: Gender, Education, Marriage status, Age  
- **Credit Info**: Credit limit, bill amounts, payment amounts  
- **Behavioral Patterns**: Past payment statuses and repayment behavior  
- **Target Variable**: `DEFAULT_NEXT_MONTH` (0 = No default, 1 = Default)  

---

## 📊 Key Insights

- **Younger clients** exhibit higher default rates.  
- **Repayment behavior** and **credit limit** are the most influential predictors.  
- Model achieved:  
  - **Accuracy:** 86%  
  - **ROC-AUC Score:** 0.86  

### 🔍 Feature Importance Visualization

The plot below highlights the top predictors identified by the Random Forest model:

![Feature Importance Plot](feature_importance.png)

---

## ⚙️ Model Optimization Strategy

The model was optimized with the following considerations:  

- **Lightweight Hyperparameter Tuning:** Limited tuning space to reduce runtime.  
- **Reduced Tree Count:** 100 trees instead of 500+ for efficiency.  
- **Balanced Training Dataset:** ROSE applied to address the dataset's inherent imbalance.  

### **Runtime:** ~1 Minute  

**Intentional Decision:** The script is designed to execute within approximately **1 minute**.  
*Purpose:* Showcase coding principles without long execution times for reviewers.

---

## 🧩 How to Run the Code

1. Clone the repository:

```bash
git clone https://github.com/attaullahabbasi12/adf-coding-samples.git
cd adf-coding-samples
```

2. Open the R/credit_card_default_analysis.R file in RStudio or a similar IDE.

3. Run the script:
```r
source("R/credit_card_default_analysis.R", encoding = "UTF-8")
```

4. The results and plots will be displayed in the console and graphics window.


## 🧠 Insights for Reviewers

- **Code Style:** Comments are written as though addressing a future reviewer/employer.  
- **Performance Consideration:** Runtime limited to ensure accessible, timely review.  
- **Modularity:** Feature engineering and model training are logically separated for clarity.  

### 🔍 Next Steps (Potential Improvements)

- Implement SHAP values for improved model explainability.  
- Experiment with gradient boosting models to improve predictive performance.  

---

💡 *This project forms part of a larger portfolio that demonstrates skills across R, Python, SQL, and Stata.*  

🔗 **GitHub Repository:** [ADF Coding Samples](https://github.com/attaullahabbasi12/adf-coding-samples)  

---

### 👤 **Author:**  
**Name:** Attaullah Abbasi  
**Contact:** [attaullahabbasi@uchicago.edu](mailto:attaullahabbasi@uchicago.edu)  
**GitHub:** [attaullahabbasi12](https://github.com/attaullahabbasi12)  

