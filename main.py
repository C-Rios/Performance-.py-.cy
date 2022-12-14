"""
Date: Nov 01/2022
Author: Juan Camilo De Los Ríos
Topic: Cython - Python comparison
Subject: Py/Cy compare
"""

from ast import iter_fields
import Planeta_orbita_cy
import Planeta_orbita_py
import time
import numpy as np

#Params
steps= np.arange(1000000,100000000,1000000, dtype=int)
time_frame = np.arange(100,10000,100, dtype=int)

planet_cy = Planeta_orbita_cy.Planet()
#Earth data
planet_cy.x = 100*10**3
planet_cy.y = 300*10**3
planet_cy.z = 700*10**3
planet_cy.vx = 2.00*10**3
planet_cy.vy = 29.87*10**3
planet_cy.vz = 0.034*10**3
planet_cy.m = 5.9742*10**24

planet_py = Planeta_orbita_py.Planet()

#Earth data
planet_py.x = 100*10**3
planet_py.y = 300*10**3
planet_py.z = 700*10**3
planet_py.vx = 2.00*10**3
planet_py.vy = 29.87*10**3
planet_py.vz = 0.034*10**3
planet_py.m = 5.9742*10**24

#Experimentation area
#Gaussian noice reduction
print_format = "{},{},{:.5f},{:.5f}\n"

#Clears csv
f = open("planeta.csv","w")
f.truncate()
f.close()

with open("planeta.csv","a") as archivo:
    archivo.write("steps, time_frame, python, cython\n")

for i in range (len(steps)):
    step = steps[i]
    time_frame_i = time_frame[i]

    init_time=time.time()
    Planeta_orbita_py.step_time(planet_py, time_frame_i, step)
    end_time=time.time()

    time_python = end_time - init_time

    init_time=time.time()
    Planeta_orbita_cy.step_time(planet_cy, time_frame_i, step)
    end_time=time.time()

    time_cython = end_time - init_time

    with open("planeta.csv","a") as archivo:
        archivo.write(print_format.format(step,time_frame_i, time_python,time_cython))

"""
# Performance-.py-.cy

## SHARED OBJECT COMPILATION

### Create a file named setup.py

*from os import lseek*

*from distutils.core import setup, Extension*

*from Cython.Build import cythonize*

*exts = (cythonize("*File_name*.pyx"))*

*setup(ext_modules = exts)*

### Compile it into a Shared Object (SO)

`python3 setup.py build_ext --inplace`

"""

#print("Tiempo de ejecucion con python: {}s\nTiempo de ejecucion con cython: {}s".format(time_python, time_cython))
#print("Cython es {} veces más rápido que python ".format(round(time_python/time_cython, 2)))