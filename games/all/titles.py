#!/usr/bin/python3
"""
Submodule containing all games from GameCollection object
"""
from ..roms import gb, gba, gbc, gcn, n3ds, n64, nds, nes, ps2, psx, snes, wii, wiiu, ps3, sms, smd, gg, psp
from .. import GameCollection
from typing import Final

GB:   Final[GameCollection] = gb.games
GBA:  Final[GameCollection] = gba.games
GBC:  Final[GameCollection] = gbc.games
GCN:  Final[GameCollection] = gcn.games
GEN:  Final[GameCollection] = smd.games
GG:   Final[GameCollection] = gg.games
N3DS: Final[GameCollection] = n3ds.games
N64:  Final[GameCollection] = n64.games
NES:  Final[GameCollection] = nes.games
NDS:  Final[GameCollection] = nds.games
PS2:  Final[GameCollection] = ps2.games
PS3:  Final[GameCollection] = ps3.games
PSX:  Final[GameCollection] = psx.games
PSP:  Final[GameCollection] = psp.games
SMS:  Final[GameCollection] = sms.games
SMD:  Final[GameCollection] = smd.games
SNES: Final[GameCollection] = snes.games
WII:  Final[GameCollection] = wii.games
WIIU: Final[GameCollection] = wiiu.games

__all__ = ["WII", "N3DS", "PS3", "PS2", "PSX", "PSP", "GBA", "WIIU", "NES", "SNES", "GBC", "GB", "N64", "GCN", "SMD", "GEN", "SMS", "GG"]

if __name__ != '__main__':
    del gb, gba, gbc, gcn, n3ds, n64, nds, nes, ps2, psx, psp, snes, wii, wiiu, ps3, sms, smd, gg
