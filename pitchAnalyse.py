import numpy as np
from numpy.lib.function_base import append
import parselmouth
import matplotlib.pyplot as plt
from pydub import AudioSegment
AudioSegment.converter = "C:\\PATH_programs\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\PATH_programs\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\PATH_programs\\ffprobe.exe"
import seaborn as sns
import statistics
import math
import sys
import os
global sound_file_path
sound_file_path = 'newproject/Data/06bekir_nevhic_.wav' #Global Sound Path

#Checks and converts mp3 format to wav
if sound_file_path.endswith(("mp3")):
    sound = AudioSegment.from_mp3(sound_file_path)
    sound.export('newproject/Data/deneme.wav', format="wav")
    sound_file_path='newproject/Data/deneme.wav'


snd = parselmouth.Sound(sound_file_path)
pitch = snd.to_pitch_ac(0.003)
pitch_values = pitch.selected_array['frequency']

def getPitchValues():
    return pitch_values
#print("pitch values ", pitch_values)
def calculatePitch(pitch):
    # Extract selected pitch contour
    pitch_values = pitch.selected_array['frequency']
    np.savetxt("pitchvalues.txt", pitch_values, fmt="%s")
    return pitch_values
#pitch = snd.to_pitch()
#calculatePitch(pitch) 