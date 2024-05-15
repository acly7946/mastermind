from util import *

def game(args):
	pegs = args.pegs
	colors = args.colors
	guesses = args.guesses
	code = generateCode(pegs, colors)
	board = initBoard(pegs, guesses)
	hints = initHints(pegs, guesses)
	win = False

	for guessNum in range(guesses):
		guess = inputGuess(pegs, colors)
		board[guessNum] = guess
		hints[guessNum] = evaluateGuess(pegs, code, guess)
		printBoard(board, hints)
		if guess == code:
			win = True
			break

	if win:
		print("You win!")
	else:
		print(f"You lose. The code was: {str(code).strip('[]').replace(' ', '')}")