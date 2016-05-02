# -*- coding: utf-8 -*-
"""
Created on Sun May 01 14:30:26 2016

@author:sharvari
"""
import scipy
from scipy.integrate import odeint
from scipy import array
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization
import win32com.client
xl=win32com.client.gencache.EnsureDispatch("Excel.Application")
wb=xl.Workbooks('ExamProblemData2.1.xlsx')
sheet=wb.Sheets('ExamProblemData')
def getdat(sheet,Range):
    data=sheet.Range(Range).Value
    data=scipy.array(data)
    data=data.reshape((1,len(data)))[0]
    return data
t=getdat(sheet,"A2:A11")   #****** Re
y1=getdat(sheet,"B2:B11")   #******* f
y2=getdat(sheet,"C2:C11") 
print t
#t=array([9,18,26,35,44,53,62,71,80])
#y1=array([41.17,33.54,27.54,20.96,14.93,10.02,7.71,4.8,1.88])
#y2=array([1.14,2.88,3.44,4.13,4.48,4.75,5.57,5.75,5.8])

y=array([y1,y2])
y=np.transpose(y)
yinitial=array([49.44,0])
Z=array([y1,y2,t])
y1,y2,t=Z
print Z
A0=array([1,1,1,1])
(k1,k2,m,n)=A0
def derivative(y,t,k1,k2,m,n):
    dcA=-k1*y[0]**m+k2*y[1]**n
    dcB=-k2*y[1]**n+k1*y[0]**m
    return array([dcA,dcB])

def myerror(A,Z):
    k1=A[0];k2=A[1];m=A[2];n=A[3]
    y1=Z[0]
    y2=Z[1]
    t=Z[2]
    y=array([y1,y2])

    y3=odeint(derivative,yinitial,t,args=(k1,k2,m,n))
    yT=np.transpose(y3)
    r=y-yT
    return r[0]
([ans,err])=optimization.leastsq(myerror,A0,Z)
print ans
k1=ans[0]
k2=ans[1]
m=ans[2]
n=ans[3]

y4=odeint(derivative,yinitial,t,args=(k1,k2,m,n))

fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(t,y,'*')

ax.plot(t,y4,'b')    
fig.canvas.draw()
plt.show()  