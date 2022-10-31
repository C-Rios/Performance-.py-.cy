import Planeta_orbita_cy
import Planeta_orbita_py
import time

steps=1000000
time_frame = 100

planet_cy = Planeta_orbita_cy.Planet()
planet_py = Planeta_orbita_py.Planet()

init_time=time.time()
Planeta_orbita_py.step_time(planet_py, time_frame, steps)
end_time=time.time()

time_python = end_time - init_time

init_time=time.time()
Planeta_orbita_cy.step_time(planet_cy, time_frame, steps)
end_time=time.time()

time_cython = end_time - init_time

print("Tiempo de ejecucion con python: {}s\nTiempo de ejcucion con cython: {}s".format(time_python, time_cython))

print("Cython es {} veces más rápido que python ".format(round(time_python/time_cython, 2)))