from warnings import simplefilter

from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from semver.version import Version

simplefilter("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


__version__ = "0.1.20"
VERSION = Version.parse(__version__)
