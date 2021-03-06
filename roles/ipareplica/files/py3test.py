#!/usr/bin/python3

# Test ipaerver python3 binding
try:
    from ipaserver.install.server.replicainstall import (  # noqa: F401
        install_check,
    )
except ImportError:
    from ipaserver.install.server.replicainstall import (  # noqa: F401
        promote_check,
    )

# Check ipapython version to be >= 4.6
from ipapython.version import NUM_VERSION, VERSION
if NUM_VERSION < 40590:
    raise Exception("ipa %s not usable with python3" % VERSION)
