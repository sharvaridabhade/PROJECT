# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:31:22 2016

@author: SHARVARI
"""
import scipy
from scipy import array
import matplotlib.pyplot as plt
import numpy as np
P=input('Enter Pressure in Pa: ')
T=input('Enter temp in K: ')
molefrac=[]
rhopr1=[]
rhopr2=[]
rhompr21=[]
rhompr22=[]
rhocpr1=[]
rhocpr2=[]
for i in range (11):
    
    Ya=i*0.1
    molefrac.append(Ya)
    print("mole fraction of methane in mix")
    print Ya
    Yb=1-Ya
    Y=[Ya,Yb]
            #mole fraction
    Tc=array([190.56,305.33])           #K Critical temp
    Pc=array([45.99*10**5,48.71*10**5]) #Pa Critical pressure
    w=array([0.0113,0.1004])            #accentric factor
    k12=0                               #interaction parameter
    R=8.3142                            # UNIVERSAL GAS constant
    """peng robinson"""
    """parameters"""
    k=0.37464+1.54226*w-0.26992*w**2
    alpha=(1+k*(1-scipy.sqrt(T/Tc)))**2
    a=0.45724*(R**2*Tc**2/Pc)*alpha
    a12=scipy.sqrt(a[0]*a[1])*(1-k12)
    amix=Y[0]**2*a[0]+2*Y[0]*Y[1]*a12+a[1]*Y[1]**2
    b=R*Tc*0.0778/Pc
    bmix=Y[0]*b[0]+Y[1]*b[1]
    A=a*P/(R**2*T**2)
    Amix=Y[0]*A[0]+Y[1]*A[1]
    B=b*P/(R*T)
    Bmix=Y[0]*B[0]+Y[1]*B[1]
    print ("peng robinson EOS")
    mw=[16,30]
    mwmix=mw[0]*Y[0]+Y[1]*mw[1]
    coeff = [1,Bmix-1,-2*Bmix-2*Bmix**2*R*T-Bmix**2-Bmix*R*T+Amix,Bmix**3*R*T+Bmix**2*R*T-Amix*Bmix]
    roots=np.roots(coeff)

    print("liq density")
    V1=roots[2]*R*T/P
    Rho1=1/V1
    rhocalc1=Rho1*mwmix*10**-3
    print ("calc density")
    print rhocalc1
    rhopr1.append(rhocalc1)
    print ("gas density")
    V2=roots[0]*R*T/P
    Rho2=1/V2
    rhocalc2=Rho2*mwmix*10**-3
    print rhocalc2
    rhopr2.append(rhocalc2)
    """MPR2"""
    """parameters"""
    print ("MPR2 EOS")
    n=1.7309+1.6571*w+0.1554*w**2
    m=0.2476-0.8857*w+0.19*w**2
    alpha1=scipy.exp(1-n**scipy.log(T/Tc))
    
    beta=1+m*(1-T/Tc)
    a1=0.45724*(R**2*Tc**2/Pc)*alpha1
    a21=scipy.sqrt(a1[0]*a1[1])*(1-k12)
    amix=Y[0]**2*a1[0]+2*Y[0]*Y[1]*a21+a1[1]*Y[1]**2
    
    b1=R*Tc*0.0778*beta/Pc
    bmix=Y[0]*b1[0]+Y[1]*b1[1]
    A1=a1*P/(R**2*T**2)
    Amix1=Y[0]*A1[0]+Y[1]*A1[1]
    B1=b1*P/(R*T)
    Bmix1=Y[0]*B1[0]+Y[1]*B1[1]
    coeff = [1,Bmix1-1,-2*Bmix1-2*Bmix1**2*R*T-Bmix1**2-Bmix1*R*T+Amix1,Bmix1**3*R*T+Bmix1**2*R*T-Amix1*Bmix1]
    roots1=np.roots(coeff)
    print("liq density")
    V3=roots1[2]*R*T/P
    Rho3=1/V3
    rhocalc3=Rho3*mwmix*10**-3
    print ("calc density")
    print rhocalc3
    
    rhompr21.append(rhocalc3)
    print ("gas density")
    V4=roots1[0]*R*T/P
    Rho4=1/V4
    rhocalc4=Rho4*mwmix*10**-3
    print rhocalc4
    rhompr22.append(rhocalc4)
    """CPR"""
    print ("CPR EOS")
    k1=0.41287+1.34494*w+0.00421*w**2
    k2=0.03982+0.08551*w-1.05521*w**2
    k3=-0.01871+1.93328*w
    alpha2=array
    if T/Tc[0]<1:
       alpha21=scipy.exp(k1[0]*(1-T/Tc[0]))*(1+k2[0]*(1-scipy.sqrt(T/Tc[0]))**2+k3[0]*(1-scipy.sqrt(T/Tc[0]))**3)**2
    else:
       alpha21=scipy.exp(k1[0]*(1-T/Tc[0]))
    if T/Tc[1]<1:
       alpha22=scipy.exp(k1[1]*(1-T/Tc[1]))*(1+k2[1]*(1-scipy.sqrt(T/Tc[1]))**2+k3[1]*(1-scipy.sqrt(T/Tc[1]))**3)**2
    else:
       alpha22=scipy.exp(k1[1]*(1-T/Tc[1]))
    alpha2=array([alpha21,alpha22])
    
    a2=0.45724*(R**2*Tc**2/Pc)*alpha2
    a21=scipy.sqrt(a2[0]*a2[1])*(1-k12)
    amix=Y[0]**2*a2[0]+2*Y[0]*Y[1]*a21+a2[1]*Y[1]**2
    b=R*Tc*0.0778/Pc
    bmix=Y[0]*b[0]+Y[1]*b[1]
    A2=a2*P/(R**2*T**2)
    Amix2=Y[0]*A2[0]+Y[1]*A2[1]
    B2=b*P/(R*T)
    Bmix2=Y[0]*B2[0]+Y[1]*B2[1]
    print ("CPR EOS")
    mw=[16,30]
    mwmix=mw[0]*Y[0]+Y[1]*mw[1]
    coeff = [1,Bmix2-1,-2*Bmix2-2*Bmix2**2*R*T-Bmix2**2-Bmix2*R*T+Amix2,Bmix2**3*R*T+Bmix2**2*R*T-Amix2*Bmix2]
    roots2=np.roots(coeff)

    print("liq density")
    V5=roots2[2]*R*T/P
    Rho5=1/V5
    rhocalc5=Rho5*mwmix*10**-3
    print ("calc density")
    print rhocalc5
    rhocpr1.append(rhocalc5)
    print ("gas density")
    V6=roots2[0]*R*T/P
    Rho6=1/V6
    rhocalc6=Rho6*mwmix*10**-3
    print rhocalc6
    rhocpr2.append(rhocalc6)
    
    
fig=plt.figure();
ax=fig.add_subplot(111)
plt.title('liq density')
ax.plot(molefrac,rhopr1,'b');
ax.plot(molefrac,rhompr21,'g');
ax.plot(molefrac,rhocpr1,'r');
plt.xlabel('methane mole fraction')
plt.ylabel('density (kg/m3)')
fig.canvas.draw()
fig=plt.figure();
ax=fig.add_subplot(111)
plt.title('gas density')
plt.plot(molefrac,rhopr2,'b')
ax.plot(molefrac,rhompr22,'g');
ax.plot(molefrac,rhocpr2,'r');
plt.xlabel('methane mole fraction')
plt.ylabel('density (kg/m3)')
fig.canvas.draw()
   
    