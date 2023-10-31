# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PrometheusCpp(CMakePackage):
    """Prometheus client library for modern C++."""

    homepage = "https://github.com/jupp0r/prometheus-cpp"
    git = "https://github.com/jupp0r/prometheus-cpp"

    maintainers("valmar")

    version("1.1.0", tag="v1.1.0", submodules=True)

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS=ON", "-DENABLE_PUSH=ON", "-DENABLE_COMPRESSION=ON"]
        return args
