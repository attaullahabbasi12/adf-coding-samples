# README: Education Subsidy Analysis Data

## 📖 Project Overview
This folder contains datasets used for the analysis of the impact of in-kind educational subsidies on school retention, teen pregnancy, and early marriage. The analysis evaluates a randomized controlled trial (RCT) conducted between 2010 and 2012 to assess the program's outcomes.

## 📂 Folder Structure
- **schools.csv**: Contains baseline school-level data, including teacher characteristics, student demographics, and school infrastructure.
- **student_follow_ups.csv**: Contains follow-up data for students, tracking primary and secondary outcomes such as school dropout, teen pregnancy, marriage, and childbearing.

## 🔍 Data Description

### 📘 schools.csv
- `school_id`: Unique identifier for each school.
- `av_teacher_age`: Average age of teachers.
- `av_student_score`: Average test scores of students.
- `n_latrines`: Number of latrines available in the school.

### 📙 student_follow_ups.csv
- `student_id`: Unique identifier for each student.
- `school_id`: Identifier linking the student to their school.
- `dropout`: Binary variable (1 = Dropped out, 0 = Continued).
- `pregnant`: Binary variable indicating teen pregnancy.
- `married`: Binary variable indicating if the student married during the study period.
- `children`: Number of children born to the student.
- `died`: Binary variable indicating mortality.

## ⚙️ Notes
- Missing values are represented as `-99` in the raw data but will be recoded as missing (`.`) in the analysis.
- The datasets will be used in conjunction with a Stata script located in the `stata` folder for analysis.

## 🌐 Data Source
The datasets were originally collected as part of a government-sponsored evaluation of the subsidy program.

## 🛠️ Usage
These datasets are utilized in the Machine Learning for Public Policy project to analyze how educational subsidies impact school retention and social outcomes.

Key analyses include:
- Data cleaning and variable creation
- Visualizing dropout trends
- Regression modeling with control variables

## ⚠️ Important Notes
Data should be handled with care as it includes demographic information used for academic research.

The results from this analysis are intended for educational purposes as part of a class project but may offer broader insights for policy discussions.

**👤 Author:** Attaullah Abbasi  
**📧 Contact:** attaullahabbasi@uchicago.edu
