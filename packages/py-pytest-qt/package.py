# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.py_pytest_qt import PyPytestQt as BuiltinPyPytestQt


class PyPytestQt(BuiltinPyPytestQt):
    """A pytest plugin that allows programmers to write tests for
    PySide, PySide2 and PyQt applications.."""

    version("4.4.0", sha256="76896142a940a4285339008d6928a36d4be74afec7e634577e842c9cc5c56844")
