#!/usr/bin/env python3

import setuptools
import Cython.Build

setuptools.setup(
    ext_modules=Cython.Build.cythonize(
        'adjtimex.pyx',
        compiler_directives={
            'language_level': '3',
        },
    ),
    zip_safe=False,
)
