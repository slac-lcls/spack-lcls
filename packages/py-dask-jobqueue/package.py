# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDaskJobqueue(PythonPackage):
    """Deploy Dask on job queuing systems like PBS, Slurm, SGE or LSF."""

    homepage = "https://www.example.com"
    pypi = "dask-jobqueue/dask-jobqueue-0.8.2.tar.gz"

    maintainers("valmar")

    version("0.8.2", sha256="d35407a05a0534347c5d958ae749b9f8535bec529857d013b6e5649cde43914a")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-dask@22.02.0:", type="build")
    depends_on("py-distributed@22.02.0:", type="build")
