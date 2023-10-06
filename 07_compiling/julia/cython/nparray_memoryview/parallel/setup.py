from distutils.core import setup
from distutils.extension import Extension
import numpy as np

ext_modules = [Extension(
      "cythonfn",
      ["cythonfn.pyx"], 
      
      extra_compile_args=['-fopenmp'], 
      extra_link_args=['-fopenmp'],
      define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]
      )]

from Cython.Build import cythonize
setup(ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"},),include_dirs=[np.get_include()]) 

