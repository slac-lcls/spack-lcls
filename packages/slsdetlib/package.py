# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Slsdetlib(CMakePackage):
    """SLS Detector Package."""

    homepage = "https://github.com/slsdetectorgroup/slsDetectorPackage"
    url = "https://github.com/slsdetectorgroup/slsDetectorPackage/archive/refs/tags/9.0.0.tar.gz"

    maintainers("valmar")

    version("9.0.0", sha256="35758052864ee06497e16be0b298c798cd089982c3a31e6a9b98a56ea0176626")

    depends_on("libbsd", type=("build", "run"))
    depends_on("libmd", type=("build", "run"))

    def cmake_args(self):
        args = [f"-DCMAKE_CXX_FLAGS=-I{self.spec['libbsd'].prefix.include} -L{self.spec['libbsd'].prefix.lib} -L{self.spec['libmd'].prefix.lib} "
                "-DSLS_USE_TEXTCLIENT=ON", "-DSLS_USE_RECEIVER=OFF", "-DSLS_USE_GUI=OFF",
                "-DSLS_USE_MOENCH=OFF", "-DSLS_USE_TESTS=OFF", "-DSLS_USE_PYTHON=OFF",
                "-DCMAKE_BUILD_TYPE=Release", "-DSLS_USE_HDF5=OFF"]
   
        return args
