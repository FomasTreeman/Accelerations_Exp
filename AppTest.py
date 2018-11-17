from App import *


class Model:
    def __init__(self):
        print('constructor called')

    def create(self, window: tk.Canvas):
        print('create() called')

    def update(self, window: tk.Canvas):
        print('update() called')


model = Model()
app = App("Test app", model)
app.mainloop()
