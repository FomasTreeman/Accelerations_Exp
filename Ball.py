from Vector2 import *
import tkinter as tk

class Ball:
    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.r = 50
        self.c = None

    def update(self):
        self.velocity += self.acceleration

        # self.velocity = self.velocity.limit_old(5)
        # self.velocity.limit(5)

        self.position += self.velocity
        self.acceleration *= 0

    def applyForce(self, force):
        self.acceleration += force

    def setup(self, window: tk.Canvas):
        self.c = window.create_oval(self.position.x - self.r, self.position.y - self.r,
                                    self.position.x + self.r, self.position.y + self.r)

    def display(self, window: tk.Canvas):
        window.coords(self.c, self.position.x - self.r, self.position.y - self.r,
                      self.position.x + self.r, self.position.y + self.r)

    def edges(self, window: tk.Canvas):
        x = self.position.x
        y = self.position.y
        height = window.winfo_height() - self.r
        width = window.winfo_width() - self.r

        if x >= width:
            self.position.x = width
            self.velocity.x *= -1
        if x <= self.r:
            self.position.x = 0
            self.velocity.x *= -1
        if y >= height :
            self.position.y = height
            self.velocity.y *= -1
        if y <= self.r:
            self.position.y = 0
            self.velocity.y *= -1

