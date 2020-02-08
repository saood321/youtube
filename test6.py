import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
import xlrd
import pandas as pd


df = pd.read_excel("random2.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Happy1'])
list2 = list(df['Happy2'])
list3 = list(df['Happy3'])
list4 = list(df['Happy4'])
list5 = list(df['Happy5'])
list6 = list(df['Happy6'])
list7 = list(df['Sad1'])
list8 = list(df['Sad2'])
#list9 = list(df['Sad3'])
#list10 = list(df['Sad4'])
#list11 = list(df['Sad5'])
#list12 = list(df['Sad6'])
list13 = list(df['Normal1'])
list14 = list(df['Normal2'])
#list15 = list(df['Normal3'])
#list16 = list(df['Normal4'])
#list17 = list(df['Normal5'])
#list18 = list(df['Normal6'])

X = np.array([list1,list2,list3,list4,list5,list6,list7,list8,list13,list14])
y=[1,1,1,1,1,1,0,0,2,2]

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)
Testlist = list(df['Test10'])
var =clf.predict([Testlist])
if var==1:
    print("Happy mood")
elif var==0:
    print("Sad Mood")
else:
    print("Normal Mood")