# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.pkg.builtin.py_pyopencl import PyPyopencl as BuiltinPyPyopencl


class PyPyopencl(BuiltinPyPyopencl):
    """Python wrapper for OpenCL."""
    
    version("2023.1.4", sha256="220174efca900e9d5de5aef2aa1b77a6f2550501de92b035a91013aeae4d4c5e")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-pytools@2021.2.7:", type=("build", "run"))
