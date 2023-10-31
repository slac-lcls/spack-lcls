# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyopengl(PythonPackage):
    """Standard OpenGL bindings for Python."""

    homepage = "https://pyopengl.sourceforge.net"
    pypi = "PyOpenGL/PyOpenGL-3.1.7.tar.gz"

    maintainers("valmar")

    version("3.1.7", sha256="eef31a3888e6984fd4d8e6c9961b184c9813ca82604d37fe3da80eb000a76c86")

    depends_on("py-setuptools", type="build")
