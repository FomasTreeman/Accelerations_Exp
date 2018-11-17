from Vector2 import *
from App import *


class Model:
    def __init__(self):
        self.position = Vector2(500, 500)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.r = 50
        self.c = None

    def create(self, window: tk.Canvas):
        self.c = window.create_oval(self.position.x - self.r, self.position.y - self.r,
                                    self.position.x + self.r, self.position.y + self.r)

    def update(self, window: tk.Canvas):
        mouse = Vector2(
                window.master.winfo_pointerx() - window.master.winfo_rootx(),
                window.master.winfo_pointery() - window.master.winfo_rooty())

        displacement = mouse - self.position

        self.acceleration = displacement * .25
        self.velocity += self.acceleration

        # velocity = velocity.limit_old(5)
        self.velocity.limit(5)

        self.position += self.velocity

        window.coords(self.c, self.position.x - self.r, self.position.y - self.r,
                      self.position.x + self.r, self.position.y + self.r)


model = Model()
app = App("Acceleration experiment v2", model)
app.mainloop()
