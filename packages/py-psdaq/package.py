# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPsdaq(PythonPackage):
    """LCLS II Developement: PSDaq Python."""

    homepage = "https://github.com/slac-lcls/lcls2"
    git = "https://github.com/slac-lcls/lcls2"

    maintainers("valmar")

    version("experimental", commit="97636eebb42e6648bf597bb5c8939f9b52f86632")

    depends_on("py-setuptools", type="build")
    depends_on("xtcdata", type=("build", "run", "link"))
    depends_on("psalg", type=("build", "run", "link"))
    depends_on("psdaq", type=("build", "run", "link"))
    depends_on("python@3.9", type=("build", "run"))
    depends_on("py-psalg", type=("build", "run"))
    depends_on("py-p4p", type=("build", "run"))
    depends_on("py-transitions", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-amityping", type=("build", "run"))
    depends_on("py-mypy", type=("build", "run"))
    depends_on("rogue", type=("build", "run", "link"))
    depends_on("py-bluesky", type=("build", "run"))
    depends_on("py-ophyd", type=("build", "run"))
    depends_on("py-lcls2-timetool", type=("build", "run"))
    depends_on("py-posix-ipc", type=("build", "run"))
    depends_on("py-prometheus-client", type=("build", "run"))

    build_directory = 'psdaq'

    def setup_build_environment(self, env):
        env.set("INSTDIR", "{0}".format(self.prefix))
        env.set("XTCDATADIR", "{0}".format(self.spec["xtcdata"].prefix))
        env.set("PSDAQDIR", "{0}".format(self.spec["psdaq"].prefix))
