from spack.package import *
from spack_repo.builtin.packages.libfabric.package import Libfabric as BuiltinLibfabric


class Libfabric(BuiltinLibfabric):
    def setup_run_environment(self, env):
        pass

    def setup_dependent_run_environment(self, env):
        pass
