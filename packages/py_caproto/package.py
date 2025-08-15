# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyCaproto(PythonPackage):
    """A bring-your-own-IO implementation of the EPICS Channel Access protocol in pure Python."""

    homepage = "https://github.com/caproto/caproto"
    pypi = "caproto/caproto-1.2.0.tar.gz"

    maintainers("valmar")

    version("1.2.0", sha256="c0d426d474e5beabf951bab78f3087519e0263f7fea80ee1887ad78ae1044e94")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-netifaces", type=("build", "run"))
    depends_on("py-dpkt", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-dpkt", type=("build", "run"))
