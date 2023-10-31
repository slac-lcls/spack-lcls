# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.node_js import NodeJs as BuiltinNodeJs


class NodeJs(BuiltinNodeJs):
    """Node.js is an open-source, cross-platform JavaScript runtime environment."""

    patch("inttypes.patch")
