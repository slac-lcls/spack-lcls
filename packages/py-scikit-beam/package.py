# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitBeam(PythonPackage):
    """Data analysis tools for X-Ray, Neutron and Electron sciences."""

    homepage = "https://github.com/scikit-beam/scikit-beam"
    pypi = "scikit-beam/scikit-beam-0.0.24.tar.gz"

    maintainers = ["valmar"]

    version("0.0.26", sha256="4852b9c641a392d37bdca43353925a3cb7465f03017038238e3fc08238b70c64")

    depends_on("py-setuptools", type="build")
    depends_on("py-fabio", type=("build", "run"))
    depends_on("py-lmfit", type=("build", "run"))
    depends_on("py-numpy@1.15:", type=("build", "run"))
    depends_on("py-pyfai", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
