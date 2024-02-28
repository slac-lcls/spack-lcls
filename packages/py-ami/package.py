# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAmi(PythonPackage):
    """The LCLS-II online graphical analysis monitoring package.."""

    homepage = "https://github.com/slac-lcls/ami"
    url = "https://github.com/slac-lcls/ami/archive/refs/tags/2.5.0.tar.gz"

    maintainers("valmar")

    version("2.5.0", md5="84734787793b0fa420c5ae36bbbb1818")

    depends_on("python@3.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-dill", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("py-pyqtgraph", type=("build", "run"))
    depends_on("py-networkfox", type=("build", "run"))
    depends_on("py-psana", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-pint", type=("build", "run"))
    depends_on("py-qtpy", type=("build", "run"))
    depends_on("py-asyncqt", type=("build", "run"))
    depends_on("py-amityping", type=("build", "run"))
    depends_on("py-mypy", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pytest-qt", type=("build", "run"))
    depends_on("py-pytest-asyncio", type=("build", "run"))
    depends_on("py-sympy", type=("build", "run"))
    depends_on("py-pygraphviz", type=("build", "run"))
    depends_on("py-setproctitle", type=("build", "run"))
    depends_on("py-pyfftw", type=("build", "run"))
    depends_on("py-pyqode3-python", type=("build", "run"))
    depends_on("py-qtconsole", type=("build", "run"))
    depends_on("py-prometheus-client", type=("build", "run"))
    depends_on("py-p4p", type=("build", "run"))
