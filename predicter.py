import pandas as pd
import joblib
import os



def preprocessing():
    names = ['Age', 'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear', 
    'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'EnvironmentSatisfaction', 'JobSatisfaction', 
    'EducationField_Life Sciences', 'EducationField_Marketing', 'EducationField_Medical', 'EducationField_Other', 
    'EducationField_Technical Degree', 'JobRole_Human Resources', 'JobRole_Laboratory Technician', 'JobRole_Manager', 
    'JobRole_Manufacturing Director', 'JobRole_Research Director', 'JobRole_Research Scientist', 'JobRole_Sales Executive', 
    'JobRole_Sales Representative', 'MaritalStatus_Married', 'MaritalStatus_Single']
    schema = pd.DataFrame(data = 0.0, index = [0], columns = names)
    fields = ['Age', 'Attrition', 'EducationField', 'level']
    nums = ['Age', 'level']
    a = {}
    for field in fields:
        a[field] = input(f'Type the {field}: ')
    df = pd.DataFrame(data = list(a.values()), index = fields).transpose()
    for num in nums:
      df[num] = df[num].astype('float64')
    df = pd.get_dummies(df)
    aux = df.merge(schema.drop(columns = df.columns.to_list()), how = 'left', left_index=True, right_index=True)
    return aux

def load_model():
    path = os.getcwd()
    file_name = os.path.join(path,'pipeline.joblib')
    pipeline = joblib.load(file_name)
    return pipeline

def scale_and_predict(df, pipeline):
    a = pipeline.predict(df)
    return a


def predict_attrition():
    pipeline = load_model()
    df = preprocessing()
    prediction = scale_and_predict(df, pipeline)
    return prediction


