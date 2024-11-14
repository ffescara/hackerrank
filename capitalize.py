#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
  result = s.split(" ")
  return " ".join([result[i].capitalize() for i in range(len(result))])

if __name__ == '__main__':
  s = input()

  result = solve(s)
  print(result)