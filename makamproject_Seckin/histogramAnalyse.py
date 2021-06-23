import os
import sys
from makamproject_Seckin.pitchAnalyse import pitchCalc
import statistics
import numpy as np
import math
class HistAnalyse:
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
                HistAnalyse.dataArray.append(float(y))
        HistAnalyse.dataArray.sort()
        tempar=HistAnalyse.herzToCent(HistAnalyse.dataArray)
        medianCent =statistics.median(tempar)
        minCent= medianCent - 4800
        maxCent= medianCent + 4800
        commaCent =1200.0/159.0
        histData=np.zeros(round((maxCent-minCent)),dtype=float)
        for i in range(len(tempar)): 
            if  tempar[i]>=minCent and tempar[i]<maxCent :
                histData[int((HistAnalyse.dataArray[i]-minCent))]=histData[int((HistAnalyse.dataArray[i]-minCent))]+1
        np.savetxt("histoxx.txt", histData, fmt="%s")
        return histData
    def getHistData():
        histData=HistAnalyse.createHistData(HistAnalyse.pitch_values)
        return histData

    def createNormHistData(pitch_values):
        for y in pitch_values:
            if float(y)>0:
                HistAnalyse.dataArray.append(float(y))
        HistAnalyse.dataArray.sort()
        tempar=HistAnalyse.herzToCent(HistAnalyse.dataArray)
        np.savetxt("temparraynew.txt", tempar, fmt="%s")
        #tempnorm= HistAnalyse.normalizeMax(tempar)
        #tempsum = HistAnalyse.normalizeSum(tempnorm)
        medianCent =statistics.median(tempar)
        print("median cent...",medianCent)
        minCent= medianCent - 9600
        maxCent= medianCent + 9600
        commaCent =1200.0/159.0
        histDataNorm=np.zeros(round((maxCent-minCent)),dtype=float)
        for i in range(len(tempar)): 
            if  tempar[i]>=minCent and tempar[i]<maxCent :
                histDataNorm[int(tempar[i]-minCent)]=histDataNorm[int(tempar[i]-minCent)]+1
        np.savetxt("histonew.txt", histDataNorm, fmt="%s")
        print(len(histDataNorm))
        return histDataNorm

    def getHistDataNorm():
        pitch_values = pitchCalc.pitch_values
        print("pitch_values_gethistData",pitch_values)
        histDataNorm=HistAnalyse.createNormHistData(pitch_values)
        print("histdataNorm",histDataNorm)
        return histDataNorm

    def getTonicIndexNorm():
        histDataNorm=HistAnalyse.createNormHistData(HistAnalyse.pitch_values)
        tonicNorm=np.argmax(histDataNorm)
        return tonicNorm

    def getTonicPeakPointNorm():
        histDataNorm=HistAnalyse.createNormHistData(HistAnalyse.pitch_values)
        tonicNorm=np.argmax(histDataNorm)
        maxpeakNorm=histDataNorm[tonicNorm]
        return maxpeakNorm

    def getShiftedHistogram():
        shiftAmount=HistAnalyse.getTonicIndexNorm()
        initHistData=HistAnalyse.createNormHistData(HistAnalyse.pitch_values)
        shiftedHist=[]
        Xaxis=[]
        for y in range(len(initHistData)):
            Xaxis.append(y)
        print("x ax", Xaxis[:5])    
        for i in range(len(Xaxis)):
            shifted=int(Xaxis[i]-shiftAmount)
            shiftedHist.append(shifted)
        print("x axshifted", shiftedHist[:5])     
        print("shiftedHist Created")    
        return shiftedHist    
    