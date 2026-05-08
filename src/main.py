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

    game_round = 1
    while True:
        print(f"Round {game_round}")
        game_engine.play_turn()
        game_round += 1

        if game_round >= 25:
            break