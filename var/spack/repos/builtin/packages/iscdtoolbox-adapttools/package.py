# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class IscdtoolboxAdapttools(CMakePackage):
    """AdaptTools is a set of tools for mesh adaptation in two and three dimensions."""

    homepage = "https://github.com/ISCDtoolbox"
    url = "https://github.com/ISCDtoolbox/AdaptTools/archive/refs/heads/master.zip"
    git = "https://github.com/ISCDtoolbox/AdaptTools.git"

    maintainers("jcortial-safran")

    version("master", branch="master")

    depends_on("iscdtoolbox-commons")

    patch("user-defined-prefix-path.patch")
