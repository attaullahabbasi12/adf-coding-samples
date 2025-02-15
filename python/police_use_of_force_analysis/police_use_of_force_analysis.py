"""
---------------------------------------------------------------------------------
Title: Police Use-of-Force Analysis Across U.S. Cities
Author: Attaullah Abbasi
---------------------------------------------------------------------------------
Contact: attaullahabbasi@uchicago.edu | GitHub: attaullahabbasi12
---------------------------------------------------------------------------------

Project Overview:
This Python project analyzes police use-of-force incidents across U.S. cities, focusing on policy reforms, political leanings, and demographic patterns. It integrates datasets on fatalities, policy adoption, population statistics, and election outcomes to uncover trends and correlations.

Key Components:

1. Data Cleaning & Integration (pandas, GeoPandas):
   - Merging datasets from multiple sources (e.g., Fatal Encounters, U.S. Census) and resolving naming inconsistencies.

2. Descriptive Analysis & Visualization (Altair, Matplotlib):
   - Creating charts to illustrate incident counts by state, city, race, and age.

3. Policy Impact Analysis (pandas, Altair):
   - Evaluating policy effectiveness (e.g., chokehold bans) in reducing incidents.

4. Geospatial Analysis (GeoPandas, Matplotlib):
   - Visualizing geographic trends in use-of-force incidents.

5. Advanced Metrics (pandas, NumPy):
   - Calculating per capita incident rates and analyzing political leanings.

This code sample demonstrates core data analysis skills and the use of Python libraries for policy-relevant insights.
---------------------------------------------------------------------------------
"""

import pandas as pd
import geopandas as gpd
import altair as alt
import os
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from zipfile import ZipFile
from datetime import datetime

# Enable Altair rendering
alt.renderers.enable("default")

# GitHub base URL for raw data
github_base = "https://raw.githubusercontent.com/attaullahabbasi12/adf-coding-samples/main/data/police_use_of_force_analysis/"

# Files to download
files = [
    "fatal_encounters_dot_org.csv",
    "city_policies.csv",
    "ACSDP5Y2020.DP05-Data.csv",
    "countypres_2000-2020.csv",
    "ne_110m_admin_1_states_provinces.zip"
]

# Directory to save the files
data_dir = "/tmp/police_data"
os.makedirs(data_dir, exist_ok=True)

# Download files
for file in files:
    url = github_base + file
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(data_dir, file), "wb") as f:
            f.write(response.content)
        print(f"✅ {file} downloaded successfully.")
    else:
        raise Exception(f"❌ Failed to download {file} from GitHub.")

# Extract the shapefile
shapefile_zip = os.path.join(data_dir, "ne_110m_admin_1_states_provinces.zip")
extract_dir = os.path.join(data_dir, "us_states")
os.makedirs(extract_dir, exist_ok=True)

with ZipFile(shapefile_zip, "r") as zip_ref:
    zip_ref.extractall(extract_dir)
print("✅ Shapefile extracted successfully.")

# Locate the .shp file dynamically
shp_file = None
for root, dirs, files in os.walk(extract_dir):
    for file in files:
        if file.endswith(".shp"):
            shp_file = os.path.join(root, file)
            break

if not shp_file:
    raise FileNotFoundError("❌ Shapefile not found after extraction.")

print(f"✅ Shapefile found at: {shp_file}")

# Load datasets
df = pd.read_csv(os.path.join(data_dir, "fatal_encounters_dot_org.csv"))
us_states = gpd.read_file(shp_file)
policy_df = pd.read_csv(os.path.join(data_dir, "city_policies.csv"))
population_df = pd.read_csv(os.path.join(data_dir, "ACSDP5Y2020.DP05-Data.csv"))
election_df = pd.read_csv(os.path.join(data_dir, "countypres_2000-2020.csv"))

# Rename columns for consistency
df.rename(columns={
    "Subject's race": "Subject_race",
    "Subject's age": "Subject_age",
    "Subject's name": "Subject_name",
    "Date of injury resulting in death (month/day/year)": "incident_date"
}, inplace=True)

# Convert date column to datetime
df['incident_date'] = pd.to_datetime(df['incident_date'], errors='coerce')

# Drop unnecessary columns
drop_columns = [
    "URL of image of deceased", "Full Address", "Dispositions/Exclusions INTERNAL USE, NOT FOR ANALYSIS",
    "Symptoms of mental illness? INTERNAL USE, NOT FOR ANALYSIS", "Video", "Unique ID formula",
    "Unique identifier (redundant)", "Link to news article or photo of official document"
]
df.drop(columns=drop_columns, errors="ignore", inplace=True)

# Group incidents by state
grouped_by_state = df.groupby("Location of death (state)").size().reset_index(name="Number of Incidents")
grouped_by_state_short = grouped_by_state.sort_values(by="Number of Incidents", ascending=False).head(10)

# State-level incidents bar chart
state_chart = alt.Chart(grouped_by_state_short).mark_bar(color="blue").encode(
    x=alt.X("Location of death (state)", title="State", sort="-y", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Number of Incidents", title="Number of Incidents"),
    tooltip=["Location of death (state)", "Number of Incidents"]
).properties(title="Incidents by State", width=300, height=250).interactive()

# Group by city
grouped_by_city = df.groupby("Location of death (city)").size().reset_index(name="Number of Incidents")
grouped_by_city_short = grouped_by_city.sort_values(by="Number of Incidents", ascending=False).head(10)

# City-level incidents bar chart
city_chart = alt.Chart(grouped_by_city_short).mark_bar(color="red").encode(
    x=alt.X("Location of death (city)", title="City", sort="-y", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Number of Incidents", title="Number of Incidents"),
    tooltip=["Location of death (city)", "Number of Incidents"]
).properties(title="Incidents by City", width=300, height=250).interactive()

# Group by race
grouped_by_race = df.groupby("Subject_race").size().reset_index(name="Number of Incidents")

# Race-based incidents bar chart
race_chart = alt.Chart(grouped_by_race).mark_bar(color="green").encode(
    x=alt.X("Subject_race", title="Race", sort="-y", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Number of Incidents", title="Number of Incidents"),
    tooltip=["Subject_race", "Number of Incidents"]
).properties(title="Incidents by Race", width=300, height=250).interactive()

# Group by age
grouped_by_age = df.groupby("Subject_age").size().reset_index(name="Number of Incidents")
grouped_by_age_short = grouped_by_age.sort_values(by="Number of Incidents", ascending=False).head(20)

# Age-based incidents bar chart
age_chart = alt.Chart(grouped_by_age_short).mark_bar(color="purple").encode(
    x=alt.X("Subject_age:O", title="Age", axis=alt.Axis(labelAngle=0), sort="-y"),
    y=alt.Y("Number of Incidents", title="Number of Incidents"),
    tooltip=["Subject_age", "Number of Incidents"]
).properties(title="Incidents by Age", width=300, height=250).interactive()

# Final Combined Chart
final_chart = alt.vconcat(
    alt.hconcat(state_chart, city_chart),
    alt.hconcat(race_chart, age_chart)
).resolve_scale(y="independent")

final_chart.show()

# Prepare map visualization with incidents normalized by population
us_states = us_states[us_states["admin"] == "United States of America"]

# Convert state abbreviations to full names for merging
grouped_by_state["Location of death (state)"] = grouped_by_state["Location of death (state)"].replace({
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado",
    "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota",
    "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
    "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
    "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island",
    "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"
})

# Merge data with geospatial information
grouped_by_state.rename(columns={"Location of death (state)": "state"}, inplace=True)
merged = us_states.merge(grouped_by_state, left_on="name", right_on="state", how="left").fillna(0)

# Plot the normalized map (incidents per capita)
fig, ax = plt.subplots(figsize=(15, 10))
merged['incidents_per_capita'] = merged["Number of Incidents"] / (population_df["DP05_0001E"].sum() / len(population_df))
merged.plot(column="incidents_per_capita", ax=ax, legend=True, cmap="YlGnBu", edgecolor="black")
ax.set_title("Police Use-of-Force Incidents Per Capita by State")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Time series analysis (with 2100 fix)
df['year'] = df['incident_date'].dt.year
time_series = df.groupby('year').size().reset_index(name='Number of Incidents')

# Filter out future years like 2100
time_series = time_series[time_series['year'] <= datetime.now().year]

time_chart = alt.Chart(time_series).mark_line(point=True).encode(
    x=alt.X("year:O", title="Year"),
    y=alt.Y("Number of Incidents", title="Number of Incidents"),
    tooltip=["year", "Number of Incidents"]
).properties(title="Police Use-of-Force Incidents Over Time", width=600, height=400).interactive()

time_chart.show()

# Policy Impact Analysis
policy_impact = policy_df.melt(id_vars=["City", "State"], var_name="Policy", value_name="Implemented")
policy_impact_summary = policy_impact.groupby("Policy")["Implemented"].mean().reset_index()

policy_chart = alt.Chart(policy_impact_summary).mark_bar(color="teal").encode(
    x=alt.X("Policy", title="Policy", sort="-y", axis=alt.Axis(labelAngle=-45)),
    y=alt.Y("Implemented", title="Proportion Implemented"),
    tooltip=["Policy", "Implemented"]
).properties(title="Policy Implementation Analysis", width=600, height=400).interactive()

policy_chart.show()
