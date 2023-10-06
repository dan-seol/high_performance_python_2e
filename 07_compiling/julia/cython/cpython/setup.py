from distutils.core import setup

from Cython.Build import cythonize
setup(name='calc', ext_modules=cythonize("cythonfn.pyx", compiler_directives={"language_level": "3"}))
