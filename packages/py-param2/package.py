# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyParam2(PythonPackage):
    """Param is a library providing Parameters: Python attributes extended to have features such
    as type and range checking, dynamically generated values, documentation strings, default
    values, etc., each of which is inherited from parent classes if not specified in a
    subclass."""

    homepage = "https://www.example.com"
    pypi = "param2/param2-2.0.0.dev2.tar.gz"

    maintainers("valmar")

    version("2.0.0.dev2", sha256="3dded699ed067c2da26e995562f34df866d88c13f1abdf50843cbe764a10bfda")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
