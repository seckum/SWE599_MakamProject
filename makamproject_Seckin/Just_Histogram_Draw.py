from makamproject_Seckin.histogramAnalyse import HistAnalyse
from makamproject_Seckin.pitchAnalyse    import pitchCalc
from makamproject_Seckin.TeoricFileRead  import getMakam
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
global makamName1

class selectMakam:
    makamName1="asd"
    print("Seçilen Makam ", makamName1)
    makamName2="asd2"
    print("Seçilen Makam2 ", makamName2)
    makamName3="asd3"
    print("Seçilen Makam3 ", makamName3)

    def plotSelect():
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
        #User Selected Makam
        
        #yarray1=np.full((1,len(shiftedpeaks)),900)
        #yarray2=np.full((1,len(shiftedpeaks)),1200)
        #yarray3=np.full((1,len(shiftedpeaks)),1400)

        plt.figure(2)
        plt.xlim(-200,800)
        plt.xticks(np.arange(-200,800,step=20),rotation=90, fontsize=6) 
        plt.plot(xaxis,yaxis,color="blue")    
        #plt.scatter(xaxis,yarray1,color='green')  
        #plt.scatter(xaxis,yarray2,color="red")
        #plt.stem(xaxis, yarray3)
        plt.legend(('Histogram','Teorik Makam 1','Teorik Makam 2','Teorik Makam 3 '),fontsize=8,loc='upper left')
        plt.title("Histogram Analizi")
        #plt.axvline(makampoints, 0, 0.8, color='green', label='plot a green vertical line')
        
        plt.show()    


