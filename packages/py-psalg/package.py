# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPsalg(PythonPackage):
    """LCLS II Developement: PSAlg Python."""

    homepage = "https://github.com/slac-lcls/lcls2"
    url = "https://github.com/slac-lcls/lcls2/archive/refs/tags/4.0.0.tar.gz"

    maintainers("valmar")

    version("4.1.0", sha256="f3f2c7850f43a2e0dbed7589ff37a706fe17e4fa07f2878dca47f6b6ea7d677b")
    version("4.0.0", sha256="f38f8c884b688c3b681fbce9be6068078f8549b05f510234a61f985ae1db0cfd")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9", type=("build", "run"))
    depends_on("psalg", type=("build", "run"))

    build_directory = "psalg"
