# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpixHrSingle10k(PythonPackage):
    """LCLS-II Epix HR Singe 10k software and firmware.."""

    homepage = "https://github.com/slaclab/epix-hr-single-10k"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/epix-hr-single-10k-1.0.9.tar.gz"

    maintainers = ["valmar"]

    version("1.0.9", sha256="492ede2e48593a7102a2de12f3ebc8d6dee2d5382a064ffe2ea73a1bb97c09b6")
    
    patch("setup.patch")

    depends_on("py-setuptools", type="build")
