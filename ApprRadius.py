from Vector2 import *
from App import *
from Agent import *
import random


class Model:
    def __init__(self):
        self.Agents = [Agent(random.randint(10, 990), random.randint(10, 590)) for i in range(10000)]
        self.circle = None

    def setup(self, window: tk.Canvas):
        for x in self.Agents:
            x.setup(window)

        circle_ref = window.create_text(500, 300, text="o", anchor=tk.CENTER, fill="blue")
        self.circle = window.coords(circle_ref)

    def draw(self, window: tk.Canvas):
        count = 0
        for boid in self.Agents:
            distance = boid.position - Vector2(500, 300)
            if distance.mag() <= 100:
            # if boid.position.x <= 500 + 100 or boid.position.y <= 300 + 100:
                boid.display(window, "red")


model = Model()
app = App("Radius experiment v1", model)
app.mainloop()
