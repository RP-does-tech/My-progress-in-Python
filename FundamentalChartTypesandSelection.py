"""
TD2310 - Introduction to Data Visualization
Fundamental Chart Types and Chart Selection

Dataset:
    DataTypesandVisualizationDummyDataset.xlsx

Sheet:
    Student Dataset

Required packages:
    pip install pandas matplotlib openpyxl

This script demonstrates the main chart types covered in the lecture:

1. Bar chart
2. Grouped bar chart
3. Stacked bar chart
4. Line chart
5. Area chart
6. Pie chart
7. Doughnut chart
8. Dot plot
9. Lollipop chart
10. Histogram
11. Box plot
12. Scatter plot
13. Bubble chart
14. Heatmap
15. Table

The examples also reinforce chart-selection principles:
- Start with the analytical question.
- Identify the type of data.
- Match the chart to the task.
- Keep the visual simple.
- Avoid misleading design.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# 1. FILE SETTINGS
# ============================================================

# Keep the Excel dataset in the same folder as this script.
BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "DataTypesandVisualizationDummyDataset.xlsx"

OUTPUT_DIR = BASE_DIR / "TD2310_ChartTypeSelection_Output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================
# 2. LOAD DATA
# ============================================================

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Student Dataset"
)

df["Month"] = pd.to_datetime(df["Month"])

print("Dataset loaded successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ============================================================
# 3. HELPER FUNCTION
# ============================================================

def finish_chart(filename):
    """
    Save the current figure as a PNG file,
    display it, then close it.
    """
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=200,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()


# ============================================================
# CHART 1: BAR CHART
# ============================================================
# Best for:
# Comparing values across categories.
#
# Question:
# Which programme has the highest average quiz score?
# ============================================================

programme_quiz = (
    df.groupby("Programme")["Quiz_Score"]
      .mean()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
programme_quiz.plot(kind="bar")

plt.title("1. Bar Chart: Average Quiz Score by Programme")
plt.xlabel("Programme")
plt.ylabel("Average Quiz Score")
plt.xticks(rotation=0)

finish_chart("01_bar_chart.png")


# ============================================================
# CHART 2: GROUPED BAR CHART
# ============================================================
# Best for:
# Comparing subcategories across larger categories.
#
# Question:
# How do average quiz scores differ by programme and gender?
# ============================================================

grouped_data = (
    df.groupby(["Programme", "Gender"])["Quiz_Score"]
      .mean()
      .unstack()
)

plt.figure(figsize=(9, 5))
grouped_data.plot(
    kind="bar",
    ax=plt.gca()
)

plt.title("2. Grouped Bar Chart: Quiz Score by Programme and Gender")
plt.xlabel("Programme")
plt.ylabel("Average Quiz Score")
plt.xticks(rotation=0)
plt.legend(title="Gender")

finish_chart("02_grouped_bar_chart.png")


# ============================================================
# CHART 3: STACKED BAR CHART
# ============================================================
# Best for:
# Showing composition within categories.
#
# Question:
# How many observations from each programme occur in each month?
# ============================================================

stacked_data = (
    df.groupby(["Month", "Programme"])
      .size()
      .unstack(fill_value=0)
)

# Convert datetime index into simple month labels
stacked_data.index = stacked_data.index.strftime("%b")

plt.figure(figsize=(9, 5))

stacked_data.plot(
    kind="bar",
    stacked=True,
    ax=plt.gca()
)

plt.title("3. Stacked Bar Chart: Programme Composition by Month")
plt.xlabel("Month")
plt.ylabel("Number of Observations")
plt.xticks(rotation=0)
plt.legend(title="Programme")

finish_chart("03_stacked_bar_chart.png")

# ============================================================
# CHART 4: LINE CHART
# ============================================================
# Best for:
# Showing change over time.
#
# Question:
# How does average quiz score change over the semester?
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

plt.title("4. Line Chart: Average Quiz Score Over Time")
plt.xlabel("Month")
plt.ylabel("Average Quiz Score")
plt.xticks(
    monthly_quiz.index,
    [d.strftime("%b") for d in monthly_quiz.index]
)
plt.grid(axis="y", alpha=0.3)

finish_chart("04_line_chart.png")


# ============================================================
# CHART 5: AREA CHART
# ============================================================
# Best for:
# Showing trend while emphasizing magnitude over time.
#
# Question:
# How does average attendance change over time?
# ============================================================

monthly_attendance = (
    df.groupby("Month")["Attendance_Rate"]
      .mean()
      .sort_index()
)

plt.figure(figsize=(8, 5))

plt.fill_between(
    monthly_attendance.index,
    monthly_attendance.values,
    alpha=0.5
)

plt.plot(
    monthly_attendance.index,
    monthly_attendance.values,
    marker="o"
)

plt.title("5. Area Chart: Average Attendance Over Time")
plt.xlabel("Month")
plt.ylabel("Average Attendance Rate (%)")
plt.xticks(
    monthly_attendance.index,
    [d.strftime("%b") for d in monthly_attendance.index]
)

finish_chart("05_area_chart.png")


# ============================================================
# CHART 6: PIE CHART
# ============================================================
# Best for:
# Showing simple part-to-whole composition
# when there are only a few categories.
#
# Question:
# What share of the observations belongs to each programme?
# ============================================================

programme_counts = df["Programme"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    programme_counts.values,
    labels=programme_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("6. Pie Chart: Programme Composition")

finish_chart("06_pie_chart.png")


# ============================================================
# CHART 7: DOUGHNUT CHART
# ============================================================
# Best for:
# Similar use to a pie chart, with a central space.
#
# Question:
# What share of observations belongs to each gender?
# ============================================================

gender_counts = df["Gender"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.4}
)

plt.title("7. Doughnut Chart: Gender Composition")

finish_chart("07_doughnut_chart.png")


# ============================================================
# CHART 8: DOT PLOT
# ============================================================
# Best for:
# Comparing values across categories with less visual ink
# than a traditional bar chart.
#
# Question:
# How do programmes compare in average study hours?
# ============================================================

programme_hours = (
    df.groupby("Programme")["Weekly_Study_Hours"]
      .mean()
      .sort_values()
)

plt.figure(figsize=(8, 5))

y = np.arange(len(programme_hours))

plt.scatter(
    programme_hours.values,
    y
)

plt.yticks(y, programme_hours.index)
plt.title("8. Dot Plot: Average Study Hours by Programme")
plt.xlabel("Average Weekly Study Hours")
plt.ylabel("Programme")

finish_chart("08_dot_plot.png")


# ============================================================
# CHART 9: LOLLIPOP CHART
# ============================================================
# Best for:
# Comparing categorical values with a lighter visual style.
#
# Question:
# How do programmes compare in average satisfaction?
# ============================================================

programme_satisfaction = (
    df.groupby("Programme")["Satisfaction_Level"]
      .mean()
      .sort_values()
)

plt.figure(figsize=(8, 5))

y = np.arange(len(programme_satisfaction))

plt.hlines(
    y=y,
    xmin=0,
    xmax=programme_satisfaction.values
)

plt.plot(
    programme_satisfaction.values,
    y,
    "o"
)

plt.yticks(y, programme_satisfaction.index)
plt.xlim(0, 5)

plt.title("9. Lollipop Chart: Average Satisfaction by Programme")
plt.xlabel("Average Satisfaction Level")
plt.ylabel("Programme")

finish_chart("09_lollipop_chart.png")


# ============================================================
# CHART 10: HISTOGRAM
# ============================================================
# Best for:
# Showing the distribution of one continuous numerical variable.
#
# Question:
# How are quiz scores distributed?
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Quiz_Score"],
    bins=8,
    edgecolor="black"
)

plt.title("10. Histogram: Distribution of Quiz Scores")
plt.xlabel("Quiz Score")
plt.ylabel("Frequency")

finish_chart("10_histogram.png")


# ============================================================
# CHART 11: BOX PLOT
# ============================================================
# Best for:
# Summarising distribution, median, spread and possible outliers.
#
# Question:
# How does quiz-score distribution differ across programmes?
# ============================================================

programmes = df["Programme"].unique()

box_data = [
    df.loc[df["Programme"] == programme, "Quiz_Score"]
    for programme in programmes
]

plt.figure(figsize=(9, 5))

plt.boxplot(
    box_data,
    tick_labels=programmes
)

plt.title("11. Box Plot: Quiz Scores by Programme")
plt.xlabel("Programme")
plt.ylabel("Quiz Score")

finish_chart("11_box_plot.png")


# ============================================================
# CHART 12: SCATTER PLOT
# ============================================================
# Best for:
# Examining the relationship between two numerical variables.
#
# Question:
# Is study time related to quiz performance?
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Weekly_Study_Hours"],
    df["Quiz_Score"]
)

plt.title("12. Scatter Plot: Study Hours vs Quiz Score")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Quiz Score")

finish_chart("12_scatter_plot.png")


# ============================================================
# CHART 13: BUBBLE CHART
# ============================================================
# Best for:
# Showing the relationship between two numerical variables
# while using bubble size for a third variable.
#
# Question:
# How do study hours, quiz score and satisfaction interact?
# ============================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Weekly_Study_Hours"],
    df["Quiz_Score"],
    s=df["Satisfaction_Level"] * 50,
    alpha=0.6
)

plt.title("13. Bubble Chart: Study Hours, Quiz Score and Satisfaction")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Quiz Score")

finish_chart("13_bubble_chart.png")


# ============================================================
# CHART 14: HEATMAP
# ============================================================
# Best for:
# Showing intensity or patterns across a matrix.
#
# Question:
# How do average quiz scores vary by programme and month?
#
# Note:
# This example uses matplotlib directly, not seaborn.
# ============================================================

heatmap_data = (
    df.pivot_table(
        index="Programme",
        columns="Month",
        values="Quiz_Score",
        aggfunc="mean"
    )
)

plt.figure(figsize=(9, 5))

plt.imshow(
    heatmap_data.values,
    aspect="auto"
)

plt.colorbar(label="Average Quiz Score")

plt.xticks(
    range(len(heatmap_data.columns)),
    [d.strftime("%b") for d in heatmap_data.columns]
)

plt.yticks(
    range(len(heatmap_data.index)),
    heatmap_data.index
)

# Add values inside cells
for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        plt.text(
            j,
            i,
            f"{heatmap_data.iloc[i, j]:.1f}",
            ha="center",
            va="center"
        )

plt.title("14. Heatmap: Average Quiz Score by Programme and Month")
plt.xlabel("Month")
plt.ylabel("Programme")

finish_chart("14_heatmap.png")


# ============================================================
# CHART 15: TABLE
# ============================================================
# Best for:
# Presenting exact values when precision is more important
# than showing patterns.
#
# Question:
# What are the exact average scores and attendance rates
# for each programme?
# ============================================================

summary_table = (
    df.groupby("Programme")
      .agg(
          Average_Quiz=("Quiz_Score", "mean"),
          Average_Attendance=("Attendance_Rate", "mean"),
          Average_Study_Hours=("Weekly_Study_Hours", "mean")
      )
      .round(1)
      .reset_index()
)

plt.figure(figsize=(10, 4))
plt.axis("off")

table = plt.table(
    cellText=summary_table.values,
    colLabels=summary_table.columns,
    loc="center",
    cellLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.7)

plt.title("15. Table: Exact Programme Summary Values")

finish_chart("15_table.png")


# ============================================================
# CHART-SELECTION SUMMARY
# ============================================================

print()
print("==================================================")
print("CHART-SELECTION SUMMARY")
print("==================================================")

print("""
Analytical Question              Suitable Chart
------------------------------------------------------------
Compare categories               Bar chart
Compare subcategories            Grouped bar chart
Show composition by category     Stacked bar chart
Show change over time            Line chart
Show magnitude over time         Area chart
Show simple part-to-whole        Pie / doughnut chart
Compare values simply            Dot / lollipop chart
Show numerical distribution      Histogram
Summarise spread and outliers    Box plot
Show relationship                Scatter plot
Add a third numerical variable   Bubble chart
Show matrix patterns             Heatmap
Show exact values                Table
""")

print("Chart-selection principles:")
print("1. Start with the question.")
print("2. Identify the data type.")
print("3. Match the chart to the analytical task.")
print("4. Keep the visual simple and readable.")
print("5. Avoid misleading design.")
print("6. Prefer clarity over decoration.")

print()
print("All fundamental chart examples have been generated.")
print("Output folder:")
print(OUTPUT_DIR.resolve())
