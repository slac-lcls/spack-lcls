# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyPyepics(PythonPackage):
    """Epics Channel Access for Python."""

    homepage = "https://pyepics.github.io/pyepics/"
    pypi = "pyepics/pyepics-3.5.8.tar.gz"

    maintainers("valmar")

    version("3.5.8", sha256="d44e6ac9404b5a827a5224cde374387b47f6f3f891c8437ddbd2f9fb913bba51")
    version("3.5.7", sha256="be3fd878171a66fba42bf4051404b12b36ded8a448ac1894f0f81c9f2b330d7f")
    version("3.5.1", sha256="a4d0f2d0d163aa34a53f560519f5664a42ba96aeb19bbf92e46228f22fa87ff6")

    depends_on("py-setuptools@45:", type="build")
    depends_on("py-setuptools-scm@6.2:", type="build")
