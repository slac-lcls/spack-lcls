# Copyright (c) 2022, The Board of Trustees of the Leland Stanford Junior 
# University, through SLAC National Accelerator Laboratory (subject to receipt 
# of any required approvals from the U.S. Dept. of Energy).

from spack.package import *


class PyEpix100aGen2(PythonPackage):
    """LCLS-II Epix 100A Gen2  software and firmware."""

    homepage = "https://github.com/slaclab/epix-100a-gen2"    
    url = "file:///sdf/group/lcls/ds/ana/sw/conda_bld/valmar/spack-bld/source_files/epix-100a-gen2-1.0.1.tar.gz"
    maintainers = ["valmar", "mavaylon1"]

    version("1.0.1", sha256="26e9ffd88c57eb95d2350b0bfab492834112c3f6b653ac9e081b806cc967f45d")

    depends_on("py-setuptools", type="build")
