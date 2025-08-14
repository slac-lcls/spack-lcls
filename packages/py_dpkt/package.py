# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyDpkt(PythonPackage):
    """Fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols."""

    homepage = "https://github.com/kbandla/dpkt"
    pypi = "dpkt/dpkt-1.9.8.tar.gz"

    maintainers("valmar")

    version("1.9.8", sha256="43f8686e455da5052835fd1eda2689d51de3670aac9799b1b00cfd203927ee45")

    depends_on("py-setuptools", type="build")
