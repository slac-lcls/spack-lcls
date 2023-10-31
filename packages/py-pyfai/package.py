# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyfai(PythonPackage):
    """PyFAI is an azimuthal integration library that tries to be fast (as fast as C and even
    more using OpenCL and GPU)."""

    homepage = "https://www.example.com"
    pypi = "pyfai/pyfai-2023.9.0.tar.gz"

    maintainers("valmar")

    version("2023.9.0", sha256="027c24622d4c55a00f17b796b6891560f7eb6b6d92b0e3877c97f65485ec1f3b")

    depends_on("py-setuptools@:60", type="build")
    depends_on("meson", type="build")
    depends_on("py-meson-python", type="build")
    depends_on("ninja", type="build")
    depends_on("py-pyproject-metadata", type="build")
    depends_on("py-tomli", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython@0.29.31:", type=("build", "run"))
    depends_on("py-fabio", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-silx@1.1:", type=("build", "run"))
    depends_on("py-pyopengl", type=("build", "run"))
    depends_on("py-pyqt5", type=("build", "run"))
    depends_on("py-hdf5plugin", type=("build", "run"))
    depends_on("py-transformations", type=("build", "run"))
    depends_on("py-nbsphinx", type=("build", "run"))

