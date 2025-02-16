# 📊 Education Subsidy Analysis for Policy Evaluation

## 🛠️ Overview
This project analyzes the impact of an education subsidy on student outcomes using real-world school and student-level data. The analysis employs data cleaning, transformation, regression modeling with fixed effects and clustered standard errors, and insightful visualizations to support evidence-based policy evaluation.

## 📂 Repository Structure
- **`education_subsidy_analysis.do`**: Main Stata script performing data import, cleaning, analysis, and visualization (located in the `stata` folder).
- **`README.md`**: Project-specific documentation (also in the `stata` folder).
- **`/data/education_subsidy_analysis`**: Folder containing datasets specific to this analysis.

## 🧠 Analysis Objective
The primary goal of this analysis is to understand the potential effects of an educational subsidy on key student outcomes such as dropout, pregnancy, marriage, and childbearing rates.

## ⚙️ Methodology
1. **Data Cleaning**: Handles missing values and removes duplicates.
2. **Data Integration**: Merges school and student datasets.
3. **Regression Analysis**: Runs OLS regressions with clustered SEs and district fixed effects.
4. **Visualization**: Creates intuitive bar charts displaying outcome differences between treatment and control groups.

## 📊 Data Sources
The data used in this project is imported directly from a public GitHub repository:
- School-level data: [schools.csv](https://raw.githubusercontent.com/attaullahabbasi12/adf-coding-samples/main/data/education_subsidy_analysis/schools.csv)
- Student follow-up data: [student_follow_ups.csv](https://raw.githubusercontent.com/attaullahabbasi12/adf-coding-samples/main/data/education_subsidy_analysis/student_follow_ups.csv)

## 🚀 Running the Analysis
1. Open `Stata` and set the working directory to the project folder.
2. Run the following command:
   ```
   do education_subsidy_analysis.do
   ```
3. The script will:
    - Import and clean the data.
    - Run regressions with clustered standard errors.
    - Generate a bar chart comparing the treatment and control groups.

## 🧾 Key Insights
- The treatment group shows reduced rates of dropouts, pregnancies, and marriages, though results are not statistically significant.
- The findings indicate potential policy impact but suggest the need for further investigation with larger datasets.

## 🛠️ Next Steps
- Explore non-linear models for binary outcomes.
- Investigate heterogeneous effects through additional interaction terms.
- Validate results with supplementary data sources.

## 👤 Author
- Name: Attaullah Abbasi
- Contact: attaullahabbasi@uchicago.edu
- GitHub: @attaullahabbasi12



