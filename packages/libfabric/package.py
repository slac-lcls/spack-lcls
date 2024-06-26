from spack.package import *
from spack.pkg.builtin.libfabric import Libfabric as BuiltinLibfabric


class Libfabric(BuiltinLibfabric):
    def setup_run_environment(self, env):
        pass
