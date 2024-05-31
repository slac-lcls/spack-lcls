# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCameralinkGateway(PythonPackage):
    """LCLS-II Cameralink Gateway software and firmware."""

    homepage = "https://github.com/slaclab/lcls2-timetool"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/cameralink-gateway-8.2.0.tar.gz"

    maintainers = ["valmar"]

    version("8.2.0", sha256="636c574864e8474f06962a0aceef7ef23e8a1d17a03718352b54fece7e6e330b")

    depends_on("py-setuptools", type="build")
