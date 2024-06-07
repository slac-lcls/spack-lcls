# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLcls2UdpPcieApps(PythonPackage):
    """LCLS-II UDP PCIE Apps firmware and software."""

    homepage = "https://github.com/slaclab/lcls2-udp-pcie-apps"
    url = "file:///sdf/group/lcls/ds/ana/sw/conda_bld/valmar/spack-bld/source_files/lcls2-udp-pcie-apps-2.0.0.tar.gz"
    maintainers = ["valmar", "mavaylon1"]

    version("2.0.0", sha256="12e1f24902c40b95073a7afcef2197dcb37a403a7c129cd8b415d1c54e5d41a8")

    patch("setup.patch")

    depends_on("py-setuptools", type="build")
