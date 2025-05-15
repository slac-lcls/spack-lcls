
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHdf5plugin(PythonPackage):
    """HDF5 Plugins for Windows, MacOS, and Linux."""

    homepage = "https://github.com/silx-kit/hdf5plugin"
    pypi = "hdf5plugin/hdf5plugin-4.0.1.tar.gz"

    maintainers = ["valmar"]

    version("5.1.0", sha256="cf78f1426b5868128b9ec6c498b70d6734e1dc8007a8ed1e7282954ab421b3fa")
    version("5.0.0", sha256="3bcc5c4f523953fe020a220c7b1b307c62066e39fdbdcd904fa2268db80e9dbb")
    version("4.2.0", sha256="500c3de00fb80b3a588808776e89a90e8f2fc5353f0b5e921750c93030ed2d36")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools@62.4.0:", type="build")
    depends_on("py-wheel@0.34.0:", type="build")
    depends_on("py-py-cpuinfo@9.0.0", type=("build", "run"))
    depends_on("py-sphinx", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme", type=("build", "run"))
    depends_on("py-nbsphinx", type=("build", "run"))
