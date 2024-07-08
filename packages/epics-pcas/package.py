# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.epics_pcas import EpicsPcas as BuiltinEpicsPcas

class EpicsPcas(BuiltinEpicsPcas):

    depends_on("perl", type="run")

    def get_epics_host_arch(self):
        perl = which("perl", required=True)
        return perl("%s/perl/EpicsHostArch.pl" % self.spec['epics-base'].prefix.lib, output=str, error=str).strip()

    def setup_run_environment(self, envmod):
        epics_host_arch = self.get_epics_host_arch()
        envmod.prepend_path("PATH", join_path(self.prefix.bin, epics_host_arch))
