from distutils.core import setup
import numpy as np

from Cython.Build import cythonize
setup(ext_modules=cythonize("cythonfn.pyx", compiler_directives={"language_level": "3"}),
      define_macros={'NPY_NO_DEPRECATED_API': 'NPY_1_7_API_VERSION'},
      include_dirs=[np.get_include()])

