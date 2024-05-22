import unittest
from src.util import *

class TestInputValidation(unittest.TestCase):
	def testGuessValidation(self):
		"""
		Tests guess validation based on a game of
		4 pegs and 6 colors
		"""
		self.assertTrue(isValidGuess('1,2,3,4', 4, 6)) # valid
		self.assertFalse(isValidGuess('', 4, 6)) # empty
		self.assertFalse(isValidGuess(',,,', 4, 6)) # 4 empty pegs
		self.assertFalse(isValidGuess('0,0,0,0', 4, 6)) # zero pegs
		self.assertFalse(isValidGuess('1,2,3', 4, 6)) # too few pegs
		self.assertFalse(isValidGuess('1,2,3,4,5', 4, 6)) # too many pegs
		self.assertFalse(isValidGuess('1,2,3,7', 4, 6)) # out of color range
		self.assertFalse(isValidGuess('1,2,3,-1', 4, 6)) # invalid peg

	def testHintValidation(self):
		"""
		Tests hint validation based on a game of
		4 pegs
		"""
		self.assertTrue(isValidHint('X,X,X,X', 4)) # valid
		self.assertFalse(isValidHint('', 4)) # empty
		self.assertFalse(isValidHint(',,,', 4)) # 4 empty pegs
		self.assertFalse(isValidHint('X,X,X', 4)) # too few pegs
		self.assertFalse(isValidHint('X,X,X,X,X', 4)) # too many pegs
		self.assertFalse(isValidHint('X,X,X,?', 4)) # invalid peg

if __name__ == '__main__':
	unittest.main()
