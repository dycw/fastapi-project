from warnings import simplefilter

from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

simplefilter("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


__version__ = "0.1.18"
