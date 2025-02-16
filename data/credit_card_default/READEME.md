# 📂 Credit Card Default Dataset

## 🗂️ Folder Structure
This folder is part of the `data` directory and contains the dataset for analyzing credit card defaults.  

**Path:**  
`data/credit_card_default/default of credit card clients.xls`

**Files Included:**  
- `default of credit card clients.xls` – The raw dataset from the UCI Machine Learning Repository.  
- `README.md` – This documentation file.

---

## 🔍 **Dataset Overview**
This dataset includes information on 30,000 credit card clients in Taiwan, tracking demographic details, credit data, and repayment behavior to predict the likelihood of default in the next month.  

### 🔢 **Key Variables**
| Variable       | Description                                                  |
|-----------------|--------------------------------------------------------------|
| `LIMIT_BAL`    | Credit limit amount (in NT dollars)                           |
| `SEX`          | Gender (1 = Male, 2 = Female)                                 |
| `EDUCATION`    | Education level (1 = Grad, 2 = University, 3 = High school)   |
| `MARRIAGE`     | Marital status (1 = Married, 2 = Single, 3 = Other)           |
| `AGE`          | Age (in years)                                                |
| `PAY_0` - `PAY_6` | Repayment status over the last 6 months                     |
| `BILL_AMT1` - `BILL_AMT6` | Bill statement amounts over the last 6 months      |
| `PAY_AMT1` - `PAY_AMT6` | Payment amounts made in the last 6 months            |
| `default payment next month` | Target variable (1 = Default, 0 = No default)    |

---

## 🛠️ **How to Load This Dataset in R**
Ensure the **`readxl`** library is installed for reading `.xls` files.

```r
# Install the readxl package if needed
install.packages("readxl")

# Load necessary library
library(readxl)

# Load the dataset using relative path
data_path <- "data/credit_card_default/default of credit card clients.xls"
credit_data <- read_excel(data_path, sheet = 1)

# View the first few rows
head(credit_data)
```

## 🌐 Source
- [UCI Machine Learning Repository: Default of Credit Card Clients Dataset](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)

## 🔍 Notes:
- This folder contains only dataset-related documentation.
- The primary project documentation will reside at the project root level.
- Ensure the file path remains unchanged when running the R scripts.
- The .xls file requires the readxl library since newer libraries like openxlsx only support .xlsx files.
