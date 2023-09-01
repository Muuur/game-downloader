#!/usr/bin/python3
"""
Submodule containing all games
"""
from ..roms import gb, gba, gbc, gcn, n3ds, n64, nds, nes, ps2, psx, snes, wii, wiiu, ps3

WII  = wii.games
N3DS = n3ds.games
PS3  = ps3.games
PS2  = ps2.games
PSX  = psx.games
GBA  = gba.games
WIIU = wiiu.games
NES  = nes.games
NDS  = nds.games
SNES = snes.games
GBC  = gbc.games
GB   = gb.games
N64  = n64.games
GCN  = gcn.games

__all__ = ["WII", "N3DS", "PS3", "PS2", "PSX", "GBA", "WIIU", "NES", "SNES", "GBC", "GB", "N64", "GCN"]

if __name__ != '__main__':
    del gb, gba, gbc, gcn, n3ds, n64, nds, nes, ps2, psx, snes, wii, wiiu, ps3
