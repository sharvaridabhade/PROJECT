# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:38:15 2016

@author: Kaivalya
"""
#==============================================================================================================================#

import matplotlib.pyplot
import numpy

#==============================================================================================================================#

'''Creating a random array of desired dimensions containing only 0,1,2,3 as its elements'''
M=numpy.random.randint(0,4,(20,20))

'''A 30x30 matrix as an example'''
M1= [[3,0,1,0,1,2,3,0,2,1,2,3,0,1,2,3,2,3,1,0,2,3,1,3,0,3,2,1,2,3],
     [1,2,2,2,3,1,2,3,3,2,2,3,1,2,3,2,1,2,0,2,3,0,2,2,3,1,2,0,2,1],
     [2,2,0,3,1,2,1,0,3,1,1,2,3,1,0,2,3,1,2,1,2,0,2,3,1,0,1,2,2,0],
     [3,3,2,3,2,1,3,2,3,0,1,2,3,2,3,0,0,1,2,3,2,1,2,3,0,3,2,3,0,1],
     [0,3,3,1,1,3,2,3,2,0,1,2,3,0,1,2,3,1,0,3,1,2,3,1,0,3,2,1,0,1],
     [2,1,1,3,2,2,3,3,1,1,1,2,3,2,1,2,0,3,2,1,0,3,2,1,0,3,2,3,2,2],
     [2,3,2,0,3,1,0,1,2,0,1,2,1,2,3,1,2,3,1,1,2,0,0,3,1,2,3,1,2,3],
     [3,2,3,2,1,0,3,2,3,2,3,2,2,1,2,0,3,2,1,0,3,1,2,0,3,2,1,0,1,2],
     [0,3,2,3,2,0,2,3,0,0,1,1,3,0,3,2,0,3,2,2,3,1,1,2,3,1,2,1,2,0],
     [1,2,0,1,0,1,2,2,0,3,2,2,3,1,2,3,2,2,2,3,2,0,2,2,2,2,3,2,2,1],
     [0,3,2,2,1,0,2,3,2,2,1,3,2,2,1,2,1,1,1,1,1,2,1,1,2,1,0,3,1,2],
     [1,1,1,3,2,3,2,2,3,3,0,1,1,0,3,1,2,2,0,3,0,1,2,3,3,0,1,1,0,0],
     [2,0,2,2,3,2,2,1,1,0,2,3,1,2,0,3,3,0,3,2,2,2,3,0,3,0,2,3,2,3],
     [3,2,0,1,0,1,2,2,2,1,2,1,2,3,2,1,0,3,0,3,3,0,3,1,2,1,0,0,3,2],
     [2,2,3,2,1,1,2,0,1,2,1,3,2,1,3,2,3,2,0,3,2,3,0,0,1,1,2,1,1,1],
     [1,2,2,0,2,0,2,1,1,3,0,2,1,2,2,0,3,1,0,2,1,1,3,1,1,1,3,2,3,2],
     [3,1,2,1,1,2,3,2,2,2,3,1,3,3,1,3,1,2,1,1,2,2,2,0,2,2,2,2,1,1],
     [2,0,1,2,2,3,2,3,2,1,1,1,1,1,2,2,2,2,1,0,2,3,2,0,3,3,1,1,2,2],
     [1,3,2,0,1,2,1,2,1,3,2,2,0,2,0,1,1,1,2,1,0,1,0,2,0,0,0,0,0,3],
     [0,3,1,1,0,1,0,2,0,2,2,1,3,3,1,2,2,2,3,2,3,2,2,0,2,2,2,2,1,2],
     [1,2,2,2,2,3,2,1,1,0,3,2,1,1,2,3,2,0,0,1,3,2,3,3,1,1,3,1,2,0], 
     [2,1,2,3,3,2,1,3,2,2,2,1,2,2,3,2,3,2,2,3,2,1,0,2,2,2,1,3,0,2], 
     [3,2,1,1,1,1,3,0,3,1,1,1,3,0,1,1,1,3,1,2,0,0,2,2,0,0,3,2,3,3],
     [2,1,3,0,2,0,1,1,0,2,0,2,0,1,1,0,0,3,2,0,3,2,3,2,2,3,0,1,2,1],
     [1,2,0,1,1,2,2,0,1,2,2,3,2,2,2,2,0,1,0,2,2,1,2,0,3,2,2,3,3,3],
     [2,0,1,2,3,3,0,2,2,2,1,2,1,3,0,3,3,3,1,1,1,2,2,2,1,1,1,1,1,1],
     [0,1,0,2,0,1,3,3,3,2,2,0,3,3,2,2,2,2,2,0,0,3,0,1,3,3,2,2,0,2],
     [2,2,1,0,2,2,2,1,1,1,3,2,2,3,3,1,1,3,1,2,2,1,2,2,1,3,3,0,3,2],
     [3,2,3,3,1,3,1,1,2,1,2,1,1,2,2,2,2,2,3,3,2,2,0,0,2,2,0,1,2,3],
     [2,1,1,3,2,0,3,0,3,2,3,2,2,2,2,1,3,1,3,1,3,2,3,2,3,3,1,0,1,2]]


#============================================================================================================#     
'''Making an array of neighbours of an element having coordinates (x,y)'''

'''Counting numbers of neighbours of a particular type'''

def counting(M):
    Rows,Columns = len(M), len(M[0])
    n0 = [[0,]*(Columns)  for i in range(Rows)]
    n1 = [[0,]*(Columns)  for i in range(Rows)]
    n2 = [[0,]*(Columns)  for i in range(Rows)]
    n3 = [[0,]*(Columns)  for i in range(Rows)]
    for x in range(1,Columns-1):
        for y in range(1,Rows-1):
            Neigh=[M[x-1][y-1],M[x][y-1],M[x+1][y-1],M[x-1][y],M[x+1][y],M[x-1][y+1],M[x][y+1],M[x+1][y+1]]
            n0[x][y]=Neigh.count(0)
            n1[x][y]=Neigh.count(1)
            n2[x][y]=Neigh.count(2)
            n3[x][y]=Neigh.count(3) 
            n=[n0,n1,n2,n3]
        for y in range(0,0):
            Neigh=[M[x-1][y],M[x+1][y],M[x-1][y+1],M[x][y+1],M[x+1][y+1]]
            n0[x][y]=Neigh.count(0)
            n1[x][y]=Neigh.count(1)
            n2[x][y]=Neigh.count(2)
            n3[x][y]=Neigh.count(3)
            n=[n0,n1,n2,n3]            
        for y in range(Rows,Rows):
            Neigh=[M[x-1][y-1],M[x][y-1],M[x+1][y-1],M[x-1][y],M[x+1][y]]
            n0[x][y]=Neigh.count(0)
            n1[x][y]=Neigh.count(1)
            n2[x][y]=Neigh.count(2)
            n3[x][y]=Neigh.count(3)
            n=[n0,n1,n2,n3]            
    for y in range(1,Columns-1):
        for x in range(0,0):
            Neigh=[M[x][y-1],M[x+1][y-1],M[x+1][y],M[x][y+1],M[x+1][y+1]]
            n0[x][y]=Neigh.count(0)
            n1[x][y]=Neigh.count(1)
            n2[x][y]=Neigh.count(2)
            n3[x][y]=Neigh.count(3)
            n=[n0,n1,n2,n3]            
        for x in range(Columns,Columns):
            Neigh=[M[x-1][y],M[x-1][y-1],M[x-1][y+1],M[x][y+1],M[x][y-1]]
            n0[x][y]=Neigh.count(0)
            n1[x][y]=Neigh.count(1)
            n2[x][y]=Neigh.count(2)
            n3[x][y]=Neigh.count(3)            
            n=[n0,n1,n2,n3]            
    return n
   
#=========================================================================================================#'''    

'''Bringing in the rules of 'GOL' into the action'''
def conditions(M):
    Rows,Columns = len(M), len(M[0])
    n = counting(M)
    n0=n[0]
    n1=n[1]
    n2=n[2]
    n3=n[3]
    for x in range(0,Rows):
        for y in range(0,Columns):
            if M[x][y]==0 and n1[x][y]>=2:
                M[x][y]=1
            elif M[x][y]==1 and n2[x][y]>=2:
                M[x][y]=2
            elif M[x][y]==2 and n3[x][y]>=2:
                M[x][y]=3
            elif M[x][y]==3 and (n2[x][y]<2 or n3[x][y]<2):
                M[x][y]=0
            elif M[x][y]==2 and (n1[x][y]<2 or n2[x][y]<2):
                M[x][y]=0
            elif M[x][y]==1 and (n1[x][y]<2 or n2[x][y]>=2):
                M[x][y]=0
            elif M[x][y]==2 and (n1[x][y]<2 or n3[x][y]>2):
                M[x][y]=1                    
            elif M[x][y]==0 and n2[x][y]>=2 and n3[x][y]<1:
                M[x][y]=2
            elif M[x][y]==0 and n3[x][y]>=2:
                M[x][y]=3    
    return M

#==============================================================================================================#
'''Creating blank window'''

fig = matplotlib.pyplot.figure()
graph=fig.add_subplot(111)
fig.show()

#===============================================================================================================#

'''Iniating a never ending loop'''

NoEnd=1
while NoEnd>0:
    conditions(M)
    graph.clear()
    graph.imshow(M,interpolation='none', cmap=matplotlib.pyplot.cm.pink_r)
    matplotlib.pyplot.pause(0.2)

#=============================================================================================================#
