import numpy as np
from numpy.lib.function_base import append
import parselmouth
import matplotlib.pyplot as plt
from pydub import AudioSegment
#AudioSegment.converter = "C:\\PATH_programs\\ffmpeg.exe"
#AudioSegment.ffmpeg = "C:\\PATH_programs\\ffmpeg.exe"
#AudioSegment.ffprobe ="C:\\PATH_programs\\ffprobe.exe"
import seaborn as sns
import statistics
import math
import sys
import os
import pandas as pd
global sound_file_path;

#Checks and converts mp3 format to wav
class pitchCalc:
    sound_file_path ='newproject/Data/01bekir_dughic_.wav' #Global Sound Path
    pitch_values=[]
    snd = parselmouth.Sound(sound_file_path)
    pitch = snd.to_pitch_ac(0.0001)
    def checkExtension(a):
        if pitchCalc.sound_file_path.endswith(("mp3")):
            sound = AudioSegment.from_mp3(pitchCalc.sound_file_path)
            sound.export('newproject/Data/deneme.wav', format="wav")
            sound_file_path='newproject/Data/deneme.wav'
      
    def getPitchValues(a):
        return pitchCalc.pitch_values
    #print("pitch values ", pitch_values)
    def calculatePitch(a):
        dummy=[]
        snd = parselmouth.Sound(pitchCalc.sound_file_path)
        pitch = snd.to_pitch_ac(0.0001)
        pitch_values = pitch.selected_array['frequency']
        for i in range(len(pitch_values)):
            if pitch_values[i]>0:
                dummy.append(pitch_values[i])
        np.savetxt("pitchvalues.txt", dummy, fmt="%s")
        
        return pitch_values
    #pitch = snd.to_pitch()
