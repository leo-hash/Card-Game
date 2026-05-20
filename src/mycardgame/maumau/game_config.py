from mycardgame.maumau.agent import Agent

from dataclasses import dataclass
from typing import Optional

@dataclass
class PlayerConfig:
    name: str
    agent: Agent


@dataclass
class GameboardConfig:
    big_deck: bool
    double_deck: bool


@dataclass
class GameConfig:
    board: GameboardConfig
    players: list[PlayerConfig]
    # list index of start player
    start_player: Optional[int] = None