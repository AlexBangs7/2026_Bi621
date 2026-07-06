#!/usr/bin/env python

import argparse

def get_args():
	parser = argparse.ArgumentParser(description="A program to introduce yourself")
	parser.add_argument("-n", "--name", help="Your first name", required=True)
	parser.add_argument("-l", "--love", help="Something that you love", required=True)
	parser.add_argument("-k", "--kids", help="How many kids you have", type=int)
	return parser.parse_args()
	
args = get_args()
print(f"My name is {args.name} and I love {args.love}!")
if args.kids:
	print(f"I have {args.kids} kids")