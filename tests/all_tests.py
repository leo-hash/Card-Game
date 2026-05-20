import unittest
from tests.test_cards.suite_cards import suite as test_cards_suite
from tests.test_maumau.suite_maumau import suite as test_mauma_suite
from tests.test_universal_game.suite_universal import suite as test_universal_suite

def suite():
    main_suite = unittest.TestSuite()

    main_suite.addTest(test_cards_suite())
    main_suite.addTest(test_mauma_suite())
    main_suite.addTest(test_universal_suite())

    return main_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())