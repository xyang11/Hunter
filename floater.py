# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    radius = 5
    
    def __init__(self, x, y):
        aPrey = Prey(x, y, 10, 10, 1, 5)
        aPrey.randomize_angle()
        Prey.__init__(self, x, y, 10, 10, aPrey.get_angle(), random.randint(3,7))
        self._color = 'red'
    
    def update(self): 
        if random.randint(1,10) <= 3:
            change = random.random()-0.5
            self.set_angle(self.get_angle() + change)
            if 3 <= self.get_speed() + change <= 7:
                self.set_speed(self.get_speed() + change)            
        self.move()

    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius     , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)
