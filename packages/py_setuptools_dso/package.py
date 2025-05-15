# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySetuptoolsDso(PythonPackage):
    """Setuptools extension for building non-Python Dynamic Shared Objects."""

    homepage = "https://mdavidsaver.github.io/setuptools_dso"
    pypi = "setuptools_dso/setuptools_dso-2.6.tar.gz"

    maintainers("valmar")

    version("2.12.2", sha256="7afb76f93d13ce9da24502676d8f2d4dbc3da35c6245f95f27df9fa7445079a4")
    version("2.11", sha256="953e66a744e21dbbe4ad73e22b9fee2e47bae739f26bc63ab37473a45b975456")
    version("2.6", sha256="d061c0bc2a9b9d784e42d6ef71c6cd5bf5e1b5c3ab2aa43e940ee687ea2c6e23")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
