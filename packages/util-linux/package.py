# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.util_linux import UtilLinux as BuiltinUtilLinux


class UtilLinux(BuiltinUtilLinux):
    """Util-linux is a suite of essential utilities for any Linux system."""

    version("2.39.2", sha256="c8e1a11dd5879a2788973c73589fbcf08606e85aeec095e516162495ead8ba68")
