import sys
import os
import numpy
from makamproject.hertzToCent import hertztocent
from makamproject.histogramAnalyse import getHistDataNorm

tempLen=3272
histLen=636
distArray =numpy.zeros((45,tempLen-histLen+1),dtype=float)
indexes =[]
longHist=numpy.zeros(tempLen,dtype=float)
templates=[]
shiftAmount=0
templatenames=["acem","acemasiran","bestenigar",
"beyat,","beyatiraban","buselik","dugah","evcera","evic",
"ferahfeza","ferahnak","gulizar","hicaz","hicazkar","huseyni",
"huzzam","irak","isfahan","karcigar","kurdi","kurdilihicazkar","mahur",
"muhayyer","mustear","neva","neveser","nihavend","nikriz","niaburek","nuhuft",
"pencgah","pesendide","rast","saba","sedaraban","segah","sehnaz","sevkefza",
"sultaniyegah","suzidil","suzinak","tahir","tahirbuselik","ussak","yegah"]
histo = []
#temphistogram = open(r'C:\Users\Seckin\Desktop\SWE_Project_3_6\histo.txt')
temphistogram = getHistDataNorm()

def setmakamtemplates():
        dataArray1 = []
        dataArray2 = []
        dataArray3 = []
        dataArray4 = []
        dataArray5 = []
        dataArray6 = []
        dataArray7 = []
        dataArray8 = []
        dataArray9 = []
        dataArray10 = []
        dataArray11 = []
        dataArray12 = []
        dataArray13 = []
        dataArray14 = []
        dataArray15 = []
        dataArray16= []
        dataArray17 = []
        dataArray18 = []
        dataArray19 = []
        dataArray20 = []
        dataArray21 = []
        dataArray22 = []
        dataArray23 = []
        dataArray24 = []
        dataArray25 = []
        dataArray26 = []
        dataArray27 = []
        dataArray28 = []
        dataArray29 = []
        dataArray30 = []
        dataArray31 = []
        dataArray32 = []
        dataArray33 = []
        dataArray34 = []
        dataArray35 = []
        dataArray36 = []
        dataArray37 = []
        dataArray38 = []
        dataArray39 = []
        dataArray40 = []
        dataArray41 = []
        dataArray42 = []
        dataArray43 = []
        dataArray44 = []
        dataArray45 = []
        
        
        dataArrayst = open('newproject/Data/acem.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0: 
                dataArray1.append(float(y))
      
        dataArrayst = open('newproject/Data/acemasiran.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 : 
                dataArray2.append(float(y)) 
        
        dataArrayst = open('newproject/Data/bestenigar.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray3.append(float(y)) 

        dataArrayst = open('newproject/Data/beyati.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 : 
                dataArray4.append(float(y)) 

        dataArrayst = open('newproject/Data/beyatiaraban.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray5.append(float(y))
        
        dataArrayst = open('newproject/Data/buselik.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray6.append(float(y))

        dataArrayst = open('newproject/Data/dugah.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray7.append(float(y))

        dataArrayst = open('newproject/Data/evcara.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray8.append(float(y))        
        
        dataArrayst = open('newproject/Data/evic.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray9.append(float(y)) 

        dataArrayst = open('newproject/Data/ferahfeza.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray10.append(float(y))

        dataArrayst = open('newproject/Data/ferahnak.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray11.append(float(y))        

        dataArrayst = open('newproject/Data/gulizar.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray12.append(float(y))

        dataArrayst = open('newproject/Data/hicaz.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray13.append(float(y))

        dataArrayst = open('newproject/Data/hicazkar.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray14.append(float(y))

        dataArrayst = open('newproject/Data/huseyni.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray15.append(float(y))

        dataArrayst = open('newproject/Data/huzzam.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray16.append(float(y)) 

        dataArrayst = open('newproject/Data/irak.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray17.append(float(y))

        dataArrayst = open('newproject/Data/isfahan.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray18.append(float(y))

        dataArrayst = open('newproject/Data/karcigar.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray19.append(float(y))        

        dataArrayst = open('newproject/Data/kurdi.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray20.append(float(y))   

        dataArrayst = open('newproject/Data/kurdilihicazkar.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray21.append(float(y))  

        dataArrayst = open('newproject/Data/mahur.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray22.append(float(y)) 

        dataArrayst = open('newproject/Data/muhayyer.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray23.append(float(y))

        dataArrayst = open('newproject/Data/mustear.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray24.append(float(y))

        dataArrayst = open('newproject/Data/neva.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray25.append(float(y))

        dataArrayst = open('newproject/Data/neveser.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray26.append(float(y))

        dataArrayst = open('newproject/Data/nihavend.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray27.append(float(y))

        dataArrayst = open('newproject/Data/nikriz.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray28.append(float(y))

        dataArrayst = open('newproject/Data/nisaburek.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray29.append(float(y))

        dataArrayst = open('newproject/Data/nuhuft.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray30.append(float(y))

        dataArrayst = open('newproject/Data/pencgah.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray31.append(float(y))

        dataArrayst = open('newproject/Data/pesendide.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray32.append(float(y))

        dataArrayst = open('newproject/Data/rast.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray33.append(float(y))

        dataArrayst = open('newproject/Data/saba.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray34.append(float(y))

        dataArrayst = open('newproject/Data/sedaraban.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray35.append(float(y))  

        dataArrayst = open('newproject/Data/segah.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray36.append(float(y)) 

        dataArrayst = open('newproject/Data/sehnaz.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray37.append(float(y))    

        dataArrayst = open('newproject/Data/sevkefza.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray38.append(float(y)) 

        dataArrayst = open('newproject/Data/sultaniyegah.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray39.append(float(y)) 

        dataArrayst = open('newproject/Data/suzidil.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray40.append(float(y)) 

        dataArrayst = open('newproject/Data/suzinak.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray41.append(float(y))

        dataArrayst = open('newproject/Data/tahir.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray42.append(float(y))

        dataArrayst = open('newproject/Data/tahirbuselik.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray43.append(float(y))

        dataArrayst = open('newproject/Data/ussak.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray44.append(float(y)) 

        dataArrayst = open('newproject/Data/yegah.txt')
        for y in dataArrayst.readlines():
            if float(y)>0.0 :
                dataArray45.append(float(y)) 

        templates.append(dataArray1)
    
        templates.append(dataArray2)
        
        templates.append(dataArray3)
       
        templates.append(dataArray4)
        
        templates.append(dataArray5)

        templates.append(dataArray6)
    
        templates.append(dataArray7)
        
        templates.append(dataArray8)
       
        templates.append(dataArray9)
        
        templates.append(dataArray10)

        templates.append(dataArray11)
    
        templates.append(dataArray12)
        
        templates.append(dataArray13)
       
        templates.append(dataArray14)
        
        templates.append(dataArray15)
        
        templates.append(dataArray16)
    
        templates.append(dataArray17)
        
        templates.append(dataArray18)
       
        templates.append(dataArray19)
        
        templates.append(dataArray20)

        templates.append(dataArray21)
    
        templates.append(dataArray22)
        
        templates.append(dataArray23)
       
        templates.append(dataArray24)
        
        templates.append(dataArray25)

        templates.append(dataArray26)
    
        templates.append(dataArray27)
        
        templates.append(dataArray28)
       
        templates.append(dataArray29)
        
        templates.append(dataArray30)

        templates.append(dataArray31)
    
        templates.append(dataArray32)
        
        templates.append(dataArray33)
       
        templates.append(dataArray34)
        
        templates.append(dataArray35)
        
        templates.append(dataArray36)
    
        templates.append(dataArray37)
        
        templates.append(dataArray38)
       
        templates.append(dataArray39)
        
        templates.append(dataArray40)

        templates.append(dataArray41)
    
        templates.append(dataArray42)
        
        templates.append(dataArray43)
       
        templates.append(dataArray44)
        
        templates.append(dataArray45)

        return templates


def reFill(j) :
        longHist = numpy.empty(tempLen, dtype=float)
        
        for i in range(len(histo)):
            #i hep 0 dönüyor incelenmesi gerekli...
            longHist[j+i]= histo[i]
        

def L1distance(p1,p2):
        sum =float(0.0)  
        for i in range(len(p1)):
            sum = sum +(p1[i]-p2[i])
        
        return sum    

def getDistanceArray():
        return distArray

def createDistanceArray():
        
        for i in range(5):
            for j in range(tempLen - histLen+1):
                reFill(j)
                distArray[i][j]= L1distance(templates[i],longHist) 
         
def sortAndPick():
        value = 0
        values =[]
        print("Distarray boyutu= ",len(distArray))
        for i in range(len(distArray)):
            value=float(min(distArray[i]))
            values.append(value)
            print(values)
            #indexes[i] = distArray[i][value]
        ind=values.index(min(values))
        
        makamName = templatenames[ind]
        print("Tahmin edilen Makam...", makamName)
        print("indexxxx....",ind)
        return ind
         


def reCompute(tonInd, offset ):
        sub = histo[tonInd-offset : tonInd + offset]
        add = -1
        maxN = -1
        for i in range(len(sub)) :
            if sub[i]> maxN :
                maxN = sub[i]
                add = i
        tonicIndex =(tonInd+add-offset)
        return tonicIndex         

def readHisto():
        for y in temphistogram:
            histo.append(float(y))

def smootizee(ar, rang):
    temp = numpy.empty(len(ar), dtype=float)
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
def getMakamNameArray():
    return templatenames

def measure() :
        readHisto()
        setmakamtemplates()
        createDistanceArray()
        sortAndPick()
        #computeTonic()
        #reFill(shiftAmount)
        #calcPeaks(getShiftHistogram())

measure()
 
        
        
    
            
    
