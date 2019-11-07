# A Hunter is both a Mobile_Simulton and a Pulsator in that it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
import model

class Hunter(Pulsator,Mobile_Simulton):
    hunting_range = 200
    def __init__(self,x,y):
        aHunter = Mobile_Simulton(x,y,10,10,1,5)
        aHunter.randomize_angle()
        Mobile_Simulton.__init__(self, x, y, 20, 20, aHunter.get_angle(), 5)
        Pulsator.__init__(self, x, y)
    
    def update(self, eaten):
        x,y = self.get_location()
        hunting_set = model.find(lambda x: self.distance(x) <= Hunter.hunting_range)
        if hunting_set != set():
            closest = min(hunting_set, key = lambda k: k.distance((x,y)))
            x1,y1 = closest.get_location()
            angle = atan2(y1-y, x1-x)
            self.set_angle(angle)
        Pulsator.update(self, eaten)
        self.move()
