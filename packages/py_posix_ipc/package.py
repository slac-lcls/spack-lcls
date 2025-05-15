# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPosixIpc(PythonPackage):
    """POSIX IPC for Python."""

    homepage = "https://github.com/osvenskan/posix_ipc"
    pypi = "posix_ipc/posix_ipc-1.1.0.tar.gz"

    maintainers("valmar")

    version("1.2.0", sha256="b7444e2703c156b3cb9fcb568e85d716232f3e78f04529ebc881cfb2aedb3838")
    version("1.1.1", sha256="e2456ba0cfb2ee5ba14121450e8d825b3c4a1461fca0761220aab66d4111cbb7")
    version("1.1.0", sha256="f86a15b32b38573c78e305ebd9100d8198a3d9facc03ffafe39edc35833738e3")

    depends_on("py-setuptools", type="build")
