# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class IscdtoolboxMedit(CMakePackage):
    """Medit is an OpenGL-based scientific visualization software"""

    homepage = "https://github.com/ISCDtoolbox"
    url = "https://github.com/ISCDtoolbox/Medit/archive/refs/heads/master.zip"
    git = "https://github.com/ISCDtoolbox/Medit.git"

    maintainers("jcortial-safran")

    version("master", branch="master")

    depends_on("gl")
    depends_on("freeglut")

    patch("user-defined-prefix-path.patch")
