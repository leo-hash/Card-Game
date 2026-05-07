from src.maumau.agent_ki_random import AgentKiRandom
from src.maumau.game_config import GameConfig, GameboardConfig, PlayerConfig
from src.maumau.game_engine_maumau import GameEngine

if __name__ == '__main__':
    game_config = GameConfig(
        board=GameboardConfig(big_deck=False, double_deck=False),
        players=[
            PlayerConfig(name='KI_1', agent=AgentKiRandom()),
            PlayerConfig(name='KI_2', agent=AgentKiRandom()),
        ]
    )


    game_engine = GameEngine(game_config)