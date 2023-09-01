#!/usr/bin/python3
"""
GAMES
Muuur - 2022
Main script to filter games in console database
See `games -h` for help
"""
# ----------------------------------------------------------------
# ? Version history
# ! 1.1   Bugs fix and better names visibility
# ! 1.2   Added cURL verification
# ! 1.3   Stop and resume option
# ! 1.3.1 \n when stdout is not a tty (pipes)
# ! 1.4   Added PSX games
# ! 2.0   Added sha, changed cURL to python-urllib, removed stop-resume option, added update option
# ! future -> Add -# to automate assume-yes on # option

from sys import argv, stderr
from os import sep
from sys import stdin

try:
    from games.all import version, titles
except ModuleNotFoundError:
    stderr.write("Games was not found, download it from github or check the python path\n")
    exit(2)

def main() -> int:
    if len(argv) == 1 or argv[1].lower() in ("-h", "--help", "-?"):
        print("""Usage: games [ platform ] [ query ]\n
		Download games for different game platforms\n
		platform:
		    -e,  --nes   Nintendo Entertainment system
		    -s,  --snes  Super Nintendo Entertainment System
		    -g,  --gb    GameBoy
		    -k,  --gbc   GameBoy Color
		    -6,  --n64   Nintendo 64
		    -a,  --gba   GameBoy Advance
		    -c,  --gcn   Game Cube
		    -d,  --nds   Nintendo DS
		    -w,  --wii   Nintendo wii
		    -3,  --3ds   Nintendo 3DS
		    -u,  --wiiu  Nintendo Wii U
		    -x,  --psx   Play Station 1
		    -2,  --ps2   Play Station 2
            -3,  --ps3   Play Station 3\n
		query:           Game title pattern to search in database\n
		If no arguments are provided, the program interact with the user
		If no game console is introduced, the program shows this help\n""".replace("\t", ""))
        return 0
    elif argv[1].lower() in ("-w", '--wii'):
        games = titles.WII
    elif argv[1].lower() in ('-3', "--3ds", '--cia'):
        games = titles.N3DS 
    elif argv[1].lower() in ('-d', '--ds', '-ds', '--nds'):
        games = titles.NDS
    elif argv[1].lower() in ('-2', '--ps2', '--play2'):
        games = titles.PS2
    elif argv[1].lower() in ('-3', '--ps3', '--play3'):
        games = titles.PS3
    elif argv[1].lower() in ("-g", '--gb', '-gb'):
        games = titles.G
    elif argv[1].lower() in ("-k", '--gbc'):
        # games = titles.GBC
        raise NotImplementedError("Game Boy Color database is under maintenance")
    elif argv[1].lower() in ("-a", '--gba'):
        games = titles.GBA
    elif argv[1].lower() in ("-u", "--wiiu", "--wu"):
        games = titles.WIIU 
    elif argv[1].lower() in ("-e", "--nes"):
        games = titles.NES
    elif argv[1].lower() in ("-s", "--snes"):
        games = titles.SNES 
    elif argv[1].lower() in ("-c", "--gc", '--gcn'):
        games = titles.GCN
    elif argv[1].lower() in ("-6" '--64', "--n64"):
        games = titles.N64
    elif argv[1].lower() in ('-x', '--psx', '--ps1'):
        games = titles.PSX
    elif argv[1].lower() in ("-v", "--version"):
        print(f"games version {version.SCRIPT} - database version {version.DATABASE}\n\nMuuur software - 2022")
    else:
        stderr.write(f"Game console argument needed and not provided, try with `{argv[0][argv[0].rfind(sep) + 1:]} --help`\n")
        return 1

    query = (" ".join(argv[2:]) if len(argv) > 2 else input("Input search keywords: "))

    for game in games.filter(query):
        try:
            resp = input(game.get_title() + (' (Y/N): ' if stdin.isatty() else '\n'))
        except (KeyboardInterrupt, EOFError, OSError):
            stderr.write("\n")
            return 130
        if len(resp) >= 1 and resp.upper()[0] in 'SY':
            print(end="\n")
            return 1 - int(game.download(verbose=True, error=True))
    return 0

if __name__ == '__main__':
    exit(main())
