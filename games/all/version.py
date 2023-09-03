#!/usr/bin/python3
from .. import Version
from typing import Final
"""
Module containing all versions from current module
"""
SCRIPT: Final[Version] = Version(1, 1, 0)

GB:   Final[Version] = Version(1, 0, 0)
GBA:  Final[Version] = Version(1, 0, 0)
GBC:  Final[Version] = Version(1, 0, 0)
GCN:  Final[Version] = Version(1, 0, 0)
GEN:  Final[Version] = Version(1, 0, 0)
GG:   Final[Version] = Version(1, 0, 0)
N3DS: Final[Version] = Version(2, 0, 0)
N64:  Final[Version] = Version(1, 0, 0)
NDS:  Final[Version] = Version(1, 0, 0)
NES:  Final[Version] = Version(1, 0, 0)
PS2:  Final[Version] = Version(1, 0, 0)
PS3:  Final[Version] = Version(1, 0, 0)
PSX:  Final[Version] = Version(2, 0, 0)
SMD:  Final[Version] = GEN
SMS:  Final[Version] = Version(1, 0, 0)
SNES: Final[Version] = Version(1, 0, 0)
WII:  Final[Version] = Version(1, 0, 0)
WIIU: Final[Version] = Version(1, 0, 0)

__all__ = ["SCRIPT", "WII", "N3DS", "PS2", "PSX", "GBA", "WIIU", "NES", "NDS", "SNES", "GBC", "GB", "N64", "GCN", "SMS", "SMD", "GG", "GEN"]
