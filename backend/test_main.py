import unittest
import main

class Testing(unittest.TestCase):
    def test_collect_pokemon(self):
        self.assertIsNotNone(main.collect_pokemon())

if __name__ == '__main__':
    unittest.main()