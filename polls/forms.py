from django import forms
from .models import Customer, Criticalinsurancedata
from datetime import datetime, date

class CustomerForm(forms.Form):    
    custfirstname = forms.CharField(label='First Name', max_length=20)
    custmiddleinitial = forms.CharField(label='Middle Initial (Optional)', max_length=1, required=False)
    custlastname = forms.CharField(label='Last Name', max_length=20)
    custsuffix = forms.CharField(label='Name Suffix (Optional)', max_length=20, required=False)
    custdob = forms.DateTimeField(label='Date Of Birth (YYYY-MM-DD)', input_formats=['%Y-%m-%d'])
    
    custemailaddress = forms.EmailField(label='E-Mail Address', max_length=100) 
    ssn_tin = forms.CharField(label='Identification Number', max_length=12)
    ssn_type = forms.ChoiceField(label='Identification Number Type', choices = (("SSN","SSN"), ("TIN","TIN")))

    preferredlanguage = forms.CharField(label='Preferred Language', initial='English', max_length=20)

    #Not Displayed:
    custsalutation = forms.CharField(label='Salutation (Optional)', max_length=20, initial=None, required=False, widget=forms.HiddenInput())
    #Not Displayed:
    startdate = forms.CharField(initial=datetime.now().strftime("%Y-%m-%d"), required=False, widget=forms.HiddenInput())
    #Not Displayed:
    enddate = forms.CharField(initial=None, widget=forms.HiddenInput(), required=False)

    bmi = forms.FloatField(label='BMI') 
    numchildren = forms.IntegerField(label='Number of Children', initial=0)
    evermarriedflag = forms.BooleanField(label='Ever Married', initial=False, required=False) 
    sex = forms.ChoiceField(label='Assigned Sex at Birth', choices = [("Male","Male"), ("Female","Female")])
    smokerflag = forms.BooleanField(label='Smoker', initial=False, required=False) 

    #Not Displayed:
    lastassessmentdate = forms.DateTimeField(initial=None, widget=forms.HiddenInput(), required=False) 





class AssessmentForm(forms.Form):  
    custfirstname = forms.CharField(label='First Name', max_length=20)
    custmiddleinitial = forms.CharField(label='Middle Initial (Optional)', max_length=1, required=False)
    custlastname = forms.CharField(label='Last Name', max_length=20)
    custsuffix = forms.CharField(label='Name Suffix (Optional)', max_length=20, required=False)
    custdob = forms.DateTimeField(label='Date Of Birth (YYYY-MM-DD)', input_formats=['%Y-%m-%d'])
    
    #Not Displayed:
    assessmentdate = forms.DateTimeField(label='Assessment Date', initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=False, widget=forms.HiddenInput())  
    #Not Displayed:
    lastassessmentflag = forms.BooleanField(label='LastAssessmentFlag', initial=True, required=False, widget=forms.HiddenInput())  
    
    worktype = forms.ChoiceField(label='Work Type', initial = 'Private', choices = [("children","Children"), ("Govt_job","Government Job"),
                                                    ("Never_worked", "Never Worked"), ("Private", "Private"), ("Self-employed", "Self-employed")])

    urbanresidenceflag = forms.BooleanField(label='Lives in Urban Residence', required=False)  
    sleeptime = forms.IntegerField(label='Average Sleep Time (in Hours)')  

    physicalhealthscore = forms.IntegerField(label='Number of Days With Mental Health Problems In the Last 30 Days:', initial=0)  
    mentalhealthscore = forms.IntegerField(label='Number of Days With Mental Health Problems In the Last 30 Days:',  initial=0)  
     
    avgglucoselevel = forms.FloatField(label='Average Glucose Level (mg/dL)', initial=100) 
    
    physicalactivityflag = forms.BooleanField(label='Physically Active', required=False)  
    diffwalkingflag = forms.BooleanField(label='Has Difficulty Walking', required=False)

    alcoholflag = forms.BooleanField(label='Consumes Alcohol', required=False)  
    prevheartdiseaseflag = forms.BooleanField(label='Has History of Heart Disease', required=False)  
    prevstrokeflag = forms.BooleanField(label='Has History of Stroke', required=False) 

    diabeticflag = forms.BooleanField(label='Is Diabetic', required=False)  
    hypertensionflag = forms.BooleanField(label='Has Hypertension', required=False)  
    asthmaflag = forms.BooleanField(label='Has Asthma', required=False)  
    kidneydiseaseflag = forms.BooleanField(label='Has Kidney Disease', required=False)  
    skincancerflag = forms.BooleanField(label='Has Skin Cancer', required=False)  



class QuoteForm(forms.Form):  
    custfirstname = forms.CharField(label='First Name', max_length=20)
    custmiddleinitial = forms.CharField(label='Middle Initial (Optional)', max_length=1, required=False)
    custlastname = forms.CharField(label='Last Name', max_length=20)
    custsuffix = forms.CharField(label='Name Suffix (Optional)', max_length=20, required=False)
    custdob = forms.DateTimeField(label='Date Of Birth (YYYY-MM-DD)', input_formats=['%Y-%m-%d'])

    generalFlag = forms.BooleanField(label='General Insurance', initial=True, required=False)  
    heartFlag = forms.BooleanField(label='Heart Disease Insurance', required=False)  
    heartAmount = forms.FloatField(label='Coverage Amount For Heart Disease', initial=60000, required=False) 
    strokeFlag = forms.BooleanField(label='Stroke Insurance', required=False)  
    strokeAmount = forms.FloatField(label='Coverage Amount For Stroke', initial=60000, required=False) 
    