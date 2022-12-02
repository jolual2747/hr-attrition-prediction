from flask import Flask, render_template, request, flash
from forms import PredecirForm
import os
from flask_bootstrap import Bootstrap
from predicter import predict_attrition

secretkey=os.urandom(32)
app=Flask(__name__,instance_relative_config=False)
app.secret_key=secretkey
Bootstrap(app)

#Listas para poblar campos de selección
education=['Human Resources', 'Life Sciences', 'Marketing', 'Medical', 'Other',
                         'Technical Degree']
role=['Healthcare Representative', 'Research Scientist', 'Sales Executive', 'Human Resources', 
    'Research Director', 'Laboratory Technician', 'Manufacturing Director', 'Sales Representative', 'Manager']
marital=['Married', 'Single', 'Divorced']
lst_1_4=['1','2','3','4']

# Decorators
@app.route('/',methods=('GET','POST'))
def home():
    datos={}
    form=PredecirForm(request.form)
    form.EducationField.choices=education
    form.JobRole.choices=role
    form.MaritalStatus.choices=marital
    form.EnvironmentSatisfaction.choices=lst_1_4
    form.JobSatisfaction.choices=lst_1_4
    if request.method=='POST':
        if form.validate_on_submit():
            age=form.Age.data
            eduField=form.EducationField.data
            jobRole=form.JobRole.data
            maritalStatus=form.MaritalStatus.data
            montlyIncome=form.MonthlyIncome.data
            numCompanies=form.NumCompaniesWorked.data
            percentSalary=form.PercentSalaryHike.data
            totalWorking=form.TotalWorkingYears.data
            trainingTimes=form.TrainingTimesLastYear.data
            yearsCompany=form.YearsAtCompany.data
            yearsPromotion=form.YearsSinceLastPromotion.data
            yearsCurrent=form.YearsWithCurrManager.data
            enviromentSatisfaction=form.EnvironmentSatisfaction.data
            jobSatisfaction=form.JobSatisfaction.data
            datos['Age']=age
            datos['EducationField']=eduField
            datos['JobRole']=jobRole
            datos['MaritalStatus']=maritalStatus
            datos['MonthlyIncome']=montlyIncome
            datos['NumCompaniesWorked']=numCompanies
            datos['PercentSalaryHike']=percentSalary
            datos['TotalWorkingYears']=totalWorking
            datos['TrainingTimesLastYear']=trainingTimes
            datos['YearsAtCompany']=yearsCompany
            datos['YearsSinceLastPromotion']=int(yearsPromotion)
            datos['YearsWithCurrManager']=int(yearsCurrent)
            datos['EnvironmentSatisfaction']=int(enviromentSatisfaction)
            datos['JobSatisfaction']=int(jobSatisfaction)
            res=predict_attrition(datos)
            flash(res)
        else:
            flash('Please review the data entered','danger')
    return render_template("home.html",form=form)

if __name__ == "__main__":
    app.run(debug=True,port=8000,host="0.0.0.0")
