# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpixHrM320k(PythonPackage):
    """LCLS-II Epix HR M 320k software and firmware."""

    homepage = "https://github.com/slaclab/epix-hr-m-320k"    
    url = "file:///sdf/group/lcls/ds/ana/sw/conda_bld/valmar/spack-bld/source_files/epix-hr-m-320k-1.1.5.tar.gz"
    maintainers = ["valmar", "mavaylon1"]

    version("1.1.5", sha256="953537a47e257005b0ea1e9ad580034f7c15e0c89a7a9cba593ff4cc6f4d0437")
    
    patch("setup.patch")

    depends_on("py-setuptools", type="build")
