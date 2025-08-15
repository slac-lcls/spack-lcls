# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Rogue(CMakePackage):
    """SLAC Python based hardware abstraction & data acquisition system."""

    homepage = "https://github.com/slaclab/rogue"
    url = "file:///sdf/group/lcls/ds/ana/sw/source_files/rogue-6.1.3.tar.gz"

    maintainers("valmar")

    version("6.1.3", sha256="cddc55af0ff0d3c9047fab59d2bc72c72d0217ed31d928d1c5d54d790e96ba09")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("boost+python", type = ("build", "run"))
    depends_on("libzmq", type = ("build", "run"))
    depends_on("python", type = ("build", "run"))
    depends_on("py-pyyaml", type = ("build", "run"))
    depends_on("py-parse", type = ("build", "run"))
    depends_on("py-click", type = ("build", "run"))
    depends_on("py-coverage", type = ("build", "run"))
    depends_on("py-pytest@3.6:", type = ("build", "run"))
    depends_on("py-pytest-cov", type = ("build", "run"))
    depends_on("py-sphinx", type = ("build", "run"))
    depends_on("py-sphinx-rtd-theme", type = ("build", "run"))
    depends_on("py-sphinxcontrib-napoleon", type = ("build", "run"))
    depends_on("py-breathe", type = ("build", "run"))
    depends_on("py-pyzmq", type = ("build", "run"))
    depends_on("py-pyepics", type = ("build", "run"))
    depends_on("py-p4p", type = ("build", "run"))
    depends_on("py-sqlalchemy", type = ("build", "run"))
    depends_on("py-pyserial", type = ("build", "run"))
    depends_on("py-numpy", type = ("build", "run"))
    depends_on("py-flake8", type = ("build", "run"))
    depends_on("py-gitpython", type = ("build", "run"))
    depends_on("py-pygithub", type = ("build", "run"))
    depends_on("py-pydm", type = ("build", "run"))

    def cmake_args(self):
        args = ["-DROGUE_INSTALL=system", "-DROGUE_DIR={0}".format(self.prefix), "-DCMAKE_BUILD_TYPE=RelWithDebInfo", "-DROGUE_VERSION=v{0}".format(self.version)]
        return args
    
