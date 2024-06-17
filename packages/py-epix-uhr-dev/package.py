# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpixUhrDev(PythonPackage):
    """LCLS-II Epix UHR software and firmware.."""

    homepage = "https://github.com/slaclab/epix-uhr-dev"
    url = "file:///sdf/group/lcls/ds/ana/sw/source_files/epix-uhr-dev-1.0.3.tar.gz"

    maintainers = ["valmar"]

    version("1.0.3", sha256="6c96f69743e25ceb3c4210e0b7a0af0fd37992ffb68c9df4bc58585bcaf37c55")
    
    patch("setup.patch")

    depends_on("py-setuptools", type="build")
