from util import *

def game(args):
	pegs = args.pegs
	colors = args.colors
	guesses = args.guesses
	code = generateCode(pegs, colors)
	board = generateBoard(pegs, guesses)
	hints = generateHints(pegs, guesses)

	for guessNum in range(guesses):
		guess = inputGuess(pegs, colors)
		board[guessNum] = guess
		hints[guessNum] = evaluateGuess(pegs, code, guess)
		printBoard(board, hints)
		if guess == code:
			print("You win!")
			quit()

	print(f"You lose. The code was: {str(code).strip('[]').replace(' ', '')}")