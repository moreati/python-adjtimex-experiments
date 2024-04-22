#!/usr/bin/env python3

import setuptools

setuptools.setup(
    cffi_modules=['adjtimex_build.py:ffibuilder'],
)
