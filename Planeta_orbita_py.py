"""
Date: Nov 01/2022
Author: Juan Camilo De Los Ríos
Topic: Cython - Python comparison
Subject: Planets - gravitational orbit
"""

from math import sqrt

class Planet(object):
    def __init__(self):
        #Initial position and velocity
        self.x = 1.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.5
        self.vz = 0.0

        #Mass
        self.m = 1.0

def single_step(planet, dt):
    """Single step"""

    #Compute force: gravity towards origin
    distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
    Fx = -planet.x / distance**3
    Fy = -planet.y / distance**3
    Fz = -planet.z / distance**3

    #Time step position, according to velocity
    planet.x += dt * planet.vx
    planet.y += dt * planet.vy
    planet.z += dt * planet.vz

    #time step velocity, according to force and mass
    planet.vx += dt * Fx / planet.m
    planet.vy += dt * Fy / planet.m
    planet.vz += dt * Fz / planet.m

def step_time(planet, time_span, n_steps):
    """Makes a number of steps"""
    dt = time_span / n_steps
    for j in range(n_steps):
        single_step(planet, dt)

