#!/usr/bin/python3
"""
GAMES
Muuur - 2022
Main script to filter games in console database
See `game-downloader -h` for help
"""
# ----------------------------------------------------------------

from sys import argv, stderr
from os import sep
from sys import stdin, argv
from urllib.error import HTTPError
from colorama import Fore, init, Style

try:
    from games.all import version, titles
    from games import check_updates
except ModuleNotFoundError:
    init()
    stderr.write(f"{Style.BRIGHT}games{Style.RESET_ALL} was {Fore.RED}not found{Fore.RESET}, download it from {Style.BRIGHT}github{Style.RESET_ALL} or check the {Fore.LIGHTCYAN_EX}python path{Fore.RESET}\n")
    exit(2)
except TypeError:
    init()
    stderr.write(f"{Style.BRIGHT}game-downloader{Style.RESET_ALL} is {Fore.RED}not supported{Fore.RESET} before {Fore.LIGHTCYAN_EX}python{Fore.RESET} {Style.BRIGHT}3.10{Style.RESET_ALL} due to typing annotations.\n")
    exit(2)

def main(argv: list[str]=argv) -> int:
    """Main script function to download games from database"""
    init(autoreset=True)
    if len(argv) == 1 or argv[1].lower() in ("-h", "--help", "-?"):
        print(f"""Usage: {Style.BRIGHT}games{Style.RESET_ALL} [ --platform ] {{ query }}\n
		Download games for different game platforms from custom database\n
		{Style.BRIGHT}platform{Style.RESET_ALL}:
		    {Style.BRIGHT}-g{Style.RESET_ALL},  {Style.BRIGHT}--gb{Style.RESET_ALL}     GameBoy
		    {Style.BRIGHT}-a{Style.RESET_ALL},  {Style.BRIGHT}--gba{Style.RESET_ALL}    GameBoy Advance
		    {Style.BRIGHT}-k{Style.RESET_ALL},  {Style.BRIGHT}--gbc{Style.RESET_ALL}    GameBoy Color
		    {Style.BRIGHT}-c{Style.RESET_ALL},  {Style.BRIGHT}--gcn{Style.RESET_ALL}    Game Cube
		    {Style.BRIGHT}-d{Style.RESET_ALL},  {Style.BRIGHT}--gen{Style.RESET_ALL}    Genesis
		    {Style.BRIGHT}-g{Style.RESET_ALL},  {Style.BRIGHT}--gg{Style.RESET_ALL}     Game Gear
		    {Style.BRIGHT}-3{Style.RESET_ALL},  {Style.BRIGHT}--3ds{Style.RESET_ALL}    Nintendo 3DS
		    {Style.BRIGHT}-6{Style.RESET_ALL},  {Style.BRIGHT}--n64{Style.RESET_ALL}    Nintendo 64
		    {Style.BRIGHT}-d{Style.RESET_ALL},  {Style.BRIGHT}--nds{Style.RESET_ALL}    Nintendo DS
		    {Style.BRIGHT}-e{Style.RESET_ALL},  {Style.BRIGHT}--nes{Style.RESET_ALL}    Nintendo Entertainment system
		    {Style.BRIGHT}-d{Style.RESET_ALL},  {Style.BRIGHT}--smd{Style.RESET_ALL}    Sega Mega Drive (same as Genesis)
		    {Style.BRIGHT}-m{Style.RESET_ALL},  {Style.BRIGHT}--sms{Style.RESET_ALL}    Sega Master System
		    {Style.BRIGHT}-2{Style.RESET_ALL},  {Style.BRIGHT}--ps2{Style.RESET_ALL}    Play Station 2
		    {Style.BRIGHT}-3{Style.RESET_ALL},  {Style.BRIGHT}--ps3{Style.RESET_ALL}    Play Station 3
		    {Style.BRIGHT}-x{Style.RESET_ALL},  {Style.BRIGHT}--psx{Style.RESET_ALL}    Play Station 1
		    {Style.BRIGHT}-s{Style.RESET_ALL},  {Style.BRIGHT}--snes{Style.RESET_ALL}   Super Nintendo Entertainment System
		    {Style.BRIGHT}-w{Style.RESET_ALL},  {Style.BRIGHT}--wii{Style.RESET_ALL}    Nintendo wii
		    {Style.BRIGHT}-u{Style.RESET_ALL},  {Style.BRIGHT}--wiiu{Style.RESET_ALL}   Nintendo Wii U\n
		         {Style.BRIGHT}--update{Style.RESET_ALL} Check if updates are available\n
		{Style.BRIGHT}query{Style.RESET_ALL}:           Game title pattern to search in database\n
		If no arguments are provided, the program interact with the user
		If no game console is introduced, the program shows this help\n""".replace("\t", ""))
        return 0
    elif argv[1].lower() in ("-w", '--wii'):
        games = titles.WII
    elif argv[1].lower() in ("-m", '--sms', '--ms'):
        games = titles.SMS
    elif argv[1].lower() in ("-d", '--gen', '--md', '--smd'):
        games = titles.SMD
    elif argv[1].lower() in ("-g", '--gg', '--sgg'):
        games = titles.GG
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
        games = titles.GBC
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
    elif argv[1].lower() in ('-x', '--psx', '--ps1', '--play', '--play1'):
        games = titles.PSX
    elif argv[1].lower() in ("-v", "--version"):
        print(f"{Style.BRIGHT}games{Style.RESET_ALL} version {version.SCRIPT} Muuur software - 2022")
        exit(0)
    elif argv[1].lower() == "--update":
        check_updates()
        exit(0)
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
            try:
                return 1 - int(game.download(verbose=True, error=True))
            except HTTPError:
                stderr.write(f"URL {Fore.RED}not found{Fore.RESET} name={Fore.LIGHTCYAN_EX}{game.get_title()}{Fore.RESET}, url={Fore.LIGHTBLUE_EX}{game.get_url()}{Fore.RESET}\n")
                return 1
    return 0

if __name__ == '__main__':
    exit(main())
