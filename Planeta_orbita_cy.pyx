cimport cython

"""
Date: Nov 01/2022
Author: Juan Camilo De Los Ríos
Topic: Cython - Python comparison
Subject: Planets - gravitational orbit
"""

#from math import sqrt

cdef extern from "math.h":
    double sqrt(double x) nogil

cdef class Planet(object):
    #Public vars

    cdef public float x,y,z,vx,vy,vz,m

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
"""
To avoid division's by 0 (distance = 0), we'll prepare a 
Cython alert: cdivision that returns True or False
When true is returned, instruction gets declined when it gets
over the flag (INF) 
A cython decorator is declared
"""

@cython.cdivision(True)
cdef void single_step(Planet planet, double dt) nogil:
    """Single step"""

    cdef double distance, Fx, Fy, Fz

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
 
def step_time(Planet planet, double time_span, int n_steps):
    """Makes a number of steps"""
    cdef double dt = time_span / n_steps
    cdef int j

    """
    Parallelism is prepared
    """
    with nogil:
        for j in range(n_steps):
            single_step(planet,dt)

