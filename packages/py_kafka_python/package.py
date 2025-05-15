# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKafkaPython(PythonPackage):
    """Pure Python client for Apache Kafka."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/dpkp/kafka-python"
    homepage = "https://www.example.com"
    pypi = "kafka_python/kafka_python-2.2.3.tar.gz"

    maintainers("valmar")

    version("2.2.3", sha256="b2d9c4e05b5cce66d46f1122992246731bbbea222b22209539f5ff6de2fd06ee")

    depends_on("py-setuptools", type="build")
