# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyP4p(PythonPackage):
    """PVAccess for Python."""

    homepage = "https://mdavidsaver.github.io/p4p"
    pypi = "p4p/p4p-4.2.0.tar.gz"

    maintainers("valmar")

    version("4.2.0", sha256="0786e48302666f44fad71dca783b7ef2aa2373cfe4dbd3115eac655f30fecb33")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-dso@1.3a1:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython@0.20:", type=("build", "run"))
    depends_on("py-epicscorelibs@7.0.3.99.2.0a1:", type=("build", "run"))
    depends_on("py-pvxslibs", type=("build", "run"))
