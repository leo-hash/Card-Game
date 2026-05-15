import unittest


class MyTestCase(unittest.TestCase):
    def test_init(self):
        raise NotImplementedError

    def test_play_card(self):
        raise NotImplementedError

    def test_receive_card(self):
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
