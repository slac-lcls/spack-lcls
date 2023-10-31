# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.sz3 import Sz3 as BuiltinSz3


class Sz3(BuiltinSz3):
    """A generic abstraction for the compression of dense tensors."""

    patch("uint8_t.patch")
