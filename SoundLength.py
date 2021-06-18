from makamproject.pitchAnalyse import pitch,pitch_values,sound_file_path
import wave
import contextlib
fname = sound_file_path
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print("Islem Sıklığı..", len(pitch_values)/duration)
def getDuration():
    fname = sound_file_path
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration    