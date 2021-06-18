import os
import sys
from makamproject.GetUserInputMakam import UserDefinedMakam
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import EllipseSelector, Cursor, Button
from makamproject.histogramAnalyse import getHistData,getHistDataNorm, createNormHistData, getTonicIndexNorm, getTonicPeakPointNorm
from makamproject.histogramAnalyseSelected import getHistDataNormSelected,getHistDataSelected,createNormHistDataSelected
from makamproject.GetMakam import setmakamtemplates,measure,sortAndPick,getMakamNameArray
from makamproject.GetUserInputMakam import setmakamtemplatesUser,UserDefinedMakam
from makamproject.pitchAnalyse import pitch
pitch=pitch
tonic = getTonicIndexNorm()
ytonic=getTonicPeakPointNorm()
indexNum = sortAndPick()
makamnames = getMakamNameArray()
showmakamname = makamnames[indexNum]

ArrayChose=setmakamtemplates()
TeoricHist =ArrayChose[indexNum]
SoundHistNorm = getHistDataNorm()
SoundHist= getHistData()
#print("Teoric", TeoricHist[:5])
EditedSound=createNormHistData(TeoricHist)
#print("Edited",EditedSound[:5])

SoundHistSelectedNorm=getHistDataNormSelected()
makamNumber = UserDefinedMakam()
print("makamNumber: ", makamNumber)
ArrayUser=setmakamtemplatesUser()
#print("ArrayUser: ", ArrayUser)
UserSelected=ArrayUser[makamNumber]
#print("UserSelected ",UserSelected)
UserSelectedEdited=createNormHistData(UserSelected)
showusermakamname=makamnames[makamNumber]

plt.xlabel('Frequency(Cent)')
plt.ylabel('Frequency of Occurence')
plt.plot(EditedSound)
plt.plot(SoundHistNorm)
plt.plot(SoundHistSelectedNorm*20)
plt.plot(UserSelectedEdited)
plt.annotate("Tonic_Input_File "+str(tonic)+"Cent", (tonic,ytonic), arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend(('Teoric '+ showmakamname,'SoundHistNorm','SelectedPortion','UserSelectedMakam '+showusermakamname),loc='upper left')
plt.xlim(300,400)
plt.xticks(np.arange(300,400,step=2),rotation=45, fontsize=8)
plt.show()

def draw_pitch(pitch):
    pitch_values = pitch.selected_array['frequency']
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("fundamental frequency [Hz]")
    plt.plot(pitch.xs(),pitch_values)

#draw_pitch(pitch)
#plt.show()