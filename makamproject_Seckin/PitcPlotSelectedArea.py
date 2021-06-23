import numpy as np
from matplotlib import use
use('WXAgg')
from matplotlib import pyplot as plt
import wx
from matplotlib.widgets import SpanSelector , Cursor , Button
from makamproject_Seckin.pitchAnalyse import pitchCalc
import parselmouth

class AreaPlot:    
    xarray=[]
    yarray=[]
    x = 0
    y = 0
    
    def initGraph():
        AreaPlot.initGraph.fig1 = plt.figure(1,figsize=(9, 8))
        AreaPlot.initGraph.ax = AreaPlot.initGraph.fig1.add_subplot(211)
        snd = parselmouth.Sound(pitchCalc.sound_file_path)
        pitchCalc.pitch = snd.to_pitch_ac(0.0001)
        pitchCalc.pitch_values = pitchCalc.pitch.selected_array['frequency']
        AreaPlot.x = pitchCalc.pitch.xs()
        AreaPlot.y = pitchCalc.pitch_values
        AreaPlot.initGraph.ax.plot(AreaPlot.x, AreaPlot.y, '-')
        #ax.set_ylim(0, 1000)
        AreaPlot.initGraph.ax.set_title('Press left mouse button and drag to test')
        plt.ylabel('Fundemental Frequency(Hz)')
        AreaPlot.initGraph.ax2 = AreaPlot.initGraph.fig1.add_subplot(212)
        AreaPlot.initGraph.line2, = AreaPlot.initGraph.ax2.plot(AreaPlot.x, AreaPlot.y, '-')
        AreaPlot.initGraph.ax2.set_title('Zoom Area')
        plt.xlabel('time(s)')
        plt.ylabel('Fundemental Frequency(Hz)')
       

    def onselect(xmin, xmax):
        indmin, indmax = np.searchsorted(AreaPlot.x, (xmin, xmax))
        indmax = min(len(AreaPlot.x) - 1, indmax)
        thisx = AreaPlot.x[indmin:indmax]
        thisy = AreaPlot.y[indmin:indmax]
        AreaPlot.initGraph.line2.set_data(thisx, thisy)
        AreaPlot.initGraph.ax2.set_xlim(thisx[0], thisx[-1])
        AreaPlot.initGraph.ax2.set_ylim(thisy.min(), thisy.max())
        AreaPlot.initGraph.fig1.canvas.draw_idle()
        
        # save
        np.savetxt("text.out", np.c_[thisx, thisy])

    def onclick(event):
        x2,y2=event.xdata, event.ydata
        print(x2,y2)
        AreaPlot.xarray.append(x2)
        AreaPlot.yarray.append(y2)
        if len(AreaPlot.xarray)>5 :
            print("You reached the maximum number of point")
            np.savetxt("XYcoordinates.txt", (AreaPlot.xarray,AreaPlot.yarray),fmt='%s')

    def cursorspan():
        print("Entered Cursor")
        AreaPlot.cursorspan.cursor = Cursor(AreaPlot.initGraph.ax2, useblit=True, color='red', linewidth=2)
        AreaPlot.initGraph.fig1.canvas.mpl_connect('button_press_event',AreaPlot.onclick)   
        AreaPlot.cursorspan.span = SpanSelector(AreaPlot.initGraph.ax, AreaPlot.onselect, 'horizontal', useblit=True,
                            rectprops=dict(alpha=0.5, facecolor='red'))
        plt.show()
    def start():
        AreaPlot.initGraph()
        AreaPlot.cursorspan()