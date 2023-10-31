# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCaproto(PythonPackage):
    """A bring-your-own-IO implementation of the EPICS Channel Access protocol in pure Python."""

    homepage = "https://github.com/caproto/caproto"
    pypi = "caproto/caproto-1.1.0.tar.gz"

    maintainers("valmar")

    version("1.1.0", sha256="7033a8c60387688f14e556f18697137f2479537a36b224f7c1db8b73974cecd2")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pip@9.0.1:", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-netifaces", type=("build", "run"))
    depends_on("py-dpkt", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
