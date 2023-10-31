# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHoloviews(PythonPackage):
    """HoloViews is an open-source Python library designed to make data analysis and visualization seamless and simple."""

    homepage = "https://www.holoviews.org"
    pypi = "holoviews/holoviews-1.15.3.tar.gz"

    maintainers("valmar")

    version("1.18.0", sha256="bab72961ab7a18794db269351d905523f2aadcad593b321512927ce93dc9df91")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-jinja2@2.0:", type=("build", "run"))
    depends_on("py-numpy@1.11.3:", type=("build", "run"))
    depends_on("py-packaging@16.8:", type=("build", "run"))
    depends_on("py-pillow@7.1.0:", type=("build", "run"))
    depends_on("py-pyct@0.4.4:", type=("build", "run"))
    depends_on("py-pyyaml@3.10:", type=("build", "run"))
    depends_on("py-tornado@5.1:", type=("build", "run"))
    depends_on("py-typing-extensions@3.10.0:", type=("build", "run"))

