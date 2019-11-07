import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from prey      import Prey
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
preys       = set()
eaters      = set()
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, preys, eaters
    running = False
    cycle_count = 0
    preys = set()
    eaters = set()
#start running the simulation
def start ():
    global running
    running = True
    

#stop running the simulation (freezing it)
def stop ():
    global running
    running = False

#tep just one update in the simulation
def step ():
    global running
    running = True
    update_all()
    running = False

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global k
    k = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global new, k
    try:
        if k != 'Remove':
            new = eval(k)(x,y)
            if isinstance(new, Prey):
                add(new)
            else:
                eaters.add(new)
        else:
            for i in preys:
                if i.contains((x,y)):
                    remove(i)
            for i in eaters:
                if i.contains((x,y)):
                    eaters.remove(i)
    except:
        pass

#add simulton s to the simulation
def add(s):
    preys.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    preys.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    for i in preys:
        x, y = i.get_location()
        if p((x,y)):
            result.add(i)
    return result

#call update for every simulton in the simulation
def update_all():
    global cycle_count,eaters,preys
    starved = set()
    if running:
        cycle_count += 1
        for i in preys:
            i.update()
        for i in eaters:           
            s = find(i.contains)
            preys = preys - s
            if isinstance(i, Special):
                changed = i.update(s)
                for c in changed:
                    preys.add(c)
            i.update(s)
            if i.get_dimension() == (0,0):
                starved.add(i)
    for s in starved:
        eaters.remove(s)

#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    
    for b in preys:
        b.display(controller.the_canvas)
    for e in eaters:
        e.display(controller.the_canvas)
    controller.the_progress.config(text = str(cycle_count) + " cycles/ "
                                    + str(len(preys) + len(eaters)) + " simulations")