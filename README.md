# Performance-.py-.cy

SHARED OBJECT COMPILATION

Create a file named setup.py

>`from os import lseek`
>`from distutils.core import setup, Extension`
>`from Cython.Build import cythonize`
>`exts = (cythonize("*File_name*.pyx"))`

>`setup(ext_modules = exts)`

Compile it into a Shared Object (SO)

`python3 setup.py build_ext --inplace`
