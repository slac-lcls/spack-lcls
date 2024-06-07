# Copyright (c) 2024, The Board of Trustees of the Leland Stanford Junior 
# University, through SLAC National Accelerator Laboratory (subject to receipt 
# of any required approvals from the U.S. Dept. of Energy).

from spack.package import *


class PyHighRateEncoder(PythonPackage):
    """LCLS-II High Rate Encoder software and firmware."""

    homepage = "https://github.com/slaclab/high-rate-encoder-dev"
    url = "file:///sdf/group/lcls/ds/ana/sw/conda_bld/valmar/spack-bld/source_files/high-rate-encoder-dev-2.0.0.tar.gz" 

    maintainers = ["valmar","mavaylon1"]

    version("2.0.0", sha256="7bd03d867e8b25ac7ab89573b17ff9152e975cd93e72624c737681202ac90712")
    
    patch("setup.patch")
        
    depends_on("py-setuptools", type="build")
