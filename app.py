import streamlit as st 
 
import pandas as pd 

import matplotlib.pyplot as plt 

#Button 

if st.button("Click Me"): 
    st.write("The button was clicked.")

#Checkbox 

show_data = st.checkbox("Show Data") 
 
if show_data: 
    st.write("The data will appear here.") 
 

#Slider 

score = st.slider( 
    "Select a score", 
    min_value=0, 
    max_value=100, 
    value=70 
) 
 
st.write("Selected score:", score) 
 

#Select Box 

programme = st.selectbox( 
    "Select Programme", 
    [ 
        "Islamic Data Science", 
        "Islamic Finance", 
        "Media Technology" 
    ] 
) 
 
st.write("Selected programme:", programme) 
 

#Multiselect 

programmes = st.multiselect( 
    "Select Programmes", 
    [ 
        "Islamic Data Science", 
        "Islamic Finance", 
        "Media Technology" 
    ] 
) 
 
st.write(programmes) 


#components

df = pd.read_excel( 
    "Fulldummydata.xlsx", 
    sheet_name="Student_Data" 
) 
 
st.title("Student Data") 
st.dataframe(df) 

#Preview Only Part of the Dataset 

st.subheader("First 10 Records") 
st.dataframe(df.head(10))

#Descriptive statistics can also be displayed: 

st.subheader("Summary Statistics") 
st.dataframe(df.describe()) 


#Select a Programme Interactively 

programmes = df["Programme"].unique() 
 
selected_programme = st.selectbox( 
    "Select a Programme", 
    programmes 
) 
 
filtered_df = df[ 
    df["Programme"] == selected_programme 
] 
 
st.dataframe(filtered_df)


#Create a Bar Chart 

#To compare average quiz scores among programmes: 

programme_scores = ( 
    df.groupby("Programme")["Quiz_Score"] 
    .mean() 
) 
 
st.subheader("Average Quiz Score by Programme") 
st.bar_chart(programme_scores)

#Use Matplotlib with Streamlit 

#The Matplotlib skills learned earlier can be reused directly inside Streamlit: 
 
programme_scores = ( 
    df.groupby("Programme")["Quiz_Score"] 
    .mean() 
    .sort_values() 
) 
 
fig, ax = plt.subplots() 
programme_scores.plot(kind="barh", ax=ax) 
ax.set_title("Average Quiz Score by Programme") 
ax.set_xlabel("Average Quiz Score") 
ax.set_ylabel("Programme") 
 
st.pyplot(fig) 


#Create A Histogram 
fig, ax = plt.subplots() 
ax.hist(df["Quiz_Score"], bins=10) 
ax.set_title("Distribution of Quiz Scores") 
ax.set_xlabel("Quiz Score")
ax.set_ylabel("Frequency") 
 
st.pyplot(fig) 

#Create A scatterplot

fig, ax = plt.subplots() 
 
ax.scatter( 
    df["Weekly_Study_Hours"], 
    df["Quiz_Score"] 
) 
 
ax.set_title("Study Hours vs Quiz Score") 
ax.set_xlabel("Weekly Study Hours") 
ax.set_ylabel("Quiz Score") 
 
st.pyplot(fig)

#Let user choose a visualization 
chart_type = st.selectbox( 
    "Choose Visualization", 
    ["Histogram", "Scatter Plot"] 
) 
 
if chart_type == "Histogram": 
    fig, ax = plt.subplots() 
    ax.hist(df["Quiz_Score"], bins=10) 
    ax.set_title("Quiz Score Distribution") 
    st.pyplot(fig) 
 
elif chart_type == "Scatter Plot": 
    fig, ax = plt.subplots() 
    ax.scatter( 
        df["Weekly_Study_Hours"], 
        df["Quiz_Score"] 
    ) 
    ax.set_xlabel("Weekly Study Hours") 
    ax.set_ylabel("Quiz Score") 
    st.pyplot(fig)

#Create a sidebar
st.sidebar.header("Filters") 
 
programme = st.sidebar.selectbox( 
    "Programme", 
    df["Programme"].unique() 
) 
 
gender = st.sidebar.selectbox( 
    "Gender", 
    df["Gender"].unique() 
)

#Use multiple columns
col1, col2, col3 = st.columns(3) 
 
col1.metric("Students", len(df)) 
 
col2.metric( 
    "Average Quiz Score", 
    round(df["Quiz_Score"].mean(), 1) 
) 
 
col3.metric( 
    "Average Attendance", 
    f"{df['Attendance_Rate'].mean():.1f}%" 
)

#Upload a Dataset from the Browser
uploaded_file = st.file_uploader( 
    "Upload an Excel file", 
    type=["xlsx"] 
) 
 
if uploaded_file is not None: 
    df = pd.read_excel(uploaded_file) 
    st.success("Dataset loaded successfully.") 
    st.dataframe(df)


# PAGE TITLE 
st.title("TD2310 Student Data Visualization Dashboard") 
st.write("Use the controls to explore student performance data.") 
 
# LOAD DATA 
df = pd.read_excel( 
    "Fulldummydata.xlsx", 
    sheet_name="Student_Data" 
) 
 
# SIDEBAR 
st.sidebar.header("Dashboard Filters") 
selected_programme = st.sidebar.selectbox( 
    "Select Programme", 
    ["All"] + sorted(df["Programme"].unique()) 
) 
 
# FILTER DATA 
if selected_programme == "All": 
    filtered_df = df.copy() 
else: 
    filtered_df = df[ 
        df["Programme"] == selected_programme 
    ] 
 
# SUMMARY METRICS 
col1, col2, col3 = st.columns(3) 
col1.metric("Students", len(filtered_df)) 
col2.metric( 
    "Average Quiz Score", 
    round(filtered_df["Quiz_Score"].mean(), 1) 
) 
col3.metric( 
    "Average Attendance", 
    f"{filtered_df['Attendance_Rate'].mean():.1f}%" 
) 
 
# DATA TABLE 
st.subheader("Student Records") 
st.dataframe(filtered_df) 
 
# QUIZ SCORE DISTRIBUTION 
st.subheader("Quiz Score Distribution") 
fig, ax = plt.subplots() 
ax.hist(filtered_df["Quiz_Score"], bins=10) 
ax.set_xlabel("Quiz Score") 
ax.set_ylabel("Frequency") 
st.pyplot(fig) 
 
# RELATIONSHIP 
st.subheader("Study Hours vs Quiz Score") 
fig, ax = plt.subplots() 
ax.scatter( 
    filtered_df["Weekly_Study_Hours"], 
    filtered_df["Quiz_Score"] 
) 
ax.set_xlabel("Weekly Study Hours") 
ax.set_ylabel("Quiz Score") 
st.pyplot(fig) 
