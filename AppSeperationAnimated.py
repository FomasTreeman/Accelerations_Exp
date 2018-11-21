from Vector2 import *
from App import *
from Arrow import *
import random


class Model:
    def __init__(self):
        self.max_length = 100
        self.towards_ref = None
        self.mean_ref = None
        self.away_ref = None
        self.me = Agent(200, 200)
        self.agents = [Agent(random.randint(10, 990), random.randint(10, 590)) for i in range(50)]
        self.circle = None
        self.me.velocity = Vector2(0.1, 0)

    def setup(self, window: tk.Canvas):
        for x in self.agents:
            x.setup(window)

        self.me.ref = window.create_text(self.me.position.x, self.me.position.y, text="a", anchor=tk.CENTER,
                           fill="green")

        velocity = Vector2(0, 0)

        self.away_ref = window.create_line(self.me.position.x, self.me.position.y, self.me.position.x + velocity.x,
                                           self.me.position.y + velocity.y, fill="green", arrow=tk.LAST)

    def draw(self, window: tk.Canvas):
        self.me.update()
        window.coords(self.me.ref, self.me.position.x, self.me.position.y)

        sum_position = Vector2(0, 0)
        count = 0
        for boid in self.agents:
            distance = boid.position - self.me.position
            if distance.mag() <= 100:
                boid.display(window, "red")
                sum_position += boid.position
                count += 1
            else:
                boid.display(window, "black")

        mean_position = None
        if count == 0:
            mean_position = self.me.position
        else:
            mean_position = sum_position / count

        velocity = mean_position - self.me.position
        velocity *= -1
        mag = velocity.mag()
        velocity = velocity.norm() * (self.max_length - mag)

        window.coords(self.away_ref, self.me.position.x, self.me.position.y, self.me.position.x + velocity.x,
                      self.me.position.y + velocity.y)

        self.me.edges(window)

model = Model()
app = App("Seperation experiment v1", model)
app.mainloop()
