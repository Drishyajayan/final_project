import csv
Sex=[]
ChestPainType=[]
RestingECG=[]
ExerciseAngina=[]
ST_Slope=[]
xx=[]
yy=[]

# opening the CSV file
with open('heart.csv', mode ='r')as file:

# reading the CSV file
	csvFile = csv.reader(file)

	# displaying the contents of the CSV file
	i=0
	for lines in csvFile:
		if i!=0:
			row=[]
			row.append(lines[0])
			row.append(lines[1])
			row.append(lines[2])
			row.append(lines[3])
			row.append(lines[4])
			row.append(lines[5])
			row.append(lines[6])
			row.append(lines[7])
			row.append(lines[8])
			row.append(lines[9])
			row.append(lines[10])
			xx.append(row)
			if lines[1] not in Sex:
				Sex.append(lines[1])
			if lines[2] not in ChestPainType:
				ChestPainType.append(lines[2])

			if lines[6] not in RestingECG:
				RestingECG.append(lines[6])

			if lines[8] not in ExerciseAngina:
				ExerciseAngina.append(lines[8])

			if lines[10] not in ST_Slope:
				ST_Slope.append(lines[10])

			yy.append(lines[11])
		i=i+1

print(Sex,ChestPainType,RestingECG,ExerciseAngina,ST_Slope)
print(xx)
print(yy)

x=[]
y=[]
for  i in range(0,len(xx)):
	row=[]
	row.append(float(xx[i][0]))
	row.append(float(Sex.index(xx[i][1])))
	row.append(float(ChestPainType.index(xx[i][2])))
	row.append(float(xx[i][3]))
	row.append(float(xx[i][4]))
	row.append(float(xx[i][5]))
	row.append(float(RestingECG.index(xx[i][6])))
	row.append(float(xx[i][7]))
	row.append(float(ExerciseAngina.index(xx[i][8])))
	row.append(float(xx[i][9]))
	row.append(float(ST_Slope.index(xx[i][10])))
	x.append(row)
	y.append(int(yy[i]))

print(x)
print(y)


import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

X_train, X_test, y_train, y_test = train_test_split( x,y, test_size = 0.2)

# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

gnb.fit(X_train, y_train)


y_pred = gnb.predict(X_test)


print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))

print("Report : \n", classification_report(y_test, y_pred))