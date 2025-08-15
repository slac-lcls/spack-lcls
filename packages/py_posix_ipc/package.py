# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyPosixIpc(PythonPackage):
    """POSIX IPC for Python."""

    homepage = "https://github.com/osvenskan/posix_ipc"
    pypi = "posix_ipc/posix_ipc-1.3.0.tar.gz"

    maintainers("valmar")

    version("1.3.0", sha256="6e559ac5bb5f6f233c396103f4868e383bbd8f4e54d20876910896f47d353448")

    depends_on("py-setuptools", type="build")
