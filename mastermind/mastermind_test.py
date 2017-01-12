
import unittest
from mastermind import Mastermind

class MastermindTest(unittest.TestCase):

    def test_play_isCorrect(self):
        m = Mastermind()
        res = m.play([3,7,6,5])
        self.assertEqual(res, True)

    def test_play(self):
        m = Mastermind()
        res = m.play([1,2,3,4])
        self.assertEqual(res, False)
    
    def test_exist(self):
        m = Mastermind()
        res = m.exist([3,7,6,5])
        self.assertEqual(res,4)

    def test_exact(self):
        m = Mastermind()
        res = m.exact([1,1,6,0])
        self.assertEqual(res,1) 




