# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBson(PythonPackage):
    """Independent BSON codec for Python that doesn’t depend on MongoDB."""

    homepage = "https://github.com/py-bson/bson"
    pypi = "bson/bson-0.5.10.tar.gz"

    maintainers("valmar")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("Apache-2.0")

    version("0.5.10", sha256="d6511b2ab051139a9123c184de1a04227262173ad593429d21e443d6462d6590")

    depends_on("py-setuptools", type="build")
    depends_on("py-python-dateutil@2.4.0:", type=("build", "run"))
    depends_on("py-six@1.9.0:", type=("build", "run"))
