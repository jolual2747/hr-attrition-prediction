from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,IntegerField,\
    StringField,BooleanField,FieldList,FileField,MultipleFileField,FloatField,SelectField
from wtforms.validators import DataRequired,Length,Email,Regexp,NumberRange,InputRequired


class PredecirForm(FlaskForm):
    Age = IntegerField('Age', [DataRequired(message="You must provid a value"),
                                NumberRange(min=18,max=120,message="The value is incorrect")], render_kw={'style': 'width: 10ch'})
    EducationField = SelectField('EducationField', validators=[DataRequired()],render_kw={'style': 'width: 50ch'})
    JobRole = SelectField('JobRole', validators=[DataRequired()], render_kw={'style': 'width: 50ch'})
    MaritalStatus = SelectField('MaritalStatus', validators=[DataRequired()], render_kw={'style': 'width: 50ch'})
    MonthlyIncome = IntegerField('MonthlyIncome',  [DataRequired(message="You must provid a value"),
                                NumberRange(min=10000,max=200000,message="The value is incorrect")],  render_kw={'style': 'width: 20ch'})
    NumCompaniesWorked = IntegerField('NumCompaniesWorked',  [NumberRange(min=0,max=10,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    PercentSalaryHike = IntegerField('PercentSalaryHike',  [ NumberRange(min=0,max=30,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    TotalWorkingYears = IntegerField('TotalWorkingYears',  [NumberRange(min=0,max=40,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    TrainingTimesLastYear = IntegerField('TrainingTimesLastYear', [NumberRange(min=0,max=6,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    YearsAtCompany = IntegerField('YearsAtCompany',  [NumberRange(min=1,max=50,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    YearsSinceLastPromotion = IntegerField('YearsSinceLastPromotion', [NumberRange(min=0,max=20,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    YearsWithCurrManager = IntegerField('YearsWithCurrManager',  [NumberRange(min=0,max=20,message="The value is incorrect")], render_kw={'style': 'width: 20ch'})
    EnvironmentSatisfaction = SelectField('EnvironmentSatisfaction', validators=[DataRequired()], render_kw={'style': 'width: 20ch'})
    JobSatisfaction = SelectField('JobSatisfaction', validators=[DataRequired()], render_kw={'style': 'width: 20ch'})
    submit = SubmitField('Predecir')

 