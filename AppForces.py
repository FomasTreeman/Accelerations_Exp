from Vector2 import *
from App import *
from Ball import *


class Model:
    def __init__(self):
        self.ball = Ball(500, 100, 10)

    def setup(self, window: tk.Canvas):
        self.ball.setup(window)

    def draw(self, window: tk.Canvas):
        gravity = Vector2(0, 0.5)
        self.ball.applyForce(gravity)
        # wind = Vector2(0.1, 0)
        # ball.apply_force(wind)
        self.ball.update()
        self.ball.edges(window)

        self.ball.display(window)


model = Model()
app = App("Acceleration experiment v2", model)
app.mainloop()
