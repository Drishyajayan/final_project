from keras.utils.np_utils import to_categorical
import numpy

import os

import warnings
from random import shuffle
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np


import pandas as pd


# all_wave = []
# all_label = []
#
#
# import tflearn
# import numpy as np
#
# import tensorflow as tf
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix
#
# import pandas as pd
#
#
#
# def one_hot_from_item(item, items):
#     # items=set(items) # assure uniqueness
#     x = [0] * 2  # numpy.zeros(len(items))
#
#     x[int(item)] = 1
#     return x
#
#
# df = pd.read_csv(r'D:\project\src\heart.csv', header=None)
# data = np.array(df)
#
#
# ydata = data[:, -1]
#
#
#
# print("++++**************")
# print(ydata[1])
# x=[]
# y=[]
# ii=0
# for i in ydata:
#     if ii!=0:
#         row=i.split(";")
#         x.append(row[:-1])
#         if row[-1]=="No":
#             y.append(0)
#         else:
#             y.append(1)
#     ii=ii+1
#
# print(x[0])
# print(y[0])
# print("+=+=+=+=+=+=+=+")
#
# x_train=[]
# y_train=[]
# for i in x:
#     row=[]
#
#     if i[0]=="Male":
#         row.append(0)
#     else:
#         row.append(1)
#     row.append(int(i[3]))
#     row.append(int(i[6]))
#     row.append(int(i[7]))
#     row.append(int(i[12]))
#     row.append(int(i[13]))
#     row.append(int(i[18]))
#     row.append(int(i[19]))
#     row.append(int(i[24]))
#     row.append(int(i[25]))
#     x_train.append(row)
# print("=================")
# print(x_train[0])
# print(y[0])
# #
# print(x_train[0],len(x_train))
#
#
# # for i in y:
# #     y_train.append(one_hot_from_item(i,2))
#
#
# #
# import os
#
#
#
# print(x_train[0],len(x_train))
# import csv
# mydict = []
#
#
#
#
# #
# # #.................training & testing .....................
# #
# learning_rate = 0.00001
# training_iters = 59  # steps
# #
# width = 1
# height = 10
# classes = 2
#


import csv
Sex=[]
ChestPainType=[]
RestingECG=[]
ExerciseAngina=[]
ST_Slope=[]
xx=[]
yy=[]

# opening the CSV file
with open('D:\project\src\heart.csv', mode ='r')as file:

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

X, Y = x,y
X=np.array(X)
print(len(X),len(Y))
print()

trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.20, random_state=4)


X = trainX
y_int = Y
Y = to_categorical(trainY,2)
#Y = trainY

# Test Set
XTest = testX
ytest=testY

ytest_int = testY
yTest = to_categorical(ytest_int)

# create model
model = Sequential()
model.add(Dense(output_dim=4, init='uniform', activation='relu', input_dim=11))
model.add(Dense(output_dim=4, init='uniform', activation='relu', input_dim=4))
model.add(Dense(output_dim=2, init='uniform', activation='softmax', input_dim=4))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()
if not os.path.isfile("model123.h5"):

    print(X[0])
# Fit the model
    history = model.fit(X, Y,epochs=60,batch_size=20)

    curt = 0
    print("\nSLNO  :  Predict -> Label\n")
    model_json = model.to_json()
    with open("model1.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model1.h5")
    lt = len(XTest)
    y = model.predict(XTest)
    ytest = []
    ans = []
    # print()
    for r in range(0, len(y)):
        p = list(y[r]).index(max(list(y[r])))
        v = list(yTest[r]).index(max(list(yTest[r])))
        ans.append(p)
        ytest.append(v)
        # print(list(y[r]).index(max(list(y[r]))))
        # print(list(Y[r]).index(max(list(Y[r]))))
        # print( "********")

        if p == v:
            curt += 1
            # translate_text = translator.translate(str(outputlabels[int(p)]), lang_src='en', lang_tgt='ml')

        # print(r + 1, "\t:  ", int(p) + 1, outputlabels[int(p)], " --> ", int(v + 1))

    cm = confusion_matrix(ytest, ans)
    print("confusion_matrix")
    print(cm)
    print("\n\t ACCURACY : ", curt / lt)


else:
    model=model_from_json(open("model1.json","r").read())
    model.load_weights("model1.h5")


    print("\n....Model is already trained....\n")
    print("\nSLNO  :  Predict -> Label\n")
    curt = 0
    lt = len(XTest)
    y = model.predict(XTest)
    ytest = []
    ans = []
    # print()
    for r in range(0, len(y)):
        p = list(y[r]).index(max(list(y[r])))
        v = list(yTest[r]).index(max(list(yTest[r])))
        ans.append(p)
        ytest.append(v)
        # print(list(y[r]).index(max(list(y[r]))))
        # print(list(Y[r]).index(max(list(Y[r]))))
        # print( "********")

        if p == v:
            curt += 1
            # translate_text = translator.translate(str(outputlabels[int(p)]), lang_src='en', lang_tgt='ml')

        # print(r + 1, "\t:  ", int(p) + 1, outputlabels[int(p)], " --> ", int(v + 1))

    cm = confusion_matrix(ytest, ans)
    print("confusion_matrix")
    print(cm)
    print("\n\t ACCURACY : ", curt / lt)
# ******************************

# translator = google_translator()
# #model.load("model1.h5")
# print("\n....Model is already trained....\n")
# print("\nSLNO  :  Predict -> Label\n")
# curt = 0
# lt = len(XTest)
# ytest=[]
# ans=[]
# for i in range(1, lt + 1):
#     p = np.argmax(model.predict(XTest[i - 1:i]))
#     v = np.argmax(ytest_int[i - 1:i])
#     ans.append(p)
#     ytest.append(v)
#     if p == v:
#         curt += 1
#             #translate_text = translator.translate(str(outputlabels[int(p)]), lang_src='en', lang_tgt='ml')
#
#         print(i, "\t:  ", int(p)+1,outputlabels[int(p)], " --> ", int(v+1))
#
#
# cm=confusion_matrix(ytest,ans)
# print("confusion_matrix")
# print(cm)
# print("\n\t ACCURACY : ", curt / lt)
#


# ****************************
# print("Prediction   Result")
# files = os.listdir("predict/")
# #print(len(files))
# for wav in files:
#     if not wav.endswith(".wav"): continue
#     model.load("model1.h5")
#
#     //T = speechData.mfcc_target1("predict/"+wav)
#     #lt = len(T)
#     pp = np.argmax(model.predict(T))
#     print(outputlabels[int(pp)])

# #Only code needed to save model
# model_json = model.to_json()
# with open("model1.json", "w") as json_file:
#     json_file.write(model_json)
# model.save_weights("model1.h5")
##################################