from App import *
from tkinter import *
from Agent import *
import random


class Model:
    def __init__(self):
        self.positions = [
            Vector2(100, 100),
            Vector2(900, 200),
            Vector2(250, 300),
            Vector2(600, 200)
        ]
        self.agents = [Agent(random.randint(200, 400), random.randint(300, 550)) for i in range(10)]

    def setup(self, window: tk.Canvas):
        for x in self.agents:
            x.setup(window)

        sum_position = Vector2(0, 0)

        for agent in self.agents:
            sum_position += agent.position
        mean_position = sum_position / len(self.agents)
        window.create_text(mean_position.x, mean_position.y, text="b", anchor=tk.CENTER, fill="blue")

        for position in self.positions:
            velocity = mean_position - position
            window.create_text(position.x, position.y, text="a", anchor=tk.CENTER, fill="green")
            window.create_line(position.x, position.y, position.x + velocity.x, position.y + velocity.y,
                               fill="red", arrow=LAST)

    def draw(self, window: tk.Canvas):
        pass


model = Model()
app = App("Cohesion experiment v1", model)
app.mainloop()