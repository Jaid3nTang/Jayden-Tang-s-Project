PythonFinalizationError
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
# Class that describes the state of the car, including horizontal and vertical position, horizontal velocity, and time
class State:
    xpos : float
    ypos : float
    xvel : float
    time : float

time_step = 0.3

def step (state:State) -> State:
# IDK if I should put Step 2's variables (slip_angle, lateral_force, etc) into State class, I don't believe we have to since those aren't car properties 
# Or if I need to adjust some of the attributes instead (xvel -> forward speed and lateral vel)
# Also DK how to incorporate initialized variables into the model, I believe there are some physics formulas to it
    mass = 300
    forward_speed = 15 #Meters/second
    cornering_stiffness = 36000 # Newtons/radians
    # Reserach states that "Cornering stiffness quantifies a tire’s ability to generate lateral force in response to steering input." I require more elaboration. 

    # Part 2 Initialization 
    if state.time <= 3.0:
        steer_angle = 0.08726646 * state.time/3 # 5 degrees converted into 0.087626646 radians
    elif state.time <= 10.0:
        steer_angle = 0.08726646 # 5 degrees converted into 0.087626646 radians
    else:
        steer_angle = 0.0

    slip_angle = steer_angle - (state.xvel/forward_speed)
    lateral_force = cornering_stiffness * slip_angle
    lateral_accel = lateral_force/mass

    new_vel = state.xvel + (lateral_accel * time_step)
    new_xpos = state.xpos + state.xvel * time_step
    new_time = state.time + time_step


    newState = state(
        xpos = new_xpos, 
        ypos = 0.0, 
        xvel = new_vel, 
        time = new_time, 
    )

    return newState