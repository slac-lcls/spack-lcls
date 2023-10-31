# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.epics_base import EpicsBase as BuiltinEpicsBase

class EpicsBase(BuiltinEpicsBase):
    """This is the main core of EPICS, the Experimental Physics and Industrial
    Control System, comprising the build system and tools, common and OS-interface
    libraries, network protocol client and server libraries, static and run-time
    database access routines, the database processing code, and standard record,
    device and driver support."""

    def edit(self, spec, prefix):
        common_linux = FileFilter("configure/CONFIG.gnuCommon")
        common_linux.filter("CC = $(GNU_BIN)/$(CMPLR_PREFIX)gcc$(CMPLR_SUFFIX)", "CC = gcc", string=True)
        common_linux.filter("CCC = $(GNU_BIN)/$(CMPLR_PREFIX)g++$(CMPLR_SUFFIX)", "CCC = g++", string=True)
        common_linux.filter("AR = $(GNU_BIN)/$(CMPLR_PREFIX)ar$(CMPLR_SUFFIX) -rc", "AR = ar -rc", string=True)
        common_linux.filter("LD = $(GNU_BIN)/$(CMPLR_PREFIX)ld$(CMPLR_SUFFIX) -r", "LD = ld -r", string=True)
        common_linux.filter("RANLIB = $(GNU_BIN)/$(CMPLR_PREFIX)ranlib$(CMPLR_SUFFIX)", "RANLIB = ranlib", string=True)
        common = FileFilter("configure/CONFIG_COMMON")
        common.filter("PERL = perl -CSD", "PERL = perl", string=True)
