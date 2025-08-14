# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.libfabric.package import Libfabric as BuiltinLibfabric
from spack.package import *


class Libfabric(BuiltinLibfabric):
    def setup_run_environment(self, env):
        pass

    def setup_dependent_run_environment(self, env):
        pass
