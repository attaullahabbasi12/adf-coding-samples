# Police Use-of-Force Analysis Across U.S. Cities

### Overview
This project analyzes police use-of-force incidents across U.S. cities, focusing on the relationship between policy reforms, political leanings, and demographic patterns. The analysis uses datasets on police fatalities, policy adoption, population statistics, and election results to identify key trends.

### Key Analysis Components
- **Data Cleaning & Integration:** Merging datasets from multiple sources and resolving naming inconsistencies.
- **Descriptive Analysis & Visualization:** Charting incidents by state, city, race, and age.
- **Policy Impact Analysis:** Evaluating the effectiveness of reforms like chokehold bans.
- **Geospatial Analysis:** Mapping incident distributions using GIS.
- **Advanced Metrics:** Calculating per capita incident rates and examining political correlations.

### Instructions to Run the Code

1. **Clone the Repository:**  
   `git clone https://github.com/attaullahabbasi12/adf-coding-samples.git`  
   `cd adf-coding-samples/python`

2. **Install Required Libraries:**  
   `pip install pandas geopandas altair matplotlib numpy requests`

3. **Run the Analysis Script:**  
   `python police_use_of_force_analysis.py`

4. **Expected Outputs:**  
    - Bar charts of incidents by state, city, race, and age.  
    - A geographic heatmap of incidents per capita by state.  
    - A time series chart of incidents over time.  
    - A summary chart of city-level policy adoption.

### Data Sources
- Fatal Encounters Dataset  
- U.S. Census Data (ACS 5-Year Estimates)  
- U.S. Elections Data (2000-2020)
