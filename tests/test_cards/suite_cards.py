import unittest
from .test_card import TestCard
from .test_deck import TestDeck

def suite() -> unittest.TestSuite:
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTests(loader.loadTestsFromTestCase(TestCard))
    test_suite.addTests(loader.loadTestsFromTestCase(TestDeck))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
