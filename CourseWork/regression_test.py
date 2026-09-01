import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import time

startTime = time.time()

from full_logistic_model import fullLogisticModel#import the class containing the regression model

data = pd.read_csv("cleaned_cardio_train3.csv")#read the data from the cleaned cardiovascular dataset

data['BMI'] = data['weight'] / ((data['height']/100) **2) #creates a column called BMI using the weight and height columns


cardioData = data.drop(["id", "cardio","height", "weight"], axis=1).values #contains all the records for every column except 'id', 'cardio', 'height' and 'weight'
cardioValue = data["cardio"].values #contains all the values for the 'cardio' column

scaler = StandardScaler()
cardioData = scaler.fit_transform(cardioData)
#scales the data down using a standard scaler (Z-world)

cardioData_train, cardioData_test, cardioValue_train, cardioValue_test = train_test_split(
cardioData, cardioValue, test_size=0.2, random_state=55)
#split the data into 80% training data, and 20% test data

# Train model
model = fullLogisticModel(lr=0.01, numIters=5000)
model.fit(cardioData_train, cardioValue_train)

# Test model
cardioValue_pred = model.predict(cardioData_test)
acc = accuracy_score(cardioValue_test, cardioValue_pred)

endTime = time.time()

print("time taken:",endTime - startTime)
print(f"Accuracy: {acc*100:.2f}%")


#tests for the regression model
age = int(input("enter age (years):")) * 365
height = input("enter height (cm):")
weight = input("enter weight (kg):")
gender = input("enter gender (Female - 1/Male - 2 ):")
sysBP = input("enter systolic blood pressure (mm Hg):")
diaBP = input("enter diastolic blood pressure (mm Hg):")
cholesterol = int(input("enter cholesterol levels (mg/dL):"))

if cholesterol <= 200:
    cholesterol = 1
elif cholesterol > 200 and cholesterol <= 240:
    cholesterol = 2
else:
    cholesterol = 3

glucose = int(input("enter glucose levels (mg/dL):"))

if glucose <= 100:
    glucose = 1
elif glucose > 100 and glucose <= 125:
    glucose = 2
else:
    glucose = 3

smoking = input("enter smoking status (0 or 1):")
alcohol = input("enter alcohol status (0 or 1):")
sedentary = input("are you physically active (150minutes a week or more):")
cardioStatus = input("do you have a cardiovascular disease (0 or 1):")
userInputs = {"age": [int(age)],
              "height": [float(height)],
              "weight": [float(weight)],
              "gender": [int(gender)],
              "ap_hi": [int(sysBP)],
              "ap_lo": [int(diaBP)],
              "cholesterol": [int(cholesterol)],
              "gluc": [int(glucose)],
              "smoke": [int(smoking)],
              "active": [int(sedentary)],
              "alco":[int(alcohol)]
              }

userDataFrame = pd.DataFrame(userInputs)

# Add BMI like in training
userDataFrame['BMI'] = userDataFrame['weight'] / ((userDataFrame['height']/100) ** 2)

# Drop height and weight (to match training features)
userDataFrame = userDataFrame.drop(["height", "weight"], axis=1)

userDataFrame = scaler.transform(userDataFrame)

print(userDataFrame)

ans = model.predict(userDataFrame)
print("actual probability:",model.probability(userDataFrame))
print(ans)
print("actual cardio status:", cardioStatus)