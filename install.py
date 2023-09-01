#!/usr/bin/python3
"""This python script install the games module and the game-downloader script"""
from sys import stderr, version_info, path, argv
from os import getenv, system, name as osname
from pathlib import Path
from shutil import copy, copytree
from games.all.version import SCRIPT

def main() -> int:
    """Main function
    Linux and Windows installer"""
    user = getenv("USER")
    ospath = getenv("PATH")

    vernum = f'python{version_info.major}.{version_info.minor}'
    if osname == 'nt':
        from winreg import HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, OpenKey, KEY_READ, KEY_WRITE, QueryValueEx, REG_SZ, SetValueEx
        admin = system("net session > NUL 2> NUL") == 0

        loc = Path(fr'{getenv("systemdrive")}\Program files\game-downloader' if admin else fr'{getenv("userprofile")}/AppData/local/game-downloader')
        if not loc.exists():
            print("Creating game directory in", loc)
            loc.mkdir()
        try:
            print("Copying necessary files")
            copytree("games", loc / "games")
            copytree("dist-info", loc / f'games-{SCRIPT}.dist-info')
            copy("LICENSE", loc / f'games-{SCRIPT}.dist-info' / 'LICENSE')
            copy("README.md", loc / f'games-{SCRIPT}.dist-info' / 'README.md')
            copy("main.py", loc / "main.py")
        except FileExistsError:
            stderr.write(f"The package is already installed\n")
            return 1
        except KeyboardInterrupt:
            stderr.write("Package installation cancelled\nExiting . . .\n")
            return 1

        print("Creating bat launcher")
        with open(loc / "game-downloader.bat", 'w') as batfile, open(loc / f'games-{SCRIPT}.dist-info' / 'INSTALLER', 'w') as installer:
            batfile.write("@echo off\nset PYTHONPATH=%~dp0\npython -h > NUL 2> NUL || goto :nopy\npython main.py %*\nexit /b\n\n:nopy\necho Python is not installed or in path\ngoto :eof\n")
            installer.write('install.py')

        print("Adding game-downloader to path")
        if admin:
            key = OpenKey(HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment", access=KEY_READ | KEY_WRITE)
        else:
            key = OpenKey(HKEY_CURRENT_USER, "Environment", access=KEY_READ | KEY_WRITE)

        try:
            result = QueryValueEx(key, "PATH")
            value = result[0]
            value += f";{loc}"
        except FileNotFoundError:
            value = str(loc)

        try:
            SetValueEx(key, "PATH", 0, REG_SZ, value)
        except PermissionError:
            stderr.write("Adding to path failed, add it manually using system variables application\n")
            return 1
        print("The package is succesfully installed, try it typing `game-downloader --help`")
        return 0
    else:
        from os import getuid
        sudo = getuid() == 0
        if sudo:
            loc = Path(f'/usr/local/lib/{vernum}/dist-packages' if sudo else f'/home/{user}/.local/lib/{vernum}/site-packages')
        if not loc.is_dir() or loc not in path:
            if sudo:
                loc = Path(f'/usr/lib/python{version_info.major}/dist-packages')
            else:
                stderr.write(f"Could not install the package in {loc} because the requested directory don't exists or is not in python path\n")
                return 1

        print("Installing package in", loc)
        try:
            copytree("games", loc / "games")
            copytree("dist-info", loc / f'games-{SCRIPT}.dist-info')
            copy("LICENSE", loc / f'games-{SCRIPT}.dist-info' / 'LICENSE')
            copy("README.md", loc / f'games-{SCRIPT}.dist-info' / 'README.md')
            with open(loc / f'games-{SCRIPT}.dist-info' / 'INSTALLER', 'w') as installer:
                installer.write('install.py')
            print(f"Package installed in {loc}")
        except FileExistsError:
            stderr.write(f"The package is already installed\n")
        except PermissionError:
            stderr.write(f"The package cannot be installed in {gamedir} due to permissions\n")
            return 1
        except OSError:
            stderr.write(f"The package cannot be installed in {loc} due to an OS error, maybe you have no free inodes?\n")
            return 1
        except KeyboardInterrupt:
            stderr.write("Package installation cancelled\nExiting . . .\n")
            return 1

        gamedir = Path("/usr/games" if sudo else f'/home/{user}/.local/bin')
        print("installing script in", gamedir)
        if gamedir.as_posix() not in ospath.split(":"):
            stderr.write(f'Script installation failed\nThe directory "{gamedir}" is not in path, copy the main.py script as game-downloader in your desired destination to be able to run it anywhere\n')
            return 1
        try:
            name = gamedir / "game-downloader"
            copy("main.py", name)
        except FileExistsError:
            stderr.write("The script is already installed\n")
        except PermissionError:
            stderr.write(f"The script cannot be installed in {gamedir} due to permissions\n")
        except OSError:
            stderr.write(f"The script cannot be installed in {loc} due to an OS error, maybe you have no free inodes?\n")
        except KeyboardInterrupt:
            stderr.write("Script installation cancelled, copy the main.py script in your desired location to be able to run it\nExiting . . .\n")
        else:
            print(f"Script succesfully installed in {gamedir} as {name}, try it typing `game-downloader --help`")
            return 0
        return 1

if __name__ == '__main__':
    exit(main())
