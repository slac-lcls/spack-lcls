# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PySetuptoolsDso(PythonPackage):
    """Setuptools extension for building non-Python Dynamic Shared Objects."""

    homepage = "https://epics-base.github.io/setuptools_dso"
    pypi = "setuptools_dso/setuptools_dso-2.12.2.tar.gz"

    maintainers("valmar")

    version("2.12.2", sha256="7afb76f93d13ce9da24502676d8f2d4dbc3da35c6245f95f27df9fa7445079a4")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
