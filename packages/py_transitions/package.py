# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyTransitions(PythonPackage):
    """A lightweight, object-oriented Python state machine implementation with many extensions."""

    homepage = "https://github.com/pytransitions/transitions"
    pypi = "transitions/transitions-0.9.0.tar.gz"

    maintainers("valmar")

    version("0.9.2", sha256="2f8490dbdbd419366cef1516032ab06d07ccb5839ef54905e842a472692d4204")
    version("0.9.0", sha256="2f54d11bdb225779d7e729011e93a9fb717668ce3dc65f8d4f5a5d7ba2f48e10")

    depends_on("py-setuptools", type="build")
    depends_on("py-six", type=("build", "run"))
