from App import *
from Agent import *
import random


class Model:
    def __init__(self):
        self.agents = [Agent(random.randint(10, 990), random.randint(10, 590)) for i in range(10000)]
        self.circle = None

    def setup(self, window: tk.Canvas):
        for x in self.agents:
            x.setup(window)

        circle_ref = window.create_text(500, 300, text="o", anchor=tk.CENTER, fill="blue")
        self.circle = window.coords(circle_ref)

    def draw(self, window: tk.Canvas):
        for agent in self.agents:
            distance = agent.position - Vector2(500, 300)
            if distance.mag() <= 100:
                agent.display(window, "red")


model = Model()
app = App("Radius experiment v1", model)
app.mainloop()
