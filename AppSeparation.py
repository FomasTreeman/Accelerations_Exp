from App import *
from Agent import *
import random


class Model:
    def __init__(self):
        self.me = Agent(200, 200)
        self.agents = [Agent(random.randint(10, 990), random.randint(10, 590)) for i in range(50)]

    def setup(self, window: tk.Canvas):
        for x in self.agents:
            x.setup(window)

        sum_position = Vector2(0, 0)
        count = 0
        window.create_text(self.me.position.x, self.me.position.y, text="a", anchor=tk.CENTER,
                           fill="green")

        for agent in self.agents:
            distance = agent.position - self.me.position
            if distance.mag() <= 100:
                agent.display(window, "red")
                sum_position += agent.position
                count += 1
        mean_position = sum_position / count
        window.create_text(mean_position.x, mean_position.y, text="b", anchor=tk.CENTER,
                           fill="blue")
        velocity = mean_position - self.me.position
        window.create_line(self.me.position.x, self.me.position.y, self.me.position.x + velocity.x, self.me.position.y + velocity.y,
                           fill="red", arrow=tk.LAST)
        velocity *= -1
        window.create_line(self.me.position.x, self.me.position.y, self.me.position.x + velocity.x, self.me.position.y + velocity.y,
                           fill="yellow", arrow=tk.LAST)

    def draw(self, window: tk.Canvas):
        pass


model = Model()
app = App("Separation experiment v1", model)
app.mainloop()
