from Vector2 import *
from App import *
from Ball import *
import random


class Model:
    def __init__(self):
        self.balls = [Ball(random.randint(100, 800), 100, .3) for i in range(10)]

    def setup(self, window: tk.Canvas):
        for ball in self.balls:
            ball.setup(window)

    def draw(self, window: tk.Canvas):
        count = 0
        for ball in self.balls:
            gravity = Vector2(0, 0.1)
            ball.apply_force(gravity)

            count += 1
            if count < 6:
                ball.apply_friction(0.01)

            ball.update()
            ball.edges(window)
            ball.display(window)


model = Model()
app = App("Acceleration experiment v2", model)
app.mainloop()
