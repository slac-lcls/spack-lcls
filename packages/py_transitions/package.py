# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyTransitions(PythonPackage):
    """A lightweight, object-oriented Python state machine implementation with many extensions."""

    homepage = "https://github.com/pytransitions/transitions"
    pypi = "transitions/transitions-0.9.3.tar.gz"

    maintainers("valmar")

    version("0.9.3", sha256="881fb75bb1654ed55d86060bb067f2c716f8e155f57bb73fd444e53713aafec8")

    depends_on("py-setuptools", type="build")
    depends_on("py-six", type=("build", "run"))
