#A special is a Black_Hole, but it will send the prey it eats to
#a random location with color changed randomly.
#If the prey is Floater, it only changes the location.
from blackhole import Black_Hole
import model
import random
from ball import Ball

class Special(Black_Hole):
    radius = 10
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        
    def update(self,eaten):
        eaten2 = set()
        mw, mh = model.world()
        if eaten != set():
            for i in eaten:
                i.set_location(random.randint(1, mw), random.randint(1,mh))
                i.set_dimension(20, 20)
                if type(i) == Ball:
                    i._color = "#"+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]+str(hex(random.randint(20,255)))[2:]
                eaten2.add(i)
        return eaten2
            

    
    def display(self,canvas):
        canvas.create_oval(self._x-Special.radius     , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill='yellow')
        