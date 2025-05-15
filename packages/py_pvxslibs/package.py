# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPvxslibs(PythonPackage):
    """This module provides a library (libpvxs.so or pvxs.dll) and a set of CLI utilities
    acting as PVAccess protocol client and/or server. PVXS is functionally equivalent to
    the pvDataCPP and pvAccessCPP modules, which it hopes to eventually supplant."""

    homepage = "https://mdavidsaver.github.io/pvxs"
    pypi = "pvxslibs/pvxslibs-1.1.0.tar.gz"

    maintainers("valmar")

    version("1.3.3", sha256="1206bc470ffdc3d4127d1923b7e17c52b359818a9965e9d0e263ce9e7d41128b")
    version("1.3.2", sha256="f8b8b0893f866b2ff81099b45c0d7ff3d67666e962b8b5b72865993606613cb8")
    version("1.1.0", sha256="04113e92617645d915bfeef933fadf1d569aa82d64eb2cdd150192c24e21ae2f")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-dso@2.1a3:", type=("build", "run"))
    depends_on("py-epicscorelibs@7.0.3.99.2.0a1:", type=("build", "run"))
