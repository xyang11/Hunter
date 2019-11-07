# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    counter = 30
    def __init__(self, x,y):
        Black_Hole.__init__(self, x, y)
        self.count = 0
        
    def update(self, eaten):

        if eaten == set():
            self.count += 1
            if self.count > Pulsator.counter:
                self.change_dimension(-1, -1)
                self.count = 0
        else:
            self.change_dimension(1, 1)
            self.count = 0
        
        return eaten