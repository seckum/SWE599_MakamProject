import os
import sys
from makamproject.pitchAnalyse import getPitchValues
import statistics
import numpy as np
import math

pitch_values = getPitchValues()
dataArray=[]

def normalizeSum(ar):
    summ = float(0)
    for i in range(len(ar)):
     summ = summ+ar[i]
    for i in range(len(ar)):
     ar[i] = ar[i]/summ 
    return ar 

def normalizeMax(ar):
	maximum = float(0)
	temp=np.zeros(len(ar),dtype=float)
	temp =ar.copy()
	temp.sort()
	maximum =temp[len(temp)-1]
	norm=[]
	for i in range(len(ar)):
		norm.append(ar[i]/maximum)
	return norm	

def smootizee(ar, rang):
    temp = np.empty(len(ar), dtype=float)
    #print("temp array_smootize...",temp)
    #print("ar..",ar,"  rang  ",rang)
    for i in range(rang,len(ar)-rang):
        temp[i] = 0
        for j in  range(-1*rang , rang+1):
            temp[i]=temp[i]+ar[i+j]
        temp[i] = temp[i]/(2*rang+1)
    for i in range(rang):
        temp[i] = ar[i]
        temp[len(temp)-1-i] = ar[len(ar)-1-i]
    return temp 


def herzToCent(array):
        ref_freq = float(8.17579892*2) 
        centdata=[]
        for i in range(len(array)):
         centdata.append(round(1200*math.log2(array[i]/ref_freq)))
        dataArray=centdata 
        return dataArray

def createHistData(pitch_values):
    for y in pitch_values:
        if float(y)>0:
            dataArray.append(float(y))
    dataArray.sort()
    tempar=herzToCent(dataArray)
    medianCent =statistics.median(tempar)
    minCent= medianCent - 2400
    maxCent= medianCent + 2400
    commaCent =1200.0/159.0
    histData=np.zeros(round((maxCent-minCent)/commaCent),dtype=float)
    for i in range(len(tempar)): 
       if  tempar[i]>=minCent and tempar[i]<maxCent :
           histData[int((dataArray[i]-minCent)/commaCent)]=histData[int((dataArray[i]-minCent)/commaCent)]+1
    #np.savetxt("histo.txt", histData, fmt="%s")
    return histData
def getHistData():
    histData=createHistData(pitch_values)
    return histData

def createNormHistData(pitch_values):
    for y in pitch_values:
        if float(y)>0:
            dataArray.append(float(y))
    dataArray.sort()
    tempar=herzToCent(dataArray)
    tempnorm= normalizeMax(tempar)
    tempsum = normalizeSum(tempnorm)
    medianCent =statistics.median(tempsum)
    minCent= medianCent - 2400
    maxCent= medianCent + 2400
    commaCent =1200.0/159.0
    histDataNorm=np.zeros(round((maxCent-minCent)/commaCent),dtype=float)
    for i in range(len(tempsum)): 
       if  tempsum[i]>=minCent and tempsum[i]<maxCent :
           histDataNorm[int((dataArray[i]-minCent)/commaCent)]=histDataNorm[int((dataArray[i]-minCent)/commaCent)]+1
    #np.savetxt("histo.txt", histData, fmt="%s
    return histDataNorm

def getHistDataNorm():
    histDataNorm=createNormHistData(pitch_values)
    return histDataNorm

def getTonicIndexNorm():
    histDataNorm=createNormHistData(pitch_values)
    tonicNorm=np.argmax(histDataNorm)
    return tonicNorm

def getTonicPeakPointNorm():
    histDataNorm=createNormHistData(pitch_values)
    tonicNorm=np.argmax(histDataNorm)
    maxpeakNorm=histDataNorm[tonicNorm]
    return maxpeakNorm


