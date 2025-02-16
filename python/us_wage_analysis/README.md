# 📊 U.S. Wage Analysis Using Machine Learning

This project analyzes wage patterns across the United States, focusing on the relationship between education, race, gender, and wages. The analysis employs data manipulation, visualization, and machine learning techniques to uncover wage disparities.

> 🎓 *This project was originally completed as part of the Machine Learning for Public Policy course at the University of Chicago, but the code and methodology demonstrate core Python skills applicable to real-world data analysis tasks.*

---

## 🛠️ **Key Components**

- 📦 **Data Cleaning & Transformation:** `pandas`, `numpy`  
- 📈 **Descriptive & Visual Analysis:** `matplotlib`, `seaborn`  
- 🔍 **Regression Modeling:** `statsmodels`  
- 🔧 **Feature Engineering & Interaction Terms:** Python  
- 🌱 **Spline Regression:** `patsy`
 
---

## 📂 **Project Structure**

```plaintext
adf-coding-samples/
    ├── python/                         # Main folder for Python projects
    │    ├── us_wage_analysis/          # U.S. wage analysis project
    │    │    ├── us_wage_analysis.py   # Main Python script
    │    │    └── README.md             # Documentation
    │    └── police_use_of_force_analysis/  # Police use-of-force analysis project
    │         ├── police_use_of_force_analysis.py
    │         └── README.md
    └── data/
         └── us_wage_analysis/          # Data specific to wage analysis
             ├── usa_00001.csv          # Census wage data
             └── Crosswalk.csv          # Education code crosswalk
```


## 🚀 **How to Run the Analysis**

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/attaullahabbasi12/adf-coding-samples.git
    cd adf-coding-samples/python/us_wage_analysis
    ```

2. **Install the Required Libraries:**

    ```bash
    pip install pandas numpy matplotlib seaborn statsmodels patsy
    ```

3. **Run the Script:**

    ```bash
    python us_wage_analysis.py
    ```

---

## 🧠 **Project Insights**

This analysis explores how demographic factors, particularly education, gender, and race, influence wage outcomes. Key findings and methods include:

- 📊 **Linear & Spline Regression:** To capture both simple and non-linear wage-age relationships.  
- 🏫 **Education Impact:** Investigating the wage premium for high school and college diplomas.  
- ⚖️ **Gender & Race Disparities:** Analyzing income differences across demographic groups.  
- 📈 **Predictive Modeling:** Using feature engineering and interaction terms to improve wage predictions.

---

## 📖 **Data Sources**

- 🏛️ **U.S. Census Data:** American Community Survey (ACS)  
- 🔢 **Education Code Crosswalk:** Custom crosswalk provided for the course assignment  

---

## 🧩 **Reproducibility**

This project is designed for full reproducibility. All datasets are downloaded directly from the repository when the script is executed. Ensure you have an active internet connection when running the code for the first time.

---

## 💼 **About the Author**

- **👤 Name:** Attaullah Abbasi  
- **🏫 Affiliation:** University of Chicago, Harris School of Public Policy  
- **📧 Email:** attaullahabbasi@uchicago.edu  
- **🔗 GitHub:** [attaullahabbasi12](https://github.com/attaullahabbasi12)  

---

*This project showcases core Python skills relevant for roles in data analysis, machine learning, and public policy research. Feedback and collaboration opportunities are always welcome!* 🚀
