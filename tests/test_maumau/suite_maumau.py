import unittest
from .test_gameboard import TestGameboard
from .test_player_maumau import TestPlayerMauMau
from .test_agent_ki_random import TestAgentKiRandom
from .test_game_engine_maumau import TestGameEngine

def suite() -> unittest.TestSuite:
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTests(loader.loadTestsFromTestCase(TestGameboard))
    test_suite.addTests(loader.loadTestsFromTestCase(TestPlayerMauMau))
    test_suite.addTests(loader.loadTestsFromTestCase(TestAgentKiRandom))
    test_suite.addTests(loader.loadTestsFromTestCase(TestGameEngine))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
