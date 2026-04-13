import pandas as pd

df = pd.read_csv("LABTEST\hospital_diabetes_dataset.csv")
df.head()
print(df.head())

# Numerical
num_cols =['Age','BMI','Systolic_BP','Diastolic_BP','Glucose_Level','HbA1c','Cholesterol','Exercise_Minutes_Per_Day','Sleep_Hours','Hospital_Visits_Last_Year','Diet_Score']
for colm in num_cols:
    df[colm] = df[colm].fillna(df[colm].mean())

# Categorical
cat_cols =['Gender','Blood_Pressure_Category','Smoking_Status','Physical_Activity','Family_History','Admission_Type','Diagnosis']
for col in cat_cols:
    df[col].fillna({col:df[col].mode()}, inplace=True)
df.drop_duplicates(inplace=True)
df['Gender'] = df['Gender'].str.lower()

df['Gender'] = df['Gender'].replace({
    'm': 'male',
    'f': 'female'
})
df['Smoking_Status']=df['Smoking_Status'].str.lower()
df['Smoking_Status'] = df['Smoking_Status'].replace({
    'y': 'yes',
    'n': 'no',
    'o':'occasional'

})
df['Admission_Type']=df['Admission_Type'].str.lower()
df['Diagnosis']=df['Diagnosis'].str.lower()
print(df.head(50))
