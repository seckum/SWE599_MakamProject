from makamproject_Seckin.pitchAnalyse import pitchCalc
import wave
import contextlib
fname = pitchCalc.sound_file_path
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print("Islem Sıklığı..", len(pitchCalc.pitch_values)/duration)
def getDuration():
    fname = pitchCalc.sound_file_path
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration    