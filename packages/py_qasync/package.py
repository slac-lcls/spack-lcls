# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyQasync(PythonPackage):
    """Python library for using asyncio in Qt-based applications."""

    homepage = "https://github.com/CabbageDevelopment/qasync"
    pypi = "qasync/qasync-0.27.1.tar.gz"

    maintainers("valmar")

    license("BSD-2-Clause license", checked_by="github_user1")

    version("0.27.1", sha256="8dc768fd1ee5de1044c7c305eccf2d39d24d87803ea71189d4024fb475f4985f")

    depends_on("py-poetry-core", type="build")
