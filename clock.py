#!/usr/bin/python3
# coding: utf-8

import time
import random
from tkinter import ttk, Tk
from tkinter import font

def interpolate_color(color1, color2, factor: float):
    """Interpolate between two colors with a given factor (0.0 - 1.0)."""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def refresh_time():
    global current_color, target_color, step

    # Update the label text
    time_label.configure(text=time.strftime('%H:%M:%S'))

    # Interpolate the color
    new_color = interpolate_color(current_color, target_color, step)
    time_label.configure(foreground=new_color)

    # Update the step and check if we need to pick a new target color
    step += 0.01
    if step >= 1.0:
        step = 0.0
        current_color = target_color
        target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Schedule the next update
    time_label.after(100, refresh_time)

root = Tk()
root.title("Clock App")
root.geometry("600x200")
root["bg"] = "black"

style = ttk.Style()
style.configure('TLabel', background='black')

time_label = ttk.Label(root, text="", font=('arial', 100))
time_label.pack(expand=True)

# Initialize colors and step
current_color = (0, 255, 255)  # Initial color (light blue)
target_color = (255, 0, 255)   # Initial target color (magenta)
step = 0.0

# Start the update loop
time_label.after(100, refresh_time)

root.mainloop()