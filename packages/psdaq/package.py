# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Psdaq(CMakePackage):
    """LCLS II Developement: PSDaq."""

    homepage = "https://github.com/slac-lcls/lcls2"
    git = "https://github.com/slac-lcls/lcls2"

    maintainers("valmar")

    version("experimental", commit="97636eebb42e6648bf597bb5c8939f9b52f86632")

    depends_on("aes-stream-drivers-headers", type=("build"))
    depends_on("eigen", type=("build"))
    depends_on("psalg", type=("build", "run"))
    depends_on("xtcdata", type=("build", "run"))
    depends_on("libfabric", type=("build", "run"))
    depends_on("epics-base", type=("build", "run"))
    depends_on("prometheus-cpp", type=("build", "run"))
    depends_on("rapidjson", type=("build", "run"))
    depends_on("readline", type=("build", "run"))
    depends_on("rdma-core", type=("build", "run"))
    depends_on("libfabric", type=("build", "run"))
    depends_on("libzmq", type=("build", "run"))
    depends_on("python@3.9", type=("build", "run"))

    root_cmakelists_dir = 'psdaq'

    def setup_build_environment(self, env):
        env.append_flags("CXXFLAGS", "-I{0}/include".format(self.spec["aes-stream-drivers-headers"].prefix))
