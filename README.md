# GAMES - game console database and download tool

## Introduction

__Games python library__. It contains a database to download a varierty of _PAL_ (EUR)
and _NTSC-U_ (USA) games for almost every game platform existing in the moment.
PS4, switch and xbox family games will be added in the future, _NTSC-J_ (japan
and korea) games have been deleted for storage, but will be recovered in the
future if requested.
You can __import__ the library to create you own scripts or use the `game-downloader`
script to automate the process. The library only depends on colorama.
The package is not yet available to MacOS because i don't know how to automate the
installation, but you can install it manually in you desired location.

## Python dependencies
1. colorama

## Operating System dependencies
1. __Python >= 3.10__ (tested with python 3.10, typing annotations not supported in 3.8)
2. git (optional)
3. unzip (optional, or other uncompressing software)

## How to install

Installation will be performed user-only if the program don't get privileges
Else, the program will be installed for all users in the machine

### How to install - Windows with source code and clicking
1. __Download__ the source code
2. __Unzip__ the full folder
3. __Enter__ the new folder created
4. __Double click__ on `install.py`
5. If the last step don't work, then
	1. __Rigth click__ on `install.py`
	2. Click __Open as__
	3. __Search__ python executable and open it

### How to install - Windows with git
```cmd
git clone https://github.com/Muuur/game-downloader
python install.py
```

### How to install - Linux
```bash
git clone https://github.com/Muuur/game-downloader
python3 install.py
```

### MacOS instalation
MacOS install is not yet ready for use, so be patient until the install function is
ready. You can do for now is a manual install, copying the _games_ folder somewhere
in python path, copying _dist-info_ in the same directory as _games.1.0.0-dist-info_
with _LICENSE_ and _README.md_ file in it. Then finally copy the main.py script
somewhere in your path as _game-downloader_ to use it anywhere.

## Package info

### Library folder structure - Modules avail
```md
games
├── __init__.py
├── all
│	├── baseurl.py
│	├── titles.py
│	└── version.py
└── roms
    ├── gb.py	(GameBoy)
    ├── gbc.py	(GameBoy Color)
    ├── gba.py	(GameBoy Advance)
    ├── gcn.py	(Game Cube)
    ├── n3ds.py	(Nintendo 3DS)
    ├── nds.py	(Nintendo DS)
    ├── n64.py	(Nintendo 64)
    ├── nes.py	(Nintendo Entertainment System)
    ├── ps2.py	(Play Station 2)
    ├── ps3.py	(Play Station 3)
    ├── psx.py	(Play Station)
    ├── psp.py	(Play Station Portable)
    ├── sms.py	(Sega Master System)
    ├── smd.py	(Sega Mega Drive)
    ├── gen.py	(Sega Genesis, symlink to smd.py)
    ├── snes.py	(Super Nintendo Entertainment System)
    ├── wii.py	(Nintendo wii)
    └── wiiu.py	(Nintendo Wii U)
```

### Classes and functions structure
1. games (\_\_init\_\_.py)
	1. class __Game__
		1. \_\_init\_\_(name: str, baseurl: str | Link, sha: Optional[str]=None)
		2. @classethod fromsha(cls, url: str, sha: str)
		3. download(self, verbose: bool=False, error: bool=True, filename: Optional[str]=None) -> bool
		4. get_url(self) -> Link
		5. get_name(self) -> str
		6. get_title(self) -> str
		7. open(self) -> self
		8. verify(self, file: str) -> bool
	2. class __GameCollection__
		1. \_\_init\_\_(self, baseurl: str | Link, games: dict[str, dict[str, str]]) -> None
		2. \_\_getitem\_\_(self, key: str) -> tuple[str, Optional[dict[str, str]]]
		3. \_\_iter\_\_() -> Generator[Game, None, None]
		4. \_\_len\_\_() -> int
		5. filter(self, query: str, error: bool=False)
		6. get_baseurl(self) -> Link
		7. get_urls(self) -> list[str]
	3. class __Link__(str)
		1. \_\_truediv\_\_(self, other: str | Link)
		2. \_\_add\_\_(self, other: str | Link)
		3. open() -> self
	4. class __Version__
		1. \_\_init\_\_(major: int, minor: int=0, revision: int=0)
		2. \_\_eq\_\_(self, other: Version) -> bool
		3. \_\_lt\_\_(self, other: Version) -> bool
		4. \_\_le\_\_(self, other: Version) -> bool
		5. get_number(self) -> str
	5. def check_updates() -> bool
	6. def fmtbytes(byte: str | int) -> int
2. __all.baseurl__, __all.titles__, __all.version__
	1. module .baseurl: _Link_
	2. module .titles:  _GameCollection_
	3. module .version: _Version_
	4. Constants for each submodule: GB, GBA, GBC, GCN, GEN, GG, N3DS, N64, NDS, NES, SMD, SMS, PS2, PS3, PSX, PSP, SNES, WII, WIIU
3. __roms.platform__ (each platform is the console)
	1. variable .baseurl: _Link_
	2. variable .games:   _GameCollection_
	3. variable.version: _Version_

## Version history

- 0.1   Bugs fix and better names visibility
- 0.2   Added cURL verification
- 0.3   Stop and resume option
- 0.3.1 '\n' when stdout is not a tty (pipes)
- 0.4   Added PSX games
- 1.0   Added sha, changed cURL to python-urllib, removed stop-resume option, added update option
- 1.1   Added --update cli option, changed N3DS and PSX databases, added SMS, SMD, GEN and GG databases and fixed WII database with part 2 and 3

## How to use

### How to use the script - All platforms
```bash
# Get help
game-downloader --help

# Get a Play Station 2 game interactively
game-downloader --ps2

# Get final fantasy's Nintendo Entertainment System games using argv query string (quotes not needed)
game-downloader --nes final fantasy
```

### How to use the package - Example in python
```python
>>> from games.roms import nds

>>> print(f"The nds games version is {nds.version}")

>>> for n, game in enumerate(nds.games.filter("pokemon")):
... 	title = game.get_title()
... 	print(f"The {n}th pokemon game in database is {title}")
... 	if "Pearl" in title and '(Europe)' in title:
... 		game.download(verbose=True, error=True)
...
```
