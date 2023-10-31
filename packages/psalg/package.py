# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Psalg(CMakePackage):
    """LCLS II Development: PSAlg."""

    homepage = "https://github.com/slac-lcls/lcls2"
    git = "https://github.com/slac-lcls/lcls2"

    maintainers("valmar")

    version("experimental", commit="97636eebb42e6648bf597bb5c8939f9b52f86632")

    depends_on("xtcdata", type=("build", "run"))
    depends_on("rapidjson", type=("build", "run"))
    depends_on("curl", type=("build", "run"))

    root_cmakelists_dir='psalg' 
