# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Psdaq(CMakePackage):
    """LCLS II Developement: PSDaq."""

    homepage = "https://github.com/slac-lcls/lcls2"
    url = "https://github.com/slac-lcls/lcls2/archive/refs/tags/4.0.0.tar.gz"

    maintainers("valmar")
  
    version("4.1.2", sha256="db2cb8f6e4050380fbe71f88afa3d3b4e5d7903d58666c5984fb591c8e06a957")
    version("4.1.1", sha256="41f99018f13f10020140982e416817b3569de53a0a44ad4dc99f03a5b5ad2ddd")
    version("4.1.0", sha256="f3f2c7850f43a2e0dbed7589ff37a706fe17e4fa07f2878dca47f6b6ea7d677b")
    version("4.0.0", sha256="f38f8c884b688c3b681fbce9be6068078f8549b05f510234a61f985ae1db0cfd")

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
    depends_on("nlohmann-json", type=("build", "run"))
    depends_on("python@3.9", type=("build", "run"))

    root_cmakelists_dir = 'psdaq'

    def setup_build_environment(self, env):
        env.append_flags("CXXFLAGS", "-I{0}/include".format(self.spec["aes-stream-drivers-headers"].prefix))
