from Vector2 import *
from App import *
from Ball import *
import random


class Model:
    def __init__(self):
        self.balls = [Ball(random.randint(100, 800), 100, random.random() * 4) for i in range(10)]

    def setup(self, window: tk.Canvas):
        window.create_line(0, 300, 1000, 300)
        for ball in self.balls:
            ball.setup(window)

    def draw(self, window: tk.Canvas):
        count = 0
        for ball in self.balls:
            gravity = Vector2(0, 0.1 * ball.mass)
            ball.apply_force(gravity)

            if ball.position.y > 300:
                ball.apply_drag(-0.1)

            ball.update()
            ball.edges(window)
            ball.display(window)


model = Model()
app = App("Acceleration experiment v2", model)
app.mainloop()
