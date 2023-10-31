# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.py_pyfftw import PyPyfftw as BuiltinPyPyfftw


class PyPyfftw(BuiltinPyPyfftw):
    """A pythonic wrapper around FFTW, the FFT library,
    presenting a unified interface for all the supported transforms."""

    patch("setuptools.patch", when="@0.12.0:")
