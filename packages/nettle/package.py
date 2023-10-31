# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.nettle import Nettle as BuiltinNettle


class Nettle(BuiltinNettle):
    """The Nettle package contains the low-level cryptographic library
    that is designed to fit easily in many contexts."""

    depends_on("openssl", type=("build", "run", "link"))
