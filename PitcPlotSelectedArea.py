import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector , Cursor , Button
from makamproject.pitchAnalyse import pitch,pitch_values

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(211)

x = pitch.xs()
y = pitch_values

ax.plot(x, y, '-')
#ax.set_ylim(0, 1000)
ax.set_title('Press left mouse button and drag to test')
plt.ylabel('Fundemental Frequency(Hz)')


ax2 = fig.add_subplot(212)
line2, = ax2.plot(x, y, '-')
ax2.set_title('Zoom Area')
plt.xlabel('time(s)')
plt.ylabel('Fundemental Frequency(Hz)')
xarray=[]
yarray=[]

def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(x, (xmin, xmax))
    indmax = min(len(x) - 1, indmax)

    thisx = x[indmin:indmax]
    thisy = y[indmin:indmax]
    line2.set_data(thisx, thisy)
    ax2.set_xlim(thisx[0], thisx[-1])
    ax2.set_ylim(thisy.min(), thisy.max())
    
    fig.canvas.draw_idle()
    
    # save
    np.savetxt("text.out", np.c_[thisx, thisy])

def onclick(event):
    x2,y2=event.xdata, event.ydata
    print(x2,y2)
    xarray.append(x2)
    yarray.append(y2)
    if len(xarray)>5 :
        print("You reached the maximum number of point")
        np.savetxt("XYcoordinates.txt", (xarray,yarray),fmt='%s')

cursor = Cursor(ax2, useblit=True, color='red', linewidth=2)
fig.canvas.mpl_connect('button_press_event',onclick)   
span = SpanSelector(ax, onselect, 'horizontal', useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red'))
plt.show()