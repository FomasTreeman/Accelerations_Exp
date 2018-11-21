#https://www.python-course.eu/tkinter_canvas.php
#canvas
from tkinter import *
import random
import os
import subprocess
import platform
from Vector2 import *


class Boid:

    def __init__(self, velocity, position):
        self.velocity = velocity
        self.position = position

#make top window
#https://stackoverflow.com/questions/1892339/how-to-make-a-tkinter-window-jump-to-the-front
def raise_app(root: Tk):
    root.attributes("-topmost", True)
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
        script = tmpl.format(os.getpid())
        output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
    root.after(0, lambda: root.attributes("-topmost", False))

master = Tk()

canvas_width = 1000
canvas_height = 1000
window = Canvas(master,
           width=canvas_width,
           height=canvas_height)
window.pack()

sum_velocity = Vector2(0, 0)
COUNT = 10
for i in range(COUNT):
    position = Vector2(random.randint(100, 900), random.randint(100, 900))
    velocity = Vector2(random.randint(-50, 50), random.randint(-100, 100))
    sum_velocity += velocity
    window.create_line(position.x, position.y, position.x + velocity.x, position.y + velocity.y, fill="red", arrow=LAST)

my_velocity = sum_velocity / COUNT
window.create_line(600, 600, 600 + my_velocity.x, 600 + my_velocity.y, fill="black", arrow=LAST)

raise_app(master)


mainloop()