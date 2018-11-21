from Vector2 import *
from App import *
from Ball import *


class Model:
    def __init__(self):
        self.sun = Ball(500, 300, 10)
        self.planet = Ball(500, 100, 2)

    def setup(self, window: tk.Canvas):
        self.sun.setup(window)
        self.planet.setup(window)

    def draw(self, window: tk.Canvas):
        attract = self.sun.attract(self.planet)
        self.planet.apply_force(attract)

        wind = Vector2(0.1, 0)
        self.planet.apply_force(wind)

        self.planet.update()
        self.planet.display(window)
        self.sun.update()
        self.sun.display(window)


model = Model()
app = App("Attraction experiment", model)
app.mainloop()
