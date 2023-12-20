# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPsana(PythonPackage):
    """LCLS II Developement: PSAna Python."""

    homepage = "https://github.com/slac-lcls/lcls2"
    git = "https://github.com/slac-lcls/lcls2"

    maintainers("valmar")

    version("experimental", commit="97636eebb42e6648bf597bb5c8939f9b52f86632")

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("python@3.9", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-psalg", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-bson", type=("build", "run"))
    depends_on("py-amityping", type=("build", "run"))
    depends_on("py-mypy-extensions", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("py-psmon", type=("build", "run"))
    depends_on("py-lcls-krtc", type=("build", "run"))
    depends_on("py-psmon", type=("build", "run"))
    depends_on("py-ipykernel", type=("build", "run"))
    depends_on("opencv", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pyabel", type=("build", "run"))
    depends_on("py-prometheus-client", type=("build", "run"))
    depends_on("py-kafka-python", type=("build", "run"))
    depends_on("xtcdata", type=("build", "run", "link"))
    depends_on("psalg", type=("build", "run", "link"))
    depends_on("libpressio", type=("build", "run", "link"))

    build_directory = "psana"

    def setup_build_environment(self, env):
        env.set("INSTDIR", "{0}".format(self.prefix))
        env.set("XTCDATADIR", "{0}".format(self.spec["xtcdata"].prefix))
        env.set("PSALGDIR", "{0}".format(self.spec["psalg"].prefix))
