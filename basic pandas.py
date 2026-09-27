#IMPORT PANDAS AS THE MAIN
import pandas as pd

#CREATE STUDENT DICTIONARY
student_data = {
    'Student_ID':[
        '25B1207', '25B1632', '23B0703'
    ],
    'Name':[
        'Syahmi', 'Hakeem', 'Safwan'
    ],
    'Gender':[
        'Male','Male','Male'
    ],
    'INTRODUCTION_TO_DATABASE_SCORE':[
        80,78,90
    ],
    'INTRODUCTION_TO_CLOUD_COMPUTING_SCORE':[
        78,80,79
    ],
    'COMPUTATIONAL_THINKING_SCORE':[
        70,70,78
    ],
    'Conduct_grade':[
        'Excellent', 'Excellent','Excellent'
    ],
    'Attendance_percentage':[
        100,98,85
    ]
}

#USING PANDA AS THE DATAFRAME
df = pd.DataFrame(student_data)

#CALCULATE THE AVERAGE SCORE ACROSS ALL THE SUBJECTS
subjects = [
    'INTRODUCTION_TO_DATABASE_SCORE', 'INTRODUCTION_TO_CLOUD_COMPUTING_SCORE', 'COMPUTATIONAL_THINKING_SCORE',
]
df['Average_score'] = df[subjects].mean(axis=1).round(2)


#CALCULATE THE AVERAGE STUDENT SCORES
print("\n--- STUDENT AVERAGE SCORES ---")
print(df[['Name', 'Average_score']].sort_values(
      'Average_score', ascending=False).to_string(index=False))

#DISOLAY PEFORMANCE GRADES USING FUNCTION
def assign_grade(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 80:
        return 'Very good'
    elif score >= 70:
        return 'Good'
    elif score >= 60:
        return 'Pass'
    else:
        return 'Fail'
df['Grade'] = df['Average_score'].apply(assign_grade)

print("\n--- STUDENT GRADES --- ")
print(df[['Name', 'Average_score', 'Grade']].to_string(index=False))


#DISPLAY ATTENDANCE PERCENTAGE
print("\n --- ATTENDANCE ANALYSIS ---")
gender_peformance = df.groupby('Gender').agg({
    'Attendance_percentage' : 'mean'
}).round(2)

print(gender_peformance)

#DISPLAY SUBJECTS ANALYSIS USING SERIES
print("\n--- SUBJECT ANALYSIS PERFORMANCE---")
for subject in subjects:
    s = df[subject]
    print(f"\n{subject.replace('_', ' ')}")
    print(f" Class Average : {s.mean ():1f}")
    print(f"  Highest Score : {s.max()} — {df.loc[s.idxmax(), 'Name']}")
    print(f"  Lowest Score  : {s.min()} — {df.loc[s.idxmin(), 'Name']}")
