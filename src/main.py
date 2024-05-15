#! /usr/bin/env python3

import argparse
import computerGame

def main():
	parser = argparse.ArgumentParser(description="A command line mastermind game")
	gameModes = parser.add_mutually_exclusive_group()
	gameModes.add_argument("--computer", action="store_true",
						help="Play against the computer (default if no arguments passed)")
	gameModes.add_argument("--human", action="store_true",
						help="Play in 2 player mode")
	gameModes.add_argument("--campaign", action="store_true",
						help="Play in campaign mode")
	colors = parser.add_argument("-c", "--colors", type=int, default=6,
						help="The number of colors to use (default: 6)")
	pegs = parser.add_argument("-p", "--pegs", type=int, default=4,
						help="The number of pegs to use (default: 4)")
	guesses = parser.add_argument("-g", "--guesses", type=int, default=10,
						help="The number of guesses to allow (default: 10)")
	args = parser.parse_args()

	if args.human:
		humanGame.game(args)
	elif args.campaign:
		campaignGame.game(args)
	else:
		computerGame.game(args)

if __name__ == "__main__":
	main()