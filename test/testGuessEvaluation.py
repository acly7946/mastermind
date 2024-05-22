import unittest
from src.util import *

class TestGuessEvaluation(unittest.TestCase):
	def testGuessEvaluation(self):
		"""
		Test that the guess evaluation function returns the correct hints
		"""
		self.assertEqual(evaluateGuess(['1', '1', '1', '1'], ['1', '1', '1', '1'] ), ['X', 'X', 'X', 'X']) # all correct
		self.assertEqual(evaluateGuess(['1', '1', '1', '1'], ['2', '2', '2', '2'] ), ['-', '-', '-', '-']) # all incorrect
		self.assertEqual(evaluateGuess(['1', '1', '2', '2'], ['1', '1', '1', '2'] ), ['X', 'X', '-', 'X']) # duplicates


if __name__ == '__main__':
	unittest.main()
