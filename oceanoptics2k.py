import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from time import sleep
import seabreeze
seabreeze.use('pyseabreeze')  # using the python/usb lib not cseabreeze
import seabreeze.spectrometers as sb

devices = sb.list_devices()

sleep(1)
devices
spec = sb.Spectrometer(devices[0])

wl = spec.wavelengths()

spec.integration_time_micros(1e5)
wl = spec.wavelengths()

fig = plt.figure(figsize=[8,6])
ax = plt.subplot(1,1,1)
plt.ion()
#plt.xlim(400, 900)
#fig.show()
#fig.canvas.draw()

hot_pixels = [1235, 1303, 681, 589]
def hot_pixel_avg(intensity, hot_pixels=[]):
    if hot_pixel_list:
        for pixel in hot_pixel_list:
            pix = int(pixel)
            intensity[pix] = (intensity[pix-1]+intensity[pix+1])/2
    return intensity

def update_spectrum_plot(wl, intens, count=1):
    ax.clear()  # or plt.cla()
    y = intens[20:]
    #x = (1/(wl[20:]*1e-7))
    x = wl[20:]
    ax.plot(x,y)
    #ax.set_xlim(350,)
    #ax.set_ylim(1000, 6000)
    ax.relim()
    ax.autoscale_view()
    ax.text(0.05, 0.95, '%s %.2f' % (count, wl[y.argmax()]),
        verticalalignment='top', horizontalalignment='left',
        transform=ax.transAxes, color='green', fontsize=15)
    fig.canvas.draw()
    #sleep(0.5)

count = 1
for r in range(10):
    intens = spec.intensities()
    update_spectrum_plot(wl, intens, r)

#spec.close()

update_spectrum_plot(wl, m)
