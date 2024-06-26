# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import pathlib
import shutil
from spack.package import *


class AesStreamDriversHeaders(Package):
    """Headers for streaming kernel drivers (PGP, AxiStream, ExoTem)."""

    homepage = "https://github.com/slaclab/aes-stream-drivers"
    url = "https://github.com/slaclab/aes-stream-drivers/archive/refs/tags/5.17.3.tar.gz"

    maintainers("valmar")

    version("5.19.1", sha256="27bdd0c37a34a184c0a7eab9941091e3138a8b3d3d55ac3062c13b39f4c9a8fb")
    version("5.17.3", sha256="f649de81143b8afe3c1c148aa6b2949357d719737aae0b0443500af4d8fd99cd")

    def install(self, spec, prefix):
        base_path = pathlib.Path(prefix)

        pathlib.Path(base_path / "include").mkdir(parents=True)

        for file_path in pathlib.Path("include").rglob("*"):
            shutil.copyfile(file_path, base_path / file_path )
