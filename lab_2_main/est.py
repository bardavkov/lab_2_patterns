import unittest
from main import *
class Test_ball(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(90, 7, 6, 60)
        self.container = Container(-100, -100, 100, 100)



    def test_1_1(self):
        self.ball.move(4, 9)
        x = self.ball.x
        y = self.ball.y
        self.assertEqual(y, 16)
        self.assertEqual(x, 94)

    def test_1_2(self):
        self.ball.move(1, 99)
        y = self.ball.y
        x = self.ball.x
        self.assertEqual(y, 106)
        self.assertEqual(x, 91)

    def test_2_1(self):
        self.ball.perfect_vertical()
        y = self.ball.y
        self.assertEqual(y, 39)

    def test_2_2(self):
        self.ball.reflect_horizontal()
        x = self.ball.x
        self.assertEqual(x, -90)


    def test_3_1(self):
        x = self.container.collides_with(self.ball)
        self.assertEqual(x, True)