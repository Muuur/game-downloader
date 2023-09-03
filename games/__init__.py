#!/usr/bin/python3
"""
Module containing principal module classes like Version namedtuple or Game class
"""
from sys import stderr as _stderr, stdout as _stdout
from os import remove as _remove, devnull as _devnull
from re import search as _search, sub as _sub, I as _I
from functools import reduce as _reduce
from typing import Optional, Generator
from webbrowser import open as _openurl
from hashlib import sha1 as _sha1
from urllib.request import urlopen as _urlopen
from urllib.parse import unquote as _unquote
from urllib.error import URLError, HTTPError
from builtins import all as _all
from colorama import Fore as _Fore

class Version:
    """Namedtuple-like version handler"""
    def __init__(self, major: int, minor: int = 0, revision: int = 0):
        self.major = major
        self.minor = minor
        self.revision = revision

    def __repr__(self) -> str:
        return f"Version(major={self.major}, minor={self.minor}, revision={self.revision})"

    def __str__(self) -> str:
        return self.get_number()

    def get_number(self) -> str:
        """Prettier format for versions"""
        return f"{self.major}.{self.minor}.{self.revision}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Version):
            raise TypeError(f"Can only compare Versions, not {type(other).__name__}")
        return self.major == other.major and self.minor == other.minor and self.revision == other.revision

    def __lt__(self, other) -> bool:
        if not isinstance(other, Version):
            raise TypeError(f"Can only compare Versions, not {type(other).__name__}")
        if self.major < other.major:
            return True
        if self.minor < other.minor:
            return True
        if self.revision < other.revision:
            return True
        return False

    def __le__(self, other) -> bool:
        return self < other or self == other

class Link(str):
    """String capable of being opened by a browser"""
    def open(self):
        """Open the url in a web browser"""
        _openurl(self)
        return self

    def __truediv__(self, other: str):
        if not isinstance(other, (str, Link)):
            raise TypeError(f"divisor must be str or Link, not {type(other).__name__}")
        return Link(f"{self}/{other}")

    def __add__(self, other: str):
        if not isinstance(other, (str, Link)):
            raise TypeError(f"sumand must be str or Link, not {type(other).__name__}")
        return Link(f"{self}{other}")

class Game():
    def __init__(self, name: str, baseurl: str | Link, sha: Optional[str]=None) -> None:
        self._name = name
        self._baseurl = Link(baseurl)
        self._sha = sha

    @classmethod
    def fromsha(cls, url: str, sha: Optional[str]=None):
        """Create Game object using URL and sha1 sum"""
        baseurl, name = url.rsplit("/", 1)
        return Game(name, Link(baseurl), sha)

    def __repr__(self) -> str:
        return f'Game(name={self.get_title()}, baseurl={self._baseurl}, sha={self._sha})'

    def get_url(self) -> Link:
        """Complete URL getter"""
        return self._baseurl / self._name

    def open(self):
        """Open the game url in browser"""
        self.get_url().open()
        return self

    def verify(self, file: str) -> bool:
        """Check if the file sha1 sum is the same as the Game"""
        if self._sha is None:
            return True
        with open(file, 'rb') as infile:
            step = infile.read(1024)
            check = _sha1(step)
            while (step := infile.read(1024)):
                check.update(step)
        return self._sha == check.hexdigest()

    def get_title(self) -> str:
        """Game title getter in human-readable format"""
        res = _unquote(self._name)
        return res[:res.rfind('.')]

    def get_name(self) -> str:
        """Game title getter in URL format"""
        return self._name
    
    def get_sha(self) -> Optional[str]:
        """Get game sha1 sum"""
        return self._sha

    def download(self, verbose: bool=False, error: bool=True, filename: Optional[str]=None) -> bool:
        """Download the game from database into file and verify the checksum"""
        untit = _unquote(self._name)
        with open(_devnull, 'w') as nul:
            out = _stdout if verbose else nul
            err = _stderr if verbose else nul
            try:
                with _urlopen(self.get_url()) as stream, open(filename or untit, "wb") as gamefile:
                    data = b'INIT'
                    acc = 0
                    total = int(stream.headers['Content-length'])
                    while data:
                        data = stream.read(1024)
                        acc += 1024
                        gamefile.write(data)
                        print(f"Downloading {_Fore.LIGHTBLUE_EX}{untit}{_Fore.RESET}: {_Fore.LIGHTYELLOW_EX}{acc/total:.2%}{_Fore.RESET}", end="\r", file=out)
                print(f"Game {_Fore.LIGHTBLUE_EX}{untit}{_Fore.RESET} download {_Fore.LIGHTGREEN_EX}finished{_Fore.RESET}: {_Fore.LIGHTYELLOW_EX}100%{_Fore.RESET}", file=out)

            except KeyboardInterrupt as exc:
                print(f"\n{_Fore.RED}Stopped{_Fore.RESET}, removing {untit}", file=err)
                _remove(untit)
                if error:
                    raise exc
                return False
            except (URLError, HTTPError) as exc:
                if error:
                    raise exc
                else:
                    print(f"An internet {_Fore.RED}problem{_Fore.RESET} was found with url={_Fore.LIGHTBLUE_EX}{self.get_url()}{_Fore.RESET}", file=err)
                    return False

            print(f"Verifying {_Fore.LIGHTCYAN_EX}checksum{_Fore.RESET}. . .", file=out)
            if self._sha is None:
                return True
            elif self.verify(filename or untit):
                print(f"Checksum {_Fore.LIGHTGREEN_EX}correct{_Fore.RESET}, {_Fore.LIGHTMAGENTA_EX}exiting{_Fore.RESET}")
                return True

            if error:
                raise ValueError(f"\nChecksum is {_Fore.RED}incorrect{_Fore.RESET}, maybe the download {_Fore.LIGHTMAGENTA_EX}failed{_Fore.RESET} in any moment\n")
            else:
                print(f"\nChecksum is {_Fore.RED}incorrect{_Fore.RESET}, maybe the download {_Fore.LIGHTMAGENTA_EX}failed{_Fore.RESET} in any moment", file=err)
        return False

class GameCollection():
    def __init__(self, baseurl: str | Link, games: dict[str, dict[str, str]]) -> None:
        if not isinstance(games, dict) or not _all(isinstance(i, dict) for i in games.values()):
            raise ValueError("Expected dict[str, dict[str, str]]")
        self._games = games
        self._baseurl = Link(baseurl)

    def filter(self, query: str, error: bool=False) -> Generator[Game, None, None]:
        """Game generator filtered by human-readable name and using regex
        If error is set to True throws a StopIteration error if no game is found"""
        found = False
        for i in filter(lambda j: _search(query, j.get_name(), _I) is not None, self):
            found = True
            yield i

        if not found and error:
            raise StopIteration(f"No game was found with pattern: {query}\n")

    def __iter__(self) -> Generator[Game, None, None]:
        for url, gamelist in self._games.items():
            for game, sha in gamelist.items():
                yield Game(game, self._baseurl + url, sha)

    def get_baseurl(self) -> Link:
        """Baseurl getter from database"""
        return self._baseurl

    def __getitem__(self, key: str) -> tuple[str, Optional[dict[str, str]]]:
        return key, self._games.get(key, None)

    def __repr__(self) -> str:
        res = f'GameCollection(baseurl={self._baseurl}, '
        urls = self.get_urls()
        if urls[0] != '' or len(urls) > 1:
            for i, j in enumerate(urls, 1):
                res += f"url{i}={j}, "
        return res + f"game_number={len(self)})"

    def get_urls(self) -> list[str]:
        """Game urls getter"""
        return [*self._games.keys()]

    def __len__(self) -> int:
        return _reduce(lambda i, j: i + len(j), self._games.values(), 0)

def check_updates(verbose: bool=False) -> bool:
    """Function that check if updates are available in github"""
    from .all import version
    resp = _urlopen("https://raw.githubusercontent.com/Muuur/game-downloader/main/games/all/version.py")
    lines = map(bytes.decode, resp.readlines())
    gitver: dict[str, Version] = eval('{ "' + ', "'.join([i.replace(": Final[Version]", '"').replace("=", ":") for i in lines if '=' in i][:-1]) + '}')
    if verbose:
        anydat = False
        for i in ["WII", "N3DS", "PS2", "PSX", "GBA", "WIIU", "NES", "NDS", "SNES", "GBC", "GB", "N64", "GCN", "SMD", "SMC", "GG"]:
            if getattr(version, i) > gitver[i]:
                anydat = True
                print(f"Version of {i.lower().capitalize()} database is newer than local, download it from github")
        if gitver['SCRIPT'] > version.SCRIPT :
            if not anydat:
                print("All databases are in their last version")
            print("Script version is upgradable, download it from github")
        elif not anydat:
            print("The package and the script are in the last version")
    return gitver['SCRIPT'] > version.SCRIPT 

__all__ = ["Version", "Link", "Game", "GameCollection", "check_updates"]
