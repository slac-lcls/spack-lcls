# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Psalg(CMakePackage):
    """LCLS II Development: PSAlg."""

    homepage = "https://github.com/slac-lcls/lcls2"
    url = "https://github.com/slac-lcls/lcls2/archive/refs/tags/4.0.0.tar.gz"

    maintainers("valmar")

    version("4.0.0", sha256="f38f8c884b688c3b681fbce9be6068078f8549b05f510234a61f985ae1db0cfd")

    depends_on("xtcdata", type=("build", "run"))
    depends_on("rapidjson", type=("build", "run"))
    depends_on("curl", type=("build", "run"))

    root_cmakelists_dir='psalg' 
