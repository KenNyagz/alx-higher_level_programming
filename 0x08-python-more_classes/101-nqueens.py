#!/usr/bin/python3
"""Solving nqueens problem chess
   n being the number of queens as well as the
   no of cols and rows of chess board
"""


import sys

""" nqueens problem"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not isinstance(sys.argv[1], int):
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
