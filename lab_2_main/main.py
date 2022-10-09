import unittest
import math

#objects of this class will be moving on container
class Ball:
    #give params
    def __init__(self, x_1, y_1, radius, direction):
        self.x = x_1
        self.y = y_1

        self.r = radius

        self.direction = direction
        self.delta_x = self.direction * math.cos(self.x)
        self.delta_y = -1 * self.direction * math.sin(self.y)


#function for moving ball
    def move(self, x, y):
        self.x += x
        self.y += y

#functions for changing coordinates relate to Ox or Oy
    def reflect_horizontal(self) -> int:
        self.x = -1 * self.x

    def perfect_vertical(self) -> int:
        self.y = int(-1 * self.delta_y)




class Container:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = self.x + width - 1
        self.y2 = self.y + height - 1
        
#check if ball can be on container. if no, coordinates will be changed
    def collides_with(self, ball: Ball) -> bool:
        if self.width > ball.x > self.x and self.height > ball.y > self.y:
            return True
        else:
            ball.perfect_vertical() or ball.reflect_horizontal()
            return self.collides_with(ball)






