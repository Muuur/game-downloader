#!/usr/bin/python3
from .. import Link
from typing import Final
"""
Module containing all baseurl from database
"""

GB:   Final[Link] = Link("https://ia803200.us.archive.org/23/items/nointro.gb")
GBA:  Final[Link] = Link("https://ia801707.us.archive.org/23/items/nointro.gba")
GBC:  Final[Link] = Link("https://ia804606.us.archive.org/35/items/nintendo-game-boy-color-by-retro-raven")
GCN:  Final[Link] = Link("https://ia902806.us.archive.org/25/items/zoocube/")
GEN:  Final[Link] = Link("https://ia801707.us.archive.org/21/items/nointro.md")
GG:   Final[Link] = Link("https://ia601909.us.archive.org/1/items/nointro.gg")
N3DS: Final[Link] = Link("https://ia802909.us.archive.org/28/items/nintendo-3ds-complete-collection")
N64:  Final[Link] = Link("https://ia601908.us.archive.org/0/items/nointro.n64")
NDS:  Final[Link] = Link("https://ia803406.us.archive.org/12/items/nds-romset")
NES:  Final[Link] = Link("https://ia804606.us.archive.org/13/items/nes-roms")
SMD:  Final[Link] = GEN
SMS:  Final[Link] = Link("https://ia803204.us.archive.org/17/items/nointro.ms-mkiii")
SNES: Final[Link] = Link("https://ia801707.us.archive.org/6/items/nointro.snes")
PS2:  Final[Link] = Link("https://archive.org/download/PS2_COLLECTION_PART")
PS3:  Final[Link] = Link("https://archive.org/details/PS3_NOINTRO_EUR_")
PSX:  Final[Link] = Link("https://archive.org/download/redump.psx")
PSP:  Final[Link] = Link("https://archive.org/download/redump.psp")
WII:  Final[Link] = Link("https://archive.org/download/wiieuroperedump")
WIIU: Final[Link] = Link("https://ia902507.us.archive.org/2/items/wii-u-romset-iso-dump-eu-us")

__all__ = ["WII", "N3DS", "NDS", "PS2", "PS3", "PSX", "PSP", "GBA", "WIIU", "NES", "SNES", "GBC", "GB", "N64", "GCN", "SMD", "SMS", "GEN", "GG"]
