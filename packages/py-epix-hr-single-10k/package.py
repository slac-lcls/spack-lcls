# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpixHrSingle10k(PythonPackage):
    """LCLS-II Epix HR Singe 10k software and firmware.."""

    homepage = "https://github.com/slaclab/epix-hr-single-10k"
    url = "file:///sdf/group/lcls/ds/ana/sw/conda_bld/valmar/spack-bld/source_files/epix-hr-single-10k-1.3.4.tar.gz"

    maintainers = ["valmar"]

    version("1.3.4", sha256="9056f270451c4a2044833a35836e183789c170c83999d14b363121d3c0a4b9a1")
    
    patch("setup.patch")

    depends_on("py-setuptools", type="build")
