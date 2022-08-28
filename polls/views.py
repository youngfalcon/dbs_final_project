from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

from datetime import datetime, date
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from .forms import AssessmentForm, CustomerForm, QuoteForm
from .models import Criticalinsurancedata, Customer

import math
from django.contrib import messages
from django.utils.safestring import mark_safe

# ML MODELS

import numpy as np
import pandas as pd

import statistics
from statistics import mean, median, stdev, variance

# Machine learning packages
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression

# Plotting packages
import matplotlib.pyplot as plt

#To save/load models
import pickle

#======#======#======#======#======

# Dealing with Azure Data Lake

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

import os

#get the relevant data file from the data lake
def get_data(blobname: str):
    #Hard-coded just so that the program is easy to run, would normally be read from an environemtn variable
    connect_str = "DefaultEndpointsProtocol=https;AccountName=insdata;AccountKey=tCEsT8b7uvR78LkoesVe6F6kEew8Sq5dO1u83PAZtmCpGAMoOm/wApgT2XCcHzwqwCxR5hA2tVKB+AStcdoQdw==;EndpointSuffix=core.windows.net"

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    blob_client = blob_service_client.get_blob_client(
        'data', blobname, snapshot=None)

    blob_data = blob_client.download_blob()
    data = blob_data.readall()

    with open("./data/"+blobname, "wb") as binary_file:
        # Write bytes to file
        binary_file.write(data)

def upload_model(blobname: str):
    connect_str = "DefaultEndpointsProtocol=https;AccountName=insdata;AccountKey=tCEsT8b7uvR78LkoesVe6F6kEew8Sq5dO1u83PAZtmCpGAMoOm/wApgT2XCcHzwqwCxR5hA2tVKB+AStcdoQdw==;EndpointSuffix=core.windows.net"

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    blob_client = blob_service_client.get_blob_client(
        'models', blobname, snapshot=None)

    with open("./models/"+blobname, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

def get_model(blobname: str):
    connect_str = "DefaultEndpointsProtocol=https;AccountName=insdata;AccountKey=tCEsT8b7uvR78LkoesVe6F6kEew8Sq5dO1u83PAZtmCpGAMoOm/wApgT2XCcHzwqwCxR5hA2tVKB+AStcdoQdw==;EndpointSuffix=core.windows.net"

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    blob_client = blob_service_client.get_blob_client(
        'models', blobname, snapshot=None)

    blob_data = blob_client.download_blob()
    data = blob_data.readall()
    
    with open("./models/"+blobname, "wb") as binary_file:
        binary_file.write(data)
    
    return pickle.load(open("./models/"+blobname, 'rb'))
    
#======#======#======

# Training and storing models (Taken from the .ipynb files submitted in part 4)

def labelIsTarget(label: str, target :str):
  try:
    if(label.lower() == target.lower()):
      return 1
    else:
      return 0
  except:
    return np.NaN

def trainGeneralModel(blobname: str):
    df_raw = pd.read_csv('./data/'+blobname)

    df = df_raw.copy()

    # Turn categorical variables into dummy variables:

    df['isMale'] = df['sex'].apply(lambda s: labelIsTarget(s,'male'))
    # isFemale is implicit

    df['isSmoker'] = df['smoker'].apply(lambda s: labelIsTarget(s,'yes'))
    # isNotSmoker is implicit

    df['isNorthEast'] = df['region'].apply(lambda s: labelIsTarget(s,'northeast'))
    df['isNorthWest'] = df['region'].apply(lambda s: labelIsTarget(s,'northwest'))
    df['isSouthEast'] = df['region'].apply(lambda s: labelIsTarget(s,'southeast'))
    # isSouthWest is implicit

    X_cols = ['age', 'bmi', 'children', 'isMale', 'isSmoker', 'isNorthEast', 'isNorthWest', 'isSouthEast']
    y_col = 'charges'

    data = df [X_cols+[y_col]].copy().dropna()

    #Disabled scaler for ease of application
    #scaler = StandardScaler()
    #data[X_cols] = scaler.fit_transform(data[X_cols])

    model = RandomForestRegressor().fit(data[X_cols].values,data[y_col].values)
    pickle.dump(model, open('./models/general_model', 'wb'))

def trainHeartModel(blobname: str):
    df_raw = pd.read_csv('./data/'+blobname)

    df = df_raw.copy()

    # Turn categorical variables into dummy variables:

    df['hasHeartDisease'] = df['HeartDisease'].apply(lambda s: labelIsTarget(s,'Yes'))

    df['isSmoker'] = df['Smoking'].apply(lambda s: labelIsTarget(s,'Yes'))

    df['drinks'] = df['AlcoholDrinking'].apply(lambda s: labelIsTarget(s,'Yes'))

    df['isActive'] = df['PhysicalActivity'].apply(lambda s: labelIsTarget(s,'Yes'))

    df['hasDiffWalking'] = df['DiffWalking'].apply(lambda s: labelIsTarget(s,'Yes'))

    df['isMale'] = df['Sex'].apply(lambda s: labelIsTarget(s,'Male'))

    # For AgeCategory, let us use the numerical value of the first value presented (the lower-limit)
    df['age'] = df['AgeCategory'].apply(lambda s: int(s[:2]))

    # Removed for now as Race is not stored in our current implementation
    # Race: (Possibilities: ['White', 'Black', 'Asian', 'American Indian/Alaskan Native', 'Other', 'Hispanic'])
    #df['isWhite'] = df['Race'].apply(lambda s: labelIsTarget(s,'White'))
    #df['isBlack'] = df['Race'].apply(lambda s: labelIsTarget(s,'Black'))
    #df['isAsian'] = df['Race'].apply(lambda s: labelIsTarget(s,'Asian'))
    #df['isNative'] = df['Race'].apply(lambda s: labelIsTarget(s,'American Indian/Alaskan Native'))
    #df['isHispanic'] = df['Race'].apply(lambda s: labelIsTarget(s,'Hispanic'))
    # Other is implicit

    # Removed for now 
    # GenHealth: (Possibilities: ['Very good', 'Fair', 'Good', 'Poor', 'Excellent'])
    #health_map = {'Poor':1, 'Fair':2, 'Good':3, 'Very good':4, 'Excellent':5}
    #df['health'] = df['GenHealth'].apply(lambda s: health_map[s])

    # Patient medical history:
    df['hadStroke'] = df['Stroke'].apply(lambda s: labelIsTarget(s,'Yes'))
    df['isDiabetic'] = df['Diabetic'].apply(lambda s: labelIsTarget(s,'Yes'))
    df['hasAsthma'] = df['Asthma'].apply(lambda s: labelIsTarget(s,'Yes'))
    df['hasKidneyDisease'] = df['KidneyDisease'].apply(lambda s: labelIsTarget(s,'Yes'))
    df['hasSkinCancer'] = df['SkinCancer'].apply(lambda s: labelIsTarget(s,'Yes'))

    #Removed: 'isWhite', 'isBlack', 'isAsian', 'isNative', 'isHispanic', 'health'
    X_cols = ['isSmoker', 'drinks', 'isActive', 'hasDiffWalking', 'isMale', 'age',
            'hadStroke', 'isDiabetic', 'hasAsthma', 'hasKidneyDisease', 'hasSkinCancer']

    y_col = 'hasHeartDisease'

    data = df [X_cols+[y_col]].copy().dropna()

    #Disabled scaler for ease of application
    #scaler = StandardScaler()
    #data[X_cols] = scaler.fit_transform(data[X_cols])

    model = LogisticRegression().fit(data[X_cols].values,data[y_col].values)
    pickle.dump(model, open('./models/heart_disease_model', 'wb'))

def trainStrokeModel(blobname: str):
    df_raw = pd.read_csv('./data/'+blobname)

    df = df_raw.copy()

    # Turn categorical variables into dummy variables:

    df['isMale'] = df['gender'].apply(lambda s: labelIsTarget(s,'Male'))

    df['hasMarried'] = df['ever_married'].apply(lambda s: labelIsTarget(s,'Yes'))

    df['inUrban'] = df['Residence_type'].apply(lambda s: labelIsTarget(s,'Urban'))

    # work_type: (Possibilities: ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
    df['worksPrivate'] = df['work_type'].apply(lambda s: labelIsTarget(s,'Private'))
    df['worksSelf'] = df['work_type'].apply(lambda s: labelIsTarget(s,'Self-employed'))
    df['worksGovt'] = df['work_type'].apply(lambda s: labelIsTarget(s,'Govt_job'))
    df['worksChildren'] = df['work_type'].apply(lambda s: labelIsTarget(s,'children'))
    # Never_worked is implicit

    # smoking_status: (Possibilities: ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])
    df['smokeFormer'] = df['smoking_status'].apply(lambda s: labelIsTarget(s,'formerly smoked'))
    df['smokeNever'] = df['smoking_status'].apply(lambda s: labelIsTarget(s,'never smoked'))
    df['smokeCur'] = df['smoking_status'].apply(lambda s: labelIsTarget(s,'smokes'))
    # Unknown is implicit


    X_cols = ['age', 'avg_glucose_level', 'bmi', 'hypertension', 'heart_disease', 'isMale', 'hasMarried', 
            'worksPrivate', 'worksSelf', 'worksGovt', 'worksChildren', 'smokeFormer', 'smokeNever', 'smokeCur']

    y_col = 'stroke'

    data = df[X_cols+[y_col]].copy().dropna()

    #Disabled scaler for ease of application
    #scaler = StandardScaler()
    #data[X_cols] = scaler.fit_transform(data[X_cols])

    model = LogisticRegression().fit(data[X_cols].values,data[y_col].values)
    pickle.dump(model, open('./models/stroke_model', 'wb'))

#======#======#======#======#======

def index(request):
    return render(request, 'polls/index.html')
    #return HttpResponse("You're at the polls index.")

def updateGeneralModel(request):
    get_data('expenses.csv')
    trainGeneralModel('expenses.csv')
    upload_model('general_model')
    return redirect('/polls/')

def updateHeartModel(request):
    get_data('heart_disease_data.csv')
    trainHeartModel('heart_disease_data.csv')
    upload_model('heart_disease_model')
    return redirect('/polls/')

def updateStrokeModel(request):
    get_data('stroke_data.csv')
    trainStrokeModel('stroke_data.csv')
    upload_model('stroke_model')
    return redirect('/polls/')

def customerRegistration(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            print('Valid form received.')
            attributes = form.cleaned_data
            attributes['custdob'] = request.POST.dict()['custdob']
            attributes['startdate'] = timezone.now().strftime("%Y-%m-%d")
            attributes['enddate'] = None
           
            customer = Customer(**(attributes))
            customer.save()
        else:
            print('Invalid form!')
            print(form.errors.as_data())

        return render(request, 'polls/customer_form.html', {'form': form})
    else:
        form = CustomerForm()
        return render(request, 'polls/customer_form.html', {'form': form})

def assessmentEntry(request):
    if request.method == "POST":
        form = AssessmentForm(request.POST)
        
        if form.is_valid(): #TODO: Fix Cleaning
            print('Valid form received.')
            attributes = form.cleaned_data
            attributes['custdob'] = request.POST.dict()['custdob']
            attributes['assessmentdate'] = timezone.now().strftime("%Y-%m-%d")
            attributes['lastassessmentflag'] = True

            print(attributes)

            customer = Customer.objects.filter(custfirstname=attributes['custfirstname'], 
                                                custmiddleinitial = attributes['custmiddleinitial'],
                                                custlastname = attributes['custlastname'],
                                                custsuffix = attributes['custsuffix'],
                                                custdob = attributes['custdob'],
                                                ).order_by('ssn_tin').first()

            del attributes['custfirstname']
            del attributes['custmiddleinitial']
            del attributes['custlastname']
            del attributes['custsuffix']
            del attributes['custdob']

            assessment = Criticalinsurancedata(custfirstname=customer, custmiddleinitial=customer.custmiddleinitial,
                                custlastname=customer.custlastname, custsuffix=customer.custsuffix, custdob=customer.custdob,
                                **(attributes))

            assessment.save()
        else:
            print('Invalid form!')
            print(form.errors.as_data())
            
        return render(request, 'polls/assessment_form.html', {'form': form})
    else:
        form = AssessmentForm()
        return render(request, 'polls/assessment_form.html', {'form': form})


def quoteRetrieval(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)

        general_model = get_model('general_model')
        heart_disease_model = get_model('heart_disease_model')
        stroke_model = get_model('stroke_model')

        if form.is_valid():
            print('Valid form received.')
            attributes = form.cleaned_data
            attributes['custdob'] = request.POST.dict()['custdob']

            customer = Customer.objects.filter(custfirstname=attributes['custfirstname'], 
                                                custmiddleinitial = attributes['custmiddleinitial'],
                                                custlastname = attributes['custlastname'],
                                                custsuffix = attributes['custsuffix'],
                                                custdob = attributes['custdob'],
                                                ).order_by('ssn_tin').first()

            assessments = Criticalinsurancedata.objects.filter(custfirstname=attributes['custfirstname'], 
                                                custmiddleinitial = attributes['custmiddleinitial'],
                                                custlastname = attributes['custlastname'],
                                                custsuffix = attributes['custsuffix'],
                                                custdob = attributes['custdob'],
                                                ).order_by('assessmentdate') #.last()

            #If we can't find a registered customer with the given properties
            if(customer == None):
                messages.success(request, 'No such customer exists. Please check the form elements.')
                return render(request, 'polls/quote_form.html', {'form': form})

            message = ''

            #First, calculate the age of the customer
            age = relativedelta(timezone.now(), customer.custdob).years

            #In creating all the x values here, we check the correct pre-processign steps and order of elements.

            #then, Create a numpy array in the correct form (Assume the customer is from the northeast)
            x_general = np.array([age, customer.bmi, customer.numchildren, 
                    int(customer.sex=='Male'), int(customer.smokerflag), 1, 0 ,0], dtype=np.float32).reshape(1, -1)

            x_heart = np.array([], dtype=np.float32)
            x_stroke = np.array([], dtype=np.float32)

            
            
            rel_ass = assessments.last()
            print(vars(rel_ass))

            if(len(assessments) != 0):
                rel_ass = assessments.last()
                x_heart = np.array([int(customer.smokerflag), int(rel_ass.alcoholflag), int(rel_ass.physicalactivityflag),
                    int(rel_ass.diffwalkingflag), int(customer.sex=='Male'), age, int(rel_ass.prevstrokeflag),
                    int(rel_ass.diabeticflag), int(rel_ass.asthmaflag), int(rel_ass.kidneydiseaseflag),
                    int(rel_ass.skincancerflag)], dtype=np.float32).reshape(1, -1)

                x_stroke = np.array([age, rel_ass.avgglucoselevel, customer.bmi, 
                    int(rel_ass.hypertensionflag), int(rel_ass.prevheartdiseaseflag),
                    int(customer.sex=='Male'), int(customer.evermarriedflag),
                    int(rel_ass.worktype=='Private'), int(rel_ass.worktype=='Self-employed'),
                    int(rel_ass.worktype=='Govt_job'), int(rel_ass.worktype=='children'), 0,
                    (1-int(customer.smokerflag)), int(customer.smokerflag)], dtype=np.float32).reshape(1, -1)
            
            #Multiplying all guesses by 1.1 to profit 10%

            if(attributes['generalFlag']):
                message += '<br> Calculated General Coverage Quote: ' + \
                        str(math.ceil(1.1*general_model.predict(x_general)[0])) + '$'

           
            if(attributes['heartFlag']):
                if(len(assessments) == 0):
                    message += '<br> Cannot calculate heart disease coverage quote as no valid assessment exists.'
                else:
                    message += '<br> Calculated Heart Disease Coverage Quote: ' + \
                            str(math.ceil(1.1*attributes['heartAmount']*(heart_disease_model.predict_proba(x_heart)[0][1]))) + '$'

            print(heart_disease_model.predict_proba(x_heart)[0][1])
            if(attributes['strokeFlag']):
                if(len(assessments) == 0):
                    message += '<br> Cannot calculate stroke coverage quote as no valid assessment exists.'
                else:
                    message += '<br> Calculated Stroke Coverage Quote: ' + \
                            str(math.ceil(1.1*attributes['strokeAmount']*(stroke_model.predict_proba(x_stroke)[0][1]))) + '$'

            #TODO: Update

            messages.success(request, mark_safe(message))
            return render(request, 'polls/quote_form.html', {'form': form})

        else:
            print('Invalid form!')
            return render(request, 'polls/quote_form.html', {'form': form})
    else:
        form = QuoteForm()
        return render(request, 'polls/quote_form.html', {'form': form})