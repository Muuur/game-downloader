#!/usr/bin/python3
"""This python script install the games module and the game-downloader script"""
from sys import stderr, version_info, path
from os import getenv, system, name as osname, symlink
from pathlib import Path
from shutil import copy, copytree
from games.all.version import SCRIPT

try:
    import colorama
except ModuleNotFoundError:
    from pip import main as pip_main
    pip_main(["install", "-r", "requirements.txt"])

from colorama import Fore, Style, init

def main() -> int:
    """Main function for install in Linux and Windows. MacOS is not yet supported."""
    init(autoreset=True)
    print(f"> Installing {Fore.LIGHTGREEN_EX}dependencies{Fore.RESET}")
    user = getenv("USER")
    ospath = getenv("PATH")

    vernum = f'python{version_info.major}.{version_info.minor}'
    if osname == 'nt':
        from winreg import HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, OpenKey, KEY_READ, KEY_WRITE, QueryValueEx, REG_SZ, SetValueEx
        admin = system("net session > NUL 2> NUL") == 0

        loc = Path(fr'{getenv("systemdrive")}\Program files\game-downloader' if admin else fr'{getenv("userprofile")}/AppData/local/game-downloader')
        if not loc.exists():
            print(f">> Creating {Fore.BLUE}{Style.BRIGTH}game directory{Style.RESET_ALL} in", loc)
            loc.mkdir()
        try:
            print(f">> {Fore.LIGHTGREEN_EX}Copying{Fore.RESET} necessary {Fore.LIGHTGREEN_EX}{Style.BRIGHT}files{Style.RESET_ALL}")
            copytree("games", loc / "games")
            copytree("dist-info", loc / f'games-{SCRIPT}.dist-info')
            copy("LICENSE", loc / f'games-{SCRIPT}.dist-info' / 'LICENSE')
            copy("README.md", loc / f'games-{SCRIPT}.dist-info' / 'README.md')
            copy("main.py", loc / "main.py")
            symlink(loc / "smd.py", loc / "gen.py")
        except FileExistsError:
            stderr.write(f"{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}:The package is already installed\n")
            return 1
        except KeyboardInterrupt:
            stderr.write(f"Package installation {Fore.RED}cancelled{Fore.RESET}, {Fore.LIGHMAGENTA_EX}exiting{Fore.RESET} . . .\n")
            return 1

        print(f">>> {Fore.LIGHTGREEN_EX}Creating{Fore.RESET} bat launcher")
        with open(loc / "game-downloader.bat", 'w') as batfile, open(loc / f'games-{SCRIPT}.dist-info' / 'INSTALLER', 'w') as installer:
            batfile.write("@echo off\nset PYTHONPATH=%~dp0\npython -h > NUL 2> NUL || goto :nopy\npython main.py %*\nexit /b\n\n:nopy\necho Python is not installed or in path\ngoto :eof\n")
            installer.write('install.py')

        print(f">>>> {Fore.LIGHTGREEN_EX}Adding{Fore.RESET} game-downloader to {Fore.LIGHTCYAN_EX}path{Fore.RESET}")
        with OpenKey(*[(HKEY_CURRENT_USER, "Environment"), (HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment")][int(admin)], access=KEY_READ | KEY_WRITE) as key:
            try:
                result = QueryValueEx(key, "PATH")
                value = result[0]
                value += f";{loc}"
            except FileNotFoundError:
                value = str(loc)

            try:
                SetValueEx(key, "PATH", 0, REG_SZ, value)
            except PermissionError:
                stderr.write(f"{Fore.RED}Error{Fore.RESET}: Adding game-downloader to {Fore.LIGHTCYAN_EX}path{Fore.RESET} failed, {Fore.LIGHTGREEN_EX}add it manually{Fore.RESET} using system variables application\n")

            print(f">>>>> {Fore.LIGHTGREEN_EX}Adding{Fore.RESET} games to {Fore.LIGHTCYAN_EX}python path")
            try:
                result = QueryValueEx(key, "PYTHONPATH")
                value = result[0]
                value += f";{loc}"
            except FileNotFoundError:
                value = str(loc)

            try:
                SetValueEx(key, "PYTHONPATH", 0, REG_SZ, value)
            except PermissionError:
                stderr.write(f"{Fore.RED}Error{Fore.RESET}: Adding games to {Fore.LIGHTBLACK_EX}python path{Fore.RESET} failed, {Fore.LIGHTGREEN_EX}add it manually{Fore.RESET} using system variables application.\n")
                return 1
        print(f">>>>>> The package is {Fore.LIGHTGREEN_EX}succesfully{Fore.RESET} installed.\nTry it typing {Style.BRIGHT}`game-downloader --help`{Style.RESET_ALL} from your command-line.")
        return 0
    else:
        from os import getuid
        sudo = getuid() == 0
        loc = Path(f'/usr/local/lib/{vernum}/dist-packages' if sudo else f'/home/{user}/.local/lib/{vernum}/site-packages')
        if not loc.is_dir():
            if sudo:
                loc = Path(f'/usr/lib/python{version_info.major}/dist-packages')
            
            if loc not in path or not loc.is_dir():
                stderr.write(f"{Fore.RED}Error{Fore.RESET}: Could not install the package in {Fore.LIGHTBLUE_EX}{loc}{Fore.RESET} because the {Fore.LIGHTBLUE_EX}directory{Fore.RESET} is not in {Fore.LIGHTCYAN_EX}python path\n")
                return 1
            else:
                stderr.write(f"{Fore.RED}Error{Fore.RESET}: Could not install the package in {Fore.LIGHTBLUE_EX}{loc}{Fore.RESET} because the requested {Fore.LIGHTBLUE_EX}directory{Fore.RESET} {Fore.RED}don't exists\n")
                return 1

        print(f">> {Fore.LIGHTGREEN_EX}Installing{Fore.RESET} package in {Fore.LIGHTBLUE_EX}{loc}{Fore.RESET}")
        try:
            copytree("games", loc / "games")
            copytree("dist-info", loc / f'games-{SCRIPT}.dist-info')
            copy("LICENSE", loc / f'games-{SCRIPT}.dist-info' / 'LICENSE')
            copy("README.md", loc / f'games-{SCRIPT}.dist-info' / 'README.md')
            symlink("smd.py", loc / "gen.py")
            with open(loc / f'games-{SCRIPT}.dist-info' / 'INSTALLER', 'w') as installer:
                installer.write('install.py')
        except FileExistsError:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: The package is already installed\n")
        except PermissionError:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: The package cannot be installed in {gamedir} due to permissions\n")
            return 1
        except OSError:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: The package cannot be installed in {loc} due to an OS error, maybe you have {Fore.LIGHTMAGENTA_EX}no free inodes?\n")
            return 1
        except KeyboardInterrupt:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: Package installation cancelled, {Fore.LIGHTMAGENTA_EX}exiting{Fore.RESET} . . .\n")
            return 1

        gamedir = Path("/usr/games" if sudo else f'/home/{user}/.local/bin')
        print(f">>> {Fore.LIGHTGREEN_EX}Installing{Fore.RESET} script in {Fore.LIGHTBLUE_EX}{gamedir}")
        if gamedir.as_posix() not in ospath.split(":"):
            stderr.write(f'Script installation {Fore.RED}failed{Fore.RESET}.\n{Fore.LIGHTBLUE_EX}{gamedir}{Fore.RESET} is not in {Fore.LIGHTCYAN_EX}path{Fore.RESET}.\nCopy the {Fore.LIGHTGREEN_EX}main.py{Fore.RESET} script as {Fore.LIGHTGREEN_EX}game-downloader{Fore.RESET} in your desired destination to be able to run it anywhere\n')
            return 1
        try:
            name = gamedir / "game-downloader"
            copy("main.py", name)
        except FileExistsError:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: The script is already installed.\n")
        except PermissionError:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: The script cannot be installed in {gamedir} due to permissions.\n")
        except OSError:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: The script cannot be installed in {loc} due to an OS error, maybe you have no free inodes?\n")
        except KeyboardInterrupt:
            stderr.write(f"{Fore.RED}Error{Fore.RESET}: Script installation cancelled.\nCopy the main.py script in your desired location to be able to run it. Exiting . . .\n")
        else:
            print(f">>>> Script {Fore.LIGHTGREEN_EX}succesfully{Fore.RESET} installed in {Fore.LIGHTBLUE_EX}{gamedir}{Fore.RESET} as {Fore.LIGHTGREEN_EX}{name}{Fore.RESET}.\nTry it typing {Fore.LIGHTMAGENTA_EX}`game-downloader --help`{Fore.RESET} from your command-line")
            return 0
        return 1

if __name__ == '__main__':
    exit(main())
