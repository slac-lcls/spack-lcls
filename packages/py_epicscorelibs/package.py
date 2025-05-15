# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpicscorelibs(PythonPackage):
    """The EPICS (Experimental Physics and Industrial Control System) core libraries for use by python modules."""

    homepage = "https://github.com/mdavidsaver/epicscorelibs"
    pypi = "epicscorelibs/epicscorelibs-7.0.7.99.0.0.tar.gz"

    maintainers("valmar")

    version("7.0.7.99.1.1", sha256="f9dd2c01913cf13959e882c7c2afccd5d55cd5084bd4597201ea119f65752231")
    version("7.0.7.99.0.0", sha256="d08cd4b228d7087fd172b9b48d5ebc1c763b6c1fbda26369776d5b274f1c73b4")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-dso@2.0a1:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
