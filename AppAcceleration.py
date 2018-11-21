from Vector2 import *
from App import *
from Ball import *


class Model:
    def __init__(self):
        self.ball = Ball(500, 500, 2)

    def setup(self, window: tk.Canvas):
        self.ball.setup(window)

    def draw(self, window: tk.Canvas):
        mouse = Vector2(
                window.master.winfo_pointerx() - window.master.winfo_rootx(),
                window.master.winfo_pointery() - window.master.winfo_rooty())

        displacement = mouse - self.ball.position

        self.ball.apply_force(displacement * 0.25)
        self.ball.update()

        self.ball.display(window)


model = Model()
app = App("Acceleration experiment v2", model)
app.mainloop()
