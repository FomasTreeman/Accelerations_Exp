#https://www.python-course.eu/tkinter_canvas.php
#canvas

import tkinter as tk
import os
import subprocess
import platform


class App(tk.Canvas):
    def __init__(self, title: str, my_model, master=None, app_width=1000, app_height=1000):
        tk.Canvas.__init__(self, master, width=app_width, height=app_height)
        self.master.title(title)
        self.model = my_model
        self.grid()
        self.model.create(self)
        self.raise_app()
        self.move()

    def move(self):
        self.model.update(self)
        self.update()
        self.after(10, self.move)

    def raise_app(self):
        self._root().attributes("-topmost", True)
        if platform.system() == 'Darwin':
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
            script = tmpl.format(os.getpid())
            output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
        self._root().after(0, lambda: self._root().attributes("-topmost", False))
