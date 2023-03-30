import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

win = tk.Tk()
fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, win) # use this component
canvas.get_tk_widget().pack() # add to window
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.25) # add empty slot

x = [5, 6, 7, 8]
ax.plot(x, x)
ax.axis([0, 10, 0, 10])

ax_time = fig.add_axes([0.12, 0.1, 0.78, 0.03]) # the position and size of Slider
slider = Slider(ax_time, 'Time', 0, 30,  valinit=0) # new Slider

def update(val):
    pos = slider.val # get Slider value
    ax.axis([pos, pos+10, 0, 10]) # reset figure size and pos
    fig.canvas.draw_idle() # update figure

slider.on_changed(update) # trigger update on Slider pos changed

tk.mainloop()