from textblob import TextBlob
import csv
import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np
try1 = read_csv("reviews.csv",header=0)
h1=try1['names']
t1=[]
t2=[]
t3=[]
t4=[]
t5=[]
t6=[]
t7=[]
t8=[]
t=[]
no=[]
name=[]  

with open('reviews.csv') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        no.append(line[0])
        name.append(line[1])
        t1.append(line[2])
        t2.append(line[3])
        t3.append(line[4])
        t4.append(line[5])
        t5.append(line[6])
        t6.append(line[7])
        t7.append(line[8])
        t8.append(line[9])
neg1=0
pos1=0
sumt=0
#print(len(t1))

#-------------------------------------------------------------------------------------------------------------------------------------------------------

teacher=[no[0],name[0],t1[0],t2[0],t3[0],t4[0],t5[0],t6[0],t7[0],t8[0]]
#print(teacher)
tea=input("enter the teacher name")
ind = teacher.index(tea)
#print(ind)
with open('reviews.csv') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        t.append(line[ind])
theader=t.pop(0)
#print(theader)
#print("t value is",t)
neg1=0
pos1=0

for i in range(1,4):
    blob=TextBlob(t[i])
    text=blob.sentiment.polarity
    sumt=sumt+text
    if(text>0):
        pos1=pos1+text
    else:
        neg1=neg1+text
#print(pos1,pos2,pos3,neg1,neg2,neg3)
#Data to plot
#print("-------------SENTIMENT ANALYSIS MADE BY STUDENTS REVIEW---------------")
labels = 'Positive', 'negative', 
sizes = [pos1,abs(neg1)]
colors = ['gold', 'lightskyblue']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title(theader)
plt.axis('equal')
plt.show()


#---------------------------------------------------------------------------------
pos11=0
neg11=0
pos12=0
neg12=0
pos13=0
neg13=0
import csv
L=[]
#print(h1[0])

with open('reviews.csv') as csvfile:
    reader=csv.reader(csvfile)
    for col in reader:
        L.append(col[1])
    #print(L)
    #print(len(L))
    L.pop(0)
    #print(L)
    #print(len(L))
target= input("enter the name of the student:")
ind=L.index(target)
i=ind
#print(ind)
blob=TextBlob(t1[i])
text=blob.sentiment.polarity
if(text>0):
    pos11=text
else:
    neg11=text
#print("teach1",pos11,neg11)
blob=TextBlob(t2[i])
text=blob.sentiment.polarity
if(text>0):
    pos12=text
else:
    neg12=text
#print("teact1",pos12,neg12)
blob=TextBlob(t3[i])
text=blob.sentiment.polarity
if(text>0):
    pos13=text
else:
    neg13=text
#print("teact2",pos13,neg13)
posavg=pos11+pos12+pos13
negavg=neg11+neg12+neg13
a=posavg
b=abs(negavg)
print("SATISFACTION PERCENT OF STUDENT ")
#Sprint("##############",a,b)
labels = 'Positive', 'negative', 
sizes = [a,b]
colors = ['gold', 'lightskyblue']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("SATISFACTION PERCENT OF STUDENT ")
plt.axis('equal')
plt.show()
#-------------------bar graph for each student------------
print("BAR GRAPH FOR STUDENT ")
blob=TextBlob(t1[i])
text1=blob.sentiment.polarity
blob=TextBlob(t2[i])
text2=blob.sentiment.polarity
blob=TextBlob(t3[i])
text3=blob.sentiment.polarity
objects = ('a','b','c')
y_pos=np.arange(len(objects))
performance=[text1,text2,text3]
plt.bar(y_pos,performance,align='center',alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('performance')
plt.xlabel('Teachers')
plt.title('SENTIMENT ANALYSIS OF STUDENT')
plt.show()
#--------------------overall graph-----------------------------------------------------
print("---STUDENT STATISFACTION ABOUT FACULTY MEMBERS IN THIS SEMESTER----") 
st1=0
st2=0
st3=0
for i in range(1,len(t1)):
    blob1=TextBlob(t1[i])
    text1=blob1.sentiment.polarity
    st1=st1+text1
    blob2=TextBlob(t2[i])
    text2=blob2.sentiment.polarity
    st2=st2+text2
    blob3=TextBlob(t3[i])
    text3=blob3.sentiment.polarity
    st3=st3+text3   
objects = ('a','b','c')
y_pos=np.arange(len(objects))
performance=[st1,st2,st3]
plt.bar(y_pos,performance,align='center',alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('performance')
plt.xlabel('Teachers')
plt.title('OVERALL STUDENT SATISFACTION ')
plt.show()
