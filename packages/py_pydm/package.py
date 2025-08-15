# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyPydm(PythonPackage):
    """PyDM: Python Display Manager."""

    homepage = "https://github.com/slaclab/pydm"
    pypi = "pydm/pydm-1.18.1.tar.gz"

    maintainers("valmar")

    version("1.27.2", sha256="3ad2baeb84511d68a916ee267cea4406076c75926211afd7c5a342498273f5d8")

    depends_on("py-setuptools", type="build")
    depends_on("py-entrypoints", type=("build", "run"))
    depends_on("py-numpy@1.11.0:", type=("build", "run"))
    depends_on("py-pyepics@3.2.7:", type=("build", "run"))
    depends_on("py-pyqtgraph@0.12.0:", type=("build", "run"))
    depends_on("py-qtpy@2.2.0:", type=("build", "run"))
    depends_on("py-requests@1.1.0:", type=("build", "run"))
    depends_on("py-scipy@0.12.0:", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
