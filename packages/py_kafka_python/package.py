# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyKafkaPython(PythonPackage):
    """Pure Python client for Apache Kafka."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/dpkp/kafka-python"
    homepage = "https://www.example.com"
    pypi = "kafka_python/kafka_python-2.2.15.tar.gz"

    maintainers("valmar")

    version("2.2.15", sha256="ie0f480a45f3814cb0eb705b8b4f61069e1be61dae0d8c69d0f1f2da33eea1bd5")

    depends_on("py-setuptools", type="build")
