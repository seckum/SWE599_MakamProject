from makamproject_Seckin.histogramAnalyse import HistAnalyse
from makamproject_Seckin.pitchAnalyse    import pitchCalc
from makamproject_Seckin.TeoricFileRead  import getMakam

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
global makamName1

class selectMakamUser:
    makamName1="asd"
    print("Seçilen Makam ", makamName1)
    makamName2="asd2"
    print("Seçilen Makam2 ", makamName2)
    makamName3="asd3"
    print("Seçilen Makam3 ", makamName3)
    
    def getmakamID():
        print("******getmakamID'ye girdi*******")
        IDlist=[]    
        templatenames =getMakam.getTemplateNames()
        ind_1 = templatenames.index(selectMakamUser.makamName1)
        IDlist.append(ind_1)
        ind_2 = templatenames.index(selectMakamUser.makamName2)
        IDlist.append(ind_2)
        ind_3 = templatenames.index(selectMakamUser.makamName3)
        IDlist.append(ind_3)
        print("ID List--------->",IDlist)
        return IDlist

    def plotSelect():
        print("******plotSelect girdi*******")
        xarray=[]
        xarrayzero=[]
        peakhistdata=[]
        peakshistogram = getMakam.getDataHist()
        for i in range(len(peakshistogram)):
            peakhistdata.append(float(peakshistogram[i]))
            xarray.append(i)
        max_value = max(peakhistdata) 
        print("max_value----->", max_value)    
        shiftAmount = peakhistdata.index(max_value)
        print("shiftAmount----->",shiftAmount)    
        for x in range(len(xarray)):
            xarrayzero.append(xarray[x]-shiftAmount)
        
        xaxis=xarrayzero
        yaxis=getMakam.getDataHist()
        templates=getMakam.initTemplates()
        makamID=selectMakamUser.getmakamID()
        xaxis1=templates[makamID[0]]
        xaxis2=templates[makamID[1]]
        xaxis3=templates[makamID[2]]
        #User Selected Makam
        print("xaxis1***  ", xaxis1)
        print("xaxis1***  ", xaxis2)
        print("xaxis1***  ", xaxis3)
        yarray1=np.full((1,len(xaxis1)),12000)
        yarray2=np.full((1,len(xaxis2)),14000)
        yarray3=np.full((1,len(xaxis3)),16000)

        print("yarray1********", yarray1)
        print("yarray2********", yarray2)
        print("yarray3********", yarray3)
        plt.figure(4)
        plt.xlim(-200,800)
        plt.xticks(np.arange(-200,800,step=20),rotation=90, fontsize=6) 
        plt.plot(xaxis,yaxis,color="blue")    
        plt.scatter(xaxis1,yarray1,color='green')  
        plt.scatter(xaxis2,yarray2,color="red")
        plt.scatter(xaxis3, yarray3, color="indigo")
        plt.legend(('Histogram','Teorik Makam 1: ' + selectMakamUser.makamName1,
        'Teorik Makam 2: '+ selectMakamUser.makamName2,
        'Teorik Makam 3: '+ selectMakamUser.makamName3),fontsize=8,loc='upper left')
        for p in xaxis3:
            plt.axvline(p,ymax=16000,linestyle="--")
        plt.title("Makam&Histogram Analizi")
        #plt.axvline(makampoints, 0, 0.8, color='green', label='plot a green vertical line')
        
        plt.show()

    def start():
        #counter=0
        print("Start******* ")
        #selectMakamUser.getmakamID()
        selectMakamUser.plotSelect()
            