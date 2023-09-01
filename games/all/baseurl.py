#!/usr/bin/python3
from .. import Link
"""
Module containing all baseurl from database
"""

WII  = Link("https://archive.org/download/wiieuroperedump")
N3DS = Link("https://archive.org/download")
# NDS = Link("https://archive.org/download/nds-romset")
NDS  = Link("https://ia803406.us.archive.org/12/items/nds-romset")
PS3  = Link("https://archive.org/details/PS3_NOINTRO_EUR_")
PS2  = Link("https://archive.org/download/PS2_COLLECTION_PART")
PSX  = Link("https://archive.org/download/Centuron-PSX")
GBA  = Link("https://archive.org/download/nointro.gba")
WIIU = Link("https://archive.org/download/wii-u-romset-iso-dump-eu-us")
# NES = Link("https://archive.org/download/nes-roms")
NES  = Link("https://ia804606.us.archive.org/13/items/nes-roms")
# SNES = Link("https://archive.org/download/nointro.snes")
SNES = Link("https://ia801707.us.archive.org/6/items/nointro.snes")
# GBC = Link("https://archive.org/download/nintendo-game-boy-color-by-retro-raven/")
GBC  = Link("https://ia804606.us.archive.org/35/items/nintendo-game-boy-color-by-retro-raven")
# GB = Link("https://archive.org/download/nointro.gb")
GB   = Link("https://ia803200.us.archive.org/23/items/nointro.gb")
# N64 = Link()"https://archive.org/download/nointro.n64")
N64  = Link("https://ia601908.us.archive.org/0/items/nointro.n64")
GCN  = Link("https://archive.org/download/rr-nintendo-gamecube/europe")

__all__ = ["WII", "N3DS", "NDS", "PS2", "PSX", "GBA", "WIIU", "NES", "SNES", "GBC", "GB", "N64", "GCN"]
