import sys
# Understand the problem
# Recongize a pattern to the solution
# Categorized the input 
# Code the pattern into a function


# Strategy:
# Given A, B, get C from adding A + B
# Then for Xi in [0,9], and Xi to C , starting from 9 (that way the sum will always be as larage as possible)
# Stop as soon as we get a number that is divisble by 3
# Arrange A, B, and Xi to form the largest number

def biggest_three_digit_3(a,b):
  a = int(a)
  b = int(b)
  c = a + b
  for i in range(9, -1, -1):
    if (c + i) % 3 == 0:
      numList = [a, b, i]
      numList.sort(reverse=True)
      return f'{numList[0]}{numList[1]}{numList[2]}'
    else:
      continue

print(biggest_three_digit_3(sys.argv[1], sys.argv[2]))
