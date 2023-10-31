# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFabio(PythonPackage):
    """I/O library for images produced by 2D X-ray detectors."""

    homepage = "https://github.com/silx-kit/fabio"
    pypi = "fabio/fabio-2023.6.0.tar.gz"

    maintainers("valmar")

    version("2023.6.0", sha256="b7b3761c965d99729712460c7043b283780157ca1fd3f7b275666a9eed6b4257")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("meson", type=("build", "run"))
    depends_on("py-meson-python", type=("build", "run"))
    depends_on("py-ninja", type=("build", "run"))
    depends_on("py-tomli", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-lxml@4.6.3:", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-hdf5plugin", type=("build", "run"))
    depends_on("py-sphinx", type=("build", "run"))
    depends_on("py-sphinxcontrib-programoutput", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme", type=("build", "run"))
