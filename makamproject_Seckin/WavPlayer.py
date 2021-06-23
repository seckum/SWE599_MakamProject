import wx
import gettext
import struct
import matplotlib
matplotlib.use('WX')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import pyaudio
import numpy as np
import time
import sounddevice as sd
import soundfile as sf
from makamproject_Seckin.pitchAnalyse import pitchCalc
from makamproject_Seckin.SoundLength import getDuration
from scipy import signal

# A simple frame with a tab (generated by WxGlade and simplified for example purposes):
class PlayerFrame(wx.Frame):
    dur=getDuration()

    x = pitchCalc.pitch.xs()
    y = pitchCalc.pitch_values

    CHUNK_SIZE = 1024       # Size (in samples) of each audio_callback reading.
    BYTES_PER_FRAME = 2     # Number of bytes in each audio frame.
    CHANNELS = 1            # Number of channels.
    SAMPLING_RATE = 11025   # Audio sampling rate.

    audio_chunks = []
    EVT_PLAYBACK_MOVE = wx.PyEventBinder(wx.NewEventType(), 0)
    def __init__(self, *args, **kwds):
        PlayerFrame.EVT_PLAYBACK_MOVE = wx.PyEventBinder(wx.NewEventType(), 0)
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        print("initializing")
        print("Pitch Values", pitchCalc.pitch_values)
        print("Pitch ", pitchCalc.pitch.xs())
        PlayerFrame.x = pitchCalc.pitch.xs()
        PlayerFrame.y = pitchCalc.pitch_values
        PlayerFrame.main_notebook = wx.Notebook(self, wx.ID_ANY, style=0)
        self.__set_properties()
        self.__do_layout()
        self.initAudio()        # Initiates audio variables and event binding.
        self.initPlotting()     # Initiates plotting variables and widgets.
        self.startPlayback()    # Starts audio playback.
    def __set_properties(self):
        self.SetTitle(("Audio signal plotting and playback with cursor"))
        self.SetSize((800, 900))
    def __do_layout(self):
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_main.Add(PlayerFrame.main_notebook, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 25)
        self.SetSizer(sizer_main)
        self.Layout()


    # Audio stuff initialization:
    def initAudio(self):
        # Binds the playback move event to a handler:
        self.Bind(PlayerFrame.EVT_PLAYBACK_MOVE, PlayerFrame.OnPlaybackMove)
        # Creates an empty audio chunk with "CHUNK_SIZE" samples of zero value ([0, 0, ..., 0, 0]):
        empty_chunk = struct.pack("<h", 0)*PlayerFrame.CHUNK_SIZE
        # Initializes audio chunk array with 20 empty audio chunks:
        print("initializing Audio")
        #snd = parselmouth.Sound(r"C:\Users\hp\Downloads\01enver_bususs_.wav")
        data, fs = sf.read(pitchCalc.sound_file_path, dtype='float32')
        PlayerFrame.audio_chunks.extend([empty_chunk]*int(PlayerFrame.dur*14.5))
        print("audio_chunck: ", len(PlayerFrame.audio_chunks))
        print("empty_chunck: ", len(empty_chunk))
        print("duration: ", PlayerFrame.dur)

        sd.play(data, fs)

        # Points playback_counter to the first audio chunk:
        global playback_counter; playback_counter = 0

    def startPlayback(self):
        # Initializes audio playback:
        global p; p = pyaudio.PyAudio()
        print("initializing Start")
        global audio_stream; audio_stream = p.open  ( format = p.get_format_from_width(PlayerFrame.BYTES_PER_FRAME)
                                                    , channels = PlayerFrame.CHANNELS
                                                    , rate = PlayerFrame.SAMPLING_RATE
                                                    , output = True
                                                    , stream_callback = PlaybackMoveEvent.audio_callback
                                                    , frames_per_buffer = PlayerFrame.CHUNK_SIZE )

    # Plotting stuff initialization:
    def initPlotting(self):
        # Converts the raw audio chunks to a normal array:
        samples = np.fromstring(b''.join(PlayerFrame.audio_chunks), dtype=np.int16)
        print("initializing plotting")
        # Creates plot supporting widgets:
        PlayerFrame.pane = wx.Panel(PlayerFrame.main_notebook, wx.ID_ANY)
        PlayerFrame.canvas = FigureCanvas(PlayerFrame.pane, wx.ID_ANY, Figure())
        PlayerFrame.figure = PlayerFrame.canvas.figure
        PlayerFrame.pane.SetMinSize((750, 420))
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10.Add(PlayerFrame.canvas, 1, wx.EXPAND, 0)
        sizer_16.Add(sizer_10, 2, wx.BOTTOM | wx.EXPAND, 25)
        sizer_15.Add(sizer_16, 1, wx.ALL | wx.EXPAND, 25)
        PlayerFrame.pane.SetSizer(sizer_15)
        PlayerFrame.main_notebook.AddPage(PlayerFrame.pane, (pitchCalc.sound_file_path))

        t = range(len(samples))
        print("t: ", t)
        PlayerFrame.axes1 = PlayerFrame.figure.add_subplot(211)
        PlayerFrame.axes1.set_xlim(0, len(samples))
        PlayerFrame.axes1.set_ylim(0, pitchCalc.pitch.ceiling)
        print("y",PlayerFrame.y)
        print("len(samples)",len(samples))
        f = signal.resample(PlayerFrame.y, len(samples))
        PlayerFrame.line1 = PlayerFrame.axes1.plot(t, f)
        #self.axes2=self.figure.add_subplot(212)
        #self.line1 = self.axes2.plot(x, y)
        self.Layout()
        PlayerFrame.figure.canvas.draw()
        PlayerFrame.background = PlayerFrame.figure.canvas.copy_from_bbox(self.axes1.bbox)
        PlayerFrame.playback_line = PlayerFrame.axes1.axvline(color="y", animated=True)
    # For each new chunk read by the audio_callback function, we update the cursor position on the plot.
    # It's important to notice that the audio_callback function CANNOT manipulate UI's widgets on it's
    # own, because they live in different threads and Wx allows only the main thread to perform UI changes.
    def OnPlaybackMove(self):
        # =================================================
        # Updates the cursor (vertical line) at each event:
        # =================================================
        PlayerFrame.figure.canvas.restore_region(PlayerFrame.background)
        new_position = playback_counter*PlayerFrame.CHUNK_SIZE
        PlayerFrame.playback_line.set_xdata(new_position)
        PlayerFrame.axes1.draw_artist(PlayerFrame.playback_line)
        PlayerFrame.canvas.blit(PlayerFrame.axes1.bbox)

# Playback move event (for indicating that a chunk has just been played and so the cursor must be moved):

class PlaybackMoveEvent(wx.PyCommandEvent):
    def __init__(self, eventType=PlayerFrame.EVT_PLAYBACK_MOVE.evtType[0], id=0):
        wx.PyCommandEvent.__init__(self, PlayerFrame.EVT_PLAYBACK_MOVE.evtType[0], id)

    # Callback function for audio playback (called each time the sound card needs "frame_count" more samples):
    def audio_callback(afd,b,c,d):
        global playback_counter
        # In case we've run out of samples:
        if playback_counter == len(PlayerFrame.audio_chunks):
            print("Playback ended.")
            # Returns an empty chunk, thus ending playback:
            return ("", pyaudio.paComplete)
        else:
            # Gets the next audio chunk, increments the counter and returns the new chunk:
            new_chunk = PlayerFrame.audio_chunks[playback_counter]
            PlaybackMoveEvent.main_window.AddPendingEvent(PlaybackMoveEvent())
            playback_counter += 1
            return (new_chunk, pyaudio.paContinue)

    def start(a):
        gettext.install("app")
        app = wx.PySimpleApp(0)
        wx.InitAllImageHandlers()
        PlaybackMoveEvent.main_window = PlayerFrame(None, wx.ID_ANY, "")
        app.SetTopWindow(PlaybackMoveEvent.main_window)
        PlaybackMoveEvent.main_window.Show()
        app.MainLoop()  # UI's main loop. Checks for events and stuff.
        # Final lines (if we're executing here, this means the program is closing):
        audio_stream.close()
        p.terminate()

    def stop(a):
        sd.stop()
