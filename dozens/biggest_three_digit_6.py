import sys
import itertools

# Suppose the solution is ABC, ABC needs to be even and A+B+C needs to be divisble by 3
# Given A and B
# for Xi in [0,9] (starting from 9), find a number where A + B + Xi is divisble by 3 and an arrangement of A, B, Xi is even.
# - Arrange A, B, Xi so that it is the biggest possible 3 digit number arrangemnet of the 3 numbers


def biggest_three_digit_6(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    for i in range(9, -1, -1):
        if (c + i) % 3 == 0:
            numList = [a, b, i]
            haveEven = any(n % 2 == 0 for n in numList)
            if haveEven:
              possible_solutions = list(itertools.permutations(numList, 3))
              possible_solutions.sort(reverse=True)
              sorted_number = []
              for n in possible_solutions:
                sorted_number.append(int(f'{n[0]}{n[1]}{n[2]}'))
              even_num = []
              for n in sorted_number:
                if n % 2 == 0:
                  even_num.append(n)
              return even_num[0]



print(biggest_three_digit_6(sys.argv[1], sys.argv[2]))
