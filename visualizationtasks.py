"""
TD2310 - Introduction to Data Visualization
Demonstration of 11 Visualization Tasks

Dataset:
    DataTypesandVisualizationDummyDataset.xlsx

Sheet:
    Student Dataset

Required packages:
    pip install pandas matplotlib openpyxl

This script demonstrates:
1. Comparison
2. Ranking
3. Distribution
4. Composition
5. Relationship
6. Trend
7. Deviation
8. Location
9. Univariate analysis
10. Bivariate analysis
11. Multivariate analysis
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. FILE SETTINGS
# ============================================================

# Keep the Excel file in the same folder as this Python script.
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "DataTypesandVisualizationDummyDataset.xlsx"

# Folder where all generated charts will be saved.
OUTPUT_DIR = BASE_DIR / "TD2310_Visualization_Output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD THE DATASET
# ============================================================

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Student Dataset"
)

# Convert Month into a real date variable.
df["Month"] = pd.to_datetime(df["Month"])

print("Dataset loaded successfully.")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))


# ============================================================
# HELPER FUNCTION
# ============================================================

def save_chart(filename):
    """Save the current chart and then close it."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=200, bbox_inches="tight")
    plt.show()
    plt.close()


# ============================================================
# TASK 1: COMPARISON
# Question:
# Which programme has the highest average quiz score?
#
# Suitable visual:
# Bar chart
# ============================================================

programme_quiz = (
    df.groupby("Programme")["Quiz_Score"]
      .mean()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
programme_quiz.plot(kind="bar")

plt.title("1. Comparison: Average Quiz Score by Programme")
plt.xlabel("Programme")
plt.ylabel("Average Quiz Score")
plt.xticks(rotation=0)

save_chart("01_comparison_average_quiz_by_programme.png")


# ============================================================
# TASK 2: RANKING
# Question:
# Rank programmes by average attendance.
#
# Suitable visual:
# Ordered horizontal bar chart
# ============================================================

programme_attendance = (
    df.groupby("Programme")["Attendance_Rate"]
      .mean()
      .sort_values(ascending=True)
)

plt.figure(figsize=(8, 5))
programme_attendance.plot(kind="barh")

plt.title("2. Ranking: Programmes by Average Attendance")
plt.xlabel("Average Attendance Rate (%)")
plt.ylabel("Programme")

save_chart("02_ranking_average_attendance.png")


# ============================================================
# TASK 3: DISTRIBUTION
# Question:
# How are weekly study hours distributed?
#
# Suitable visual:
# Histogram
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Weekly_Study_Hours"],
    bins=8,
    edgecolor="black"
)

plt.title("3. Distribution: Weekly Study Hours")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Frequency")

save_chart("03_distribution_weekly_study_hours.png")


# ============================================================
# TASK 4: COMPOSITION
# Question:
# What proportion of observations belongs to each programme?
#
# Suitable visual:
# Pie chart
# ============================================================

programme_counts = df["Programme"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    programme_counts.values,
    labels=programme_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("4. Composition: Observations by Programme")

save_chart("04_composition_programme_share.png")


# ============================================================
# TASK 5: RELATIONSHIP
# Question:
# Is study time associated with quiz score?
#
# Suitable visual:
# Scatter plot
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Weekly_Study_Hours"],
    df["Quiz_Score"]
)

plt.title("5. Relationship: Study Hours vs Quiz Score")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Quiz Score")

save_chart("05_relationship_study_hours_vs_quiz.png")


# ============================================================
# TASK 6: TREND
# Question:
# How does average quiz score change from January to April?
#
# Suitable visual:
# Line chart
# ============================================================

monthly_quiz = (
    df.groupby("Month")["Quiz_Score"]
      .mean()
      .sort_index()
)

plt.figure(figsize=(8, 5))

plt.plot(
    monthly_quiz.index,
    monthly_quiz.values,
    marker="o"
)

plt.title("6. Trend: Average Quiz Score Over Time")
plt.xlabel("Month")
plt.ylabel("Average Quiz Score")
plt.xticks(
    monthly_quiz.index,
    [d.strftime("%b %Y") for d in monthly_quiz.index]
)
plt.grid(axis="y", alpha=0.3)

save_chart("06_trend_average_quiz_over_time.png")


# ============================================================
# TASK 7: DEVIATION
# Question:
# Which students are above or below the target quiz score of 75?
#
# Suitable visual:
# Deviation bar chart
# ============================================================

TARGET_SCORE = 75

student_average = (
    df.groupby("Student_Name")["Quiz_Score"]
      .mean()
)

deviation = (student_average - TARGET_SCORE).sort_values()

plt.figure(figsize=(9, 6))

plt.barh(
    deviation.index,
    deviation.values
)

plt.axvline(0, linewidth=1)

plt.title("7. Deviation: Average Quiz Score Relative to Target 75")
plt.xlabel("Difference from Target Score")
plt.ylabel("Student")

save_chart("07_deviation_from_target_quiz_score.png")


# ============================================================
# TASK 8: LOCATION
# Question:
# How do average quiz scores differ across districts?
#
# Suitable visual:
# Simple location scatter plot using longitude and latitude
#
# Note:
# This is a simple geographic-style plot, not a full map.
# ============================================================

district_summary = (
    df.groupby("District")
      .agg(
          Latitude=("Latitude", "mean"),
          Longitude=("Longitude", "mean"),
          Average_Quiz=("Quiz_Score", "mean")
      )
      .reset_index()
)

plt.figure(figsize=(8, 6))

plt.scatter(
    district_summary["Longitude"],
    district_summary["Latitude"],
    s=district_summary["Average_Quiz"] * 4
)

for _, row in district_summary.iterrows():
    plt.text(
        row["Longitude"] + 0.01,
        row["Latitude"] + 0.01,
        f'{row["District"]}\n{row["Average_Quiz"]:.1f}'
    )

plt.title("8. Location: Average Quiz Score by District")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

save_chart("08_location_average_quiz_by_district.png")


# ============================================================
# TASK 9: UNIVARIATE ANALYSIS
# Question:
# What is the distribution of satisfaction levels?
#
# One variable:
# Satisfaction_Level
#
# Suitable visual:
# Bar chart
# ============================================================

satisfaction_counts = (
    df["Satisfaction_Level"]
      .value_counts()
      .sort_index()
)

plt.figure(figsize=(8, 5))

satisfaction_counts.plot(kind="bar")

plt.title("9. Univariate: Distribution of Satisfaction Levels")
plt.xlabel("Satisfaction Level")
plt.ylabel("Number of Observations")
plt.xticks(rotation=0)

save_chart("09_univariate_satisfaction_levels.png")


# ============================================================
# TASK 10: BIVARIATE ANALYSIS
# Question:
# How does attendance relate to quiz score?
#
# Two variables:
# Attendance_Rate and Quiz_Score
#
# Suitable visual:
# Scatter plot
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance_Rate"],
    df["Quiz_Score"]
)

plt.title("10. Bivariate: Attendance Rate vs Quiz Score")
plt.xlabel("Attendance Rate (%)")
plt.ylabel("Quiz Score")

save_chart("10_bivariate_attendance_vs_quiz.png")


# ============================================================
# TASK 11: MULTIVARIATE ANALYSIS
# Question:
# How do study hours, quiz score, programme,
# and satisfaction interact?
#
# Variables:
# X-axis   = Weekly Study Hours
# Y-axis   = Quiz Score
# Group    = Programme
# Size     = Satisfaction Level
#
# Suitable visual:
# Bubble/scatter plot
# ============================================================

plt.figure(figsize=(9, 6))

# Plot each programme separately.
# Matplotlib automatically assigns different default colours.
for programme in df["Programme"].unique():

    subset = df[df["Programme"] == programme]

    plt.scatter(
        subset["Weekly_Study_Hours"],
        subset["Quiz_Score"],
        s=subset["Satisfaction_Level"] * 45,
        alpha=0.65,
        label=programme
    )

plt.title(
    "11. Multivariate: Study Hours, Quiz Score,\n"
    "Programme and Satisfaction"
)

plt.xlabel("Weekly Study Hours")
plt.ylabel("Quiz Score")
plt.legend(title="Programme")

save_chart("11_multivariate_study_quiz_programme_satisfaction.png")


# ============================================================
# FINAL MESSAGE
# ============================================================

print()
print("All 11 visualizations have been generated.")
print("Output folder:")
print(OUTPUT_DIR.resolve())
