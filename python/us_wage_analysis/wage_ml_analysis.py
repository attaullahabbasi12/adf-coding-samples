# 📊 U.S. Wage Analysis Using Machine Learning

# This script analyzes wage patterns across the United States using data from the American Community Survey (ACS). 
# It examines relationships between education, age, gender, race, and wages to provide insights for policy decisions.

# ---
# 🧠 Context & Data Collection
# - Source: [IPUMS USA](https://usa.ipums.org/usa/)
# - Sample: 2023 ACS (Employed individuals aged 18 to 65 only)
# - Key Variables: Age, gender, race, marital status, education, income, employment status.

# ---
# 🔍 Tasks Performed:
# 1. Data Cleaning & Feature Engineering
# 2. Descriptive Statistics Generation
# 3. Visualization of Wage-Education Relationship
# 4. Regression Analysis (OLS & Spline Models)
# 5. Prediction of Hypothetical Wages

# 🚀 Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from patsy import dmatrix

# 📥 Step 2: Load the Data from GitHub
data_path = "https://raw.githubusercontent.com/attaullahabbasi12/adf-coding-samples/main/data/us_wage_analysis/usa_00001.csv"
crosswalk_path = "https://raw.githubusercontent.com/attaullahabbasi12/adf-coding-samples/main/data/us_wage_analysis/Crosswalk.csv"

try:
    df = pd.read_csv(data_path)
    crosswalk = pd.read_csv(crosswalk_path)
except Exception as e:
    print(f"⚠️ Failed to load data: {e}")
    exit()

# 🛠️ Step 3: Merge Crosswalk to Create Continuous Education Variable
df = df.merge(crosswalk, left_on="EDUCD", right_on="educd", how="left")
df.drop(columns=["educd"], inplace=True)

# 📊 Step 4: Create Dummy Variables
dummy_vars = {
    "hsdip": lambda x: x["educdc"] == 12,
    "coldip": lambda x: x["educdc"] >= 16,
    "white": lambda x: x["RACE"] == 1,
    "black": lambda x: x["RACE"] == 2,
    "hispanic": lambda x: x["HISPAN"] > 0,
    "married": lambda x: x["MARST"] == 1,
    "female": lambda x: x["SEX"] == 2,
    "vet": lambda x: x["VETSTAT"] == 2
}

for col, func in dummy_vars.items():
    df[col] = func(df).astype(int)

# 🔄 Step 5: Generate Interaction Terms
df["hsdip_educdc"] = df["hsdip"] * df["educdc"]
df["coldip_educdc"] = df["coldip"] * df["educdc"]

# 🧠 Step 6: Create Derived Variables
df["age2"] = df["AGE"] ** 2
df = df[df["INCWAGE"] > 0]
df["lnincwage"] = np.log(df["INCWAGE"])

# 📊 Step 7: Generate Descriptive Statistics
summary_stats = df.describe().round(2)
print(summary_stats)

# 📈 Step 8: Visualize Wages vs Education
plt.figure(figsize=(10, 6))
sns.regplot(x="educdc", y="lnincwage", data=df, scatter_kws={'alpha':0.4}, line_kws={"color": "red"})
plt.xlabel("Years of Education")
plt.ylabel("Log of Wages")
plt.title("Log of Wages vs Education")
plt.text(16, df["lnincwage"].mean(), "College graduates", color="green")
plt.text(12, df["lnincwage"].mean(), "High school graduates", color="orange")
plt.xlim(df["educdc"].min(), df["educdc"].max())
plt.ylim(df["lnincwage"].min(), df["lnincwage"].max())
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()


# 🧪 Step 9: Run Baseline OLS Model
X = df[["educdc", "female", "AGE", "age2", "white", "black", "hispanic", "married", "NCHILD", "vet"]]
y = df["lnincwage"]
X = sm.add_constant(X)
baseline_model = sm.OLS(y, X).fit()
print(baseline_model.summary())

# 📊 Step 10: Visualize Education-Specific Regression Lines
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["educdc"], y=df["lnincwage"], hue=df["hsdip"] + 2 * df["coldip"], alpha=0.3)
for group, color in [("hsdip", "orange"), ("coldip", "green")]:
    subset = df[df[group] == 1]
    if len(subset) > 0:
        X_subset = sm.add_constant(subset["educdc"])
        model = sm.OLS(subset["lnincwage"], X_subset).fit()
        educ_range = np.linspace(subset["educdc"].min(), subset["educdc"].max(), 100)
        plt.plot(educ_range, model.predict(sm.add_constant(educ_range)), color=color, linewidth=2)
plt.title("Log Wages vs Education by Education Level")
plt.xlabel("Years of Education")
plt.ylabel("Log of Wage")
plt.show()

# 📊 Step 11: Interaction Model
X_int = df[["educdc", "hsdip", "coldip", "female", "AGE", "age2", "white", "black", "hispanic", 
            "married", "NCHILD", "vet", "hsdip_educdc", "coldip_educdc"]]
X_int = sm.add_constant(X_int)
interaction_model = sm.OLS(y, X_int).fit()
print(interaction_model.summary())

# 🔍 Step 12: Predict Wages for Hypothetical Individuals
hs_grad = pd.DataFrame({
    "const": [1], "educdc": [12], "hsdip": [1], "coldip": [0], "female": [1],
    "AGE": [22], "age2": [22**2], "white": [0], "black": [0], "hispanic": [0], 
    "married": [0], "NCHILD": [0], "vet": [0], "hsdip_educdc": [144], "coldip_educdc": [0]
})
college_grad = pd.DataFrame({
    "const": [1], "educdc": [16], "hsdip": [0], "coldip": [1], "female": [1],
    "AGE": [22], "age2": [22**2], "white": [0], "black": [0], "hispanic": [0], 
    "married": [0], "NCHILD": [0], "vet": [0], "hsdip_educdc": [0], "coldip_educdc": [256]
})
predicted_wages = interaction_model.predict(pd.concat([hs_grad, college_grad]))
print(f"Predicted wage for HS graduate: ${np.exp(predicted_wages.iloc[0]):.2f}")
print(f"Predicted wage for College graduate: ${np.exp(predicted_wages.iloc[1]):.2f}")

# 🎯 Step 14: Predict Age-Specific Wages with Dynamic Input
def predict_wage(age, model, df, educdc=16, female=1, white=0, black=0, hispanic=0, married=0, nchild=0, vet=0):
    # Create a test dataframe with default values
    test_data = pd.DataFrame({param: 0 for param in model.params.index}, index=[0])

    # Populate known features
    test_data.loc[0, :] = {
        "educdc": educdc,
        "hsdip": int(educdc == 12),
        "coldip": int(educdc >= 16),
        "female": female,
        "white": white,
        "black": black,
        "hispanic": hispanic,
        "married": married,
        "NCHILD": nchild,
        "vet": vet,
        "hsdip_educdc": int(educdc == 12) * educdc,
        "coldip_educdc": int(educdc >= 16) * educdc
    }

    # Set age and age squared
    test_data["AGE"] = age
    test_data["age2"] = age**2

    # Generate spline basis with df 
    spline_input = pd.DataFrame({"AGE": [age]})
    spline_formula = "bs(AGE, df=6, degree=3, include_intercept=True)"

    try:
        # Generate the spline basis
        spline_features = dmatrix(spline_formula, data=spline_input, return_type='dataframe')

        # Rename 'Intercept' to 'const' if present
        if 'Intercept' in spline_features.columns:
            spline_features.rename(columns={"Intercept": "const"}, inplace=True)

        # Add spline features to test dataframe
        for col in spline_features.columns:
            if col in test_data.columns:
                test_data[col] = spline_features[col].values[0]

        # Add constant if missing
        if 'const' not in test_data.columns:
            test_data.insert(0, 'const', 1)

        # Debugging step: print test_data to check structure
        if model.predict(test_data).isna().any():
            print("⚠️ Prediction resulted in NaN")


        # Predict log wage and convert to wage
        pred_log_wage = model.predict(test_data)
        if pred_log_wage.isna().any():
            raise ValueError("Prediction resulted in NaN")
        predicted_wage = round(np.exp(pred_log_wage.iloc[0]), 2)
        return predicted_wage

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None

# Predict wages for ages 18 and 50 with dynamic input
wage_at_18 = predict_wage(18, interaction_model, df)
wage_at_50 = predict_wage(50, interaction_model, df)

print(f"Predicted wage at age 18: ${wage_at_18}")
print(f"Predicted wage at age 50: ${wage_at_50}")
