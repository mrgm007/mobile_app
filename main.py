from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class PongBorder(Widget):
    def __init__(self, **kwargs):
        super(PongBorder, self).__init__(**kwargs)
        with self.canvas:
            Color(0.74, 0.95, 0.82)

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_x - self.center_x) / (self.width / 2)
            bounced = Vector(vx, -1 * vy)
            vel = bounced * 1.1
            ball.velocity = vel.x + offset, vel.y
    def __init__(self, **kwargs):
        super(PongPaddle, self).__init__(**kwargs)
        with self.canvas:
            Color(0.74, 0.95, 0.82)
class PongBallSelf(Widget):
    def __init__(self, **kwargs):
        super(PongBallSelf, self).__init__(**kwargs)
        with self.canvas:
            Color(0.74, 0.95, 0.82, 0.1)

class PongBall(Widget):
    temp1_x = NumericProperty(0)
    temp1_y = NumericProperty(0)
    temp2_x = NumericProperty(0)
    temp2_y = NumericProperty(0)
    temp3_x = NumericProperty(0)
    temp3_y = NumericProperty(0)
    temp4_x = NumericProperty(0)
    temp4_y = NumericProperty(0)
    temp5_x = NumericProperty(0)
    temp5_y = NumericProperty(0)
    temp6_x = NumericProperty(0)
    temp6_y = NumericProperty(0)
    temp7_x = NumericProperty(0)
    temp7_y = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.temp7_x = self.temp6_x
        self.temp7_y = self.temp6_y
        self.temp6_x = self.temp5_x
        self.temp6_y = self.temp5_y
        self.temp5_x = self.temp4_x
        self.temp5_y = self.temp4_y
        self.temp4_x = self.temp3_x
        self.temp4_y = self.temp3_y
        self.temp3_x = self.temp2_x
        self.temp3_y = self.temp2_y
        self.temp2_x = self.temp1_x
        self.temp2_y = self.temp1_y
        self.temp1_x = self.center_x
        self.temp1_y = self.center_y


    def __init__(self, **kwargs):
        super(PongBall, self).__init__(**kwargs)
        with self.canvas:
            Color(0.74, 0.95, 0.82)
class Menu(Widget):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0, 0.5)
class MyButton(Button):
    def __init__(self, posx, posy, sizex, sizey, source, other_button, **kwargs):
        super(MyButton, self).__init__(pos=(posx, posy), size=(sizex, sizey), **kwargs)
        self.other_button = other_button
        with self.canvas:
            Rectangle(pos=(posx - 10, posy - 30), size=(sizex + 20, sizey * 2), source=source)
    def on_press(self):
            # remove other button and then remove self
        self.parent.remove_widget(self.other_button)
        self.parent.remove_widget(self)
class MyButton(Button):
    def __init__(self, posx, posy, sizex, sizey, source, other_button, other_button2, **kwargs):
        super(MyButton, self).__init__(pos=(posx, posy), size=(sizex, sizey), **kwargs)
        self.other_button = other_button

        self.other_button2 = other_button2
        with self.canvas:
            Rectangle(pos=(posx - 5, posy - 5), size=(sizex + 10, sizey + 10), source=source)
    def on_press(self):
            # remove other button and then remove self
        self.parent.remove_widget(self.other_button)
        self.parent.remove_widget(self.other_button2)
        self.parent.remove_widget(self)
class MButton(Button):
    def __init__(self, posx, posy, size, source, **kwargs):
        super(MButton, self).__init__(pos=(posx, posy), size=(size, size), **kwargs)
        with self.canvas:
            Rectangle(pos=(posx, posy), size=(size, size), source=source)
    def on_press(self):
            # remove other button and then remove self
        self.parent.remove_widget(self)

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    a = NumericProperty(3)
    b = NumericProperty()
    button_player_x = NumericProperty()
    button_player1_y = NumericProperty()
    button_player2_y = NumericProperty()
    p1 = NumericProperty(2)
    p = NumericProperty(1)
    a1 = NumericProperty(2)
    MenuHeight = NumericProperty(0)
    MenuWidth = NumericProperty(0)
    BHeight = NumericProperty(640)
    BWidth = NumericProperty(360)
    i = NumericProperty(0)
    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        with self.canvas:
            Color(0.74, 0.95, 0.82)

    def create_buttons_player(self):
        button1 = MyButton(posx=self.BWidth/2 - 55, posy=self.BHeight/2 + 25, sizex=110, sizey=30, source='1p.png', other_button=None, other_button2=None)
        button2 = MyButton(posx=self.BWidth/2 - 55, posy=self.BHeight/2 - 50, sizex=110, sizey=30, source='2p.png', other_button=button1, other_button2=None)
        button1.other_button = button2
        button1.bind(on_release=self.serv_player1)
        button2.bind(on_release=self.serv_player2)
        self.add_widget(button1)
        self.add_widget(button2)
    def serv_player1(self, instance):
        self.p = 0
        self.create_buttons_difficulty()
    def serv_player2(self, instance):
        self.p = 1
        self.create_buttons_difficulty()
    def create_buttons_difficulty(self):
        button1 = MyButton(posx=self.BWidth/2 - 55, posy=self.BHeight/2 + 40, sizex=110, sizey=30, source='easy.png', other_button=None, other_button2=None)
        button2 = MyButton(posx=self.BWidth/2 - 55, posy=self.BHeight/2 - 12, sizex=110, sizey=30, source='medium.png', other_button=button1, other_button2=None)
        button3 = MyButton(posx=self.BWidth/2 - 55, posy=self.BHeight/2 - 65, sizex=110, sizey=30, source='hard.png', other_button=button1, other_button2=button2)
        button1.other_button = button2
        button1.other_button2 = button3
        button2.other_button2 = button3
        button1.bind(on_release=self.serv_easy)
        button2.bind(on_release=self.serv_medium)
        button3.bind(on_release=self.serv_hard)
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)
    def serv_easy(self, instance):
        self.a1 = 1
        self.b = 3
        self.a = self.b
        self.p1 = self.p
        self.serve_ball(vel=(0, 0))
        self.MenuHeight = self.height
        self.MenuWidth = self.width
        self.i = 0
        self.create_buttons()
    def serv_medium(self, instance):
        self.a1 = 3
        self.b = 5
        self.a = self.b
        self.p1 = self.p
        self.serve_ball(vel=(0, 0))
        self.MenuHeight = self.height
        self.MenuWidth = self.width
        self.i = 0
        self.create_buttons()
    def serv_hard(self, instance):
        self.a1 = 5
        self.b = 7
        self.a = self.b
        self.p1 = self.p
        self.serve_ball(vel=(0, 0))
        self.MenuHeight = self.height
        self.MenuWidth = self.width
        self.i = 0
        self.create_buttons()
    def create_buttons_final(self):
        button1 = MyButton(posx=self.BWidth/2 - 65, posy=self.BHeight/2 - 15, sizex=130, sizey=40, source='replay.png', other_button=None, other_button2=None)
        button2 = MyButton(posx=self.BWidth/2 - 55, posy=self.BHeight/2 - 60, sizex=110, sizey=30, source='menu.png', other_button=button1, other_button2=None)
        button1.other_button = button2
        button1.bind(on_release=self.replay)
        button2.bind(on_release=self.mainmenu)
        self.add_widget(button1)
        self.add_widget(button2)
    def replay(self, instance):
        self.MenuHeight = self.height
        self.MenuWidth = self.width
        self.serve_ball(vel=(0, 0))
        self.i = 0
        self.create_buttons()
    def mainmenu(self, instance):
        self.p1 = 2
        self.serve_ball(vel=(0, self.a))
        self.create_buttons_player()
    def create_buttons(self):
        button1 = MButton(posx=self.BWidth/2 - 40, posy=self.BHeight/2 - 40, size=80, source='start.png')
        button1.bind(on_release=self.serv)
        self.add_widget(button1)
    def serv(self,instance):
        self.serve_ball(vel=(0, self.a))
    def serve_ball(self, vel=(0, 3)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        if self.i == 0 and not self.p1 == 2:
            self.i += 1
            super(PongGame, self)
            with self.canvas:
                Color(0.74, 0.95, 0.82)
                Ellipse(pos=(self.width - 30, self.height / 2 - 20), size=(15, 15))
                Ellipse(pos=(self.width - 30, self.height / 2 - 40), size=(15, 15))
                Ellipse(pos=(self.width - 30, self.height / 2 + 10), size=(15, 15))
                Ellipse(pos=(self.width - 30, self.height / 2 + 30), size=(15, 15))
        self.BHeight = self.height
        self.BWidth = self.width
        self.ball.move()
        # bounce of paddles

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.x - 10 < self.x) or (self.ball.right + 10 > self.right):
            self.ball.velocity_x *= -1

        # went of to a side to score point?
        if self.ball.y < self.y + 10:
            if not self.p1 == 2:
                self.player2.score += 1
                self.serve_ball(vel=(0, 0))
                super(PongGame, self)
                with self.canvas:
                    Color(0.24, 0.45, 0.18)
                    if (self.player2.score == 1):
                        Ellipse(pos=(self.width - 27.5, self.height / 2 + 12.5), size=(10, 10))
                    if (self.player2.score == 2):
                        Ellipse(pos=(self.width - 27.5, self.height / 2 + 32.5), size=(10, 10))
                    Color(0.74, 0.95, 0.82)
                    if (self.player2.score == 3):
                        Ellipse(pos=(self.width - 30, self.height/2 - 20), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 - 40), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 10), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 30), size=(15, 15))
                        Color(0, 0, 0, 0.5)
                        Ellipse(pos=(self.width - 30, self.height / 2 - 20), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 - 40), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 10), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 30), size=(15, 15))
                if not self.player2.score == 3:
                    self.create_buttons()
                self.a = self.b
            else:
                self.serve_ball(vel=(0, 4))
        if self.ball.top > self.height - 10:
            if not self.p1 == 2:
                self.player1.score += 1
                self.serve_ball(vel=(0, 0))
                super(PongGame, self)
                with self.canvas:
                    Color(0.24, 0.45, 0.18)
                    if (self.player1.score == 1):
                        Ellipse(pos=(self.width - 27.5, self.height / 2 - 17.5), size=(10, 10))
                    if (self.player1.score == 2):
                        Ellipse(pos=(self.width - 27.5, self.height / 2 - 37.5), size=(10, 10))
                    Color(0.74, 0.95, 0.82)
                    if (self.player1.score == 3):
                        Ellipse(pos=(self.width - 30, self.height / 2 - 20), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 - 40), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 10), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 30), size=(15, 15))
                        Color(0, 0, 0, 0.5)
                        Ellipse(pos=(self.width - 30, self.height / 2 - 20), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 - 40), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 10), size=(15, 15))
                        Ellipse(pos=(self.width - 30, self.height / 2 + 30), size=(15, 15))
                if not self.player1.score == 3:
                    self.create_buttons()
                self.a = self.b * -1
            else:
                self.serve_ball(vel=(0, self.a))
        if self.p1 == 0:
            if (self.player2.center_x < self.ball.x):
                if (self.player2.center_x < self.width - 45):
                    if(self.ball.x - self.player2.center_x > self.a1):
                        self.player2.center_x += self.a1
            else:
                if (self.player2.center_x > self.x + 65):
                    if (self.player2.center_x - self.ball.x > self.a1):
                        self.player2.center_x -= self.a1
        if self.p1 == 2:
            if (self.player1.center_x < self.ball.x):
                if (self.player1.center_x < self.width - 45):
                    if (self.ball.x - self.player1.center_x > 1):
                        self.player1.center_x += 1
            else:
                if (self.player1.center_x > self.x + 65):
                    if (self.player1.center_x - self.ball.x > 1):
                        self.player1.center_x -= 1

            if (self.player2.center_x < self.ball.x):
                if (self.player2.center_x < self.width - 45):
                    if (self.ball.x - self.player2.center_x > 1):
                        self.player2.center_x += 1
            else:
                if (self.player2.center_x > self.x + 65):
                    if (self.player2.center_x - self.ball.x > 1):
                        self.player2.center_x -= 1
        if self.player1.score == 3:
            self.player1.score = 0
            self.player2.score = 0
            self.MenuWidth = 0
            self.MenuHeight = 0
            self.create_buttons_final()

        if self.player2.score == 3:
            self.player1.score = 0
            self.player2.score = 0
            self.MenuWidth = 0
            self.MenuHeight = 0
            self.create_buttons_final()

    def on_touch_move(self, touch):
        if not self.p1 == 2:
            if touch.y < self.height / 3:
                if touch.x < self.width - 45 and touch.x > self.x + 65:
                    self.player1.center_x = touch.x
            if self.p1 == 1:
                if touch.y > self.height - self.height / 3:
                    if touch.x < self.width - 45 and touch.x > self.x + 65:
                        self.player2.center_x = touch.x

class PongApp(App):
    def build(self):

        Window.clearcolor = (0.24, 0.45, 0.18)
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        game.create_buttons_player()
        return game


if __name__ == '__main__':
    PongApp().run()
