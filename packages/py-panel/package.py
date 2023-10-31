# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.py_panel import PyPanel as BuiltinPyPanel


class PyPanel(BuiltinPyPanel):
    """A high level app and dashboarding solution for Python."""

    homepage = "http://panel.holoviz.org/"
    pypi = "panel/panel-0.14.4.tar.gz"

    version("0.14.4", sha256="b853d2f53d7738ec6372525360c5bf9427a71ed990685ccac703bc9b442e9951")

    depends_on("node-js@14:", type="build")
