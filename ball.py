# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    
    def __init__(self, x, y):
        aPrey = Prey(x, y, 10, 10, 1, 5)
        aPrey.randomize_angle()      
        Prey.__init__(self, x, y, 10, 10, aPrey.get_angle(), 5)
        self._color = 'blue'

    def update(self):
        self.move()
        
    def display(self,canvas):
        
        canvas.create_oval(self._x-Ball.radius     , self._y-Ball.radius,
                                self._x+Ball.radius, self._y+Ball.radius,
                                fill=self._color)
        