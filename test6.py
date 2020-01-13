import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm
import xlrd
import pandas as pd
xlist=[]
ylist=[]
zlist=[]
klist=[]
loc = ("random.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

df = pd.read_excel("random.xls", sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Happy1'])
list2 = list(df['Happy2'])
list3 = list(df['Sad1'])
list4 = list(df['Sad2'])

X = np.array([list1,list2,list3,list4])
y=[1,1,0,0]
print(X)
print(y)
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)
list5 = list(df['Happy6'])
print(clf.predict([list5]))
