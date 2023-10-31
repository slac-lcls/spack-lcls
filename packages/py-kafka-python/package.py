# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKafkaPython(PythonPackage):
    """Pure Python client for Apache Kafka."""

    homepage = "https://www.example.com"
    pypi = "kafka-python/kafka-python-2.0.2.tar.gz"

    maintainers("valmar")

    version("2.0.2", sha256="04dfe7fea2b63726cd6f3e79a2d86e709d608d74406638c5da33a01d45a9d7e3")

    depends_on("py-setuptools", type="build")
