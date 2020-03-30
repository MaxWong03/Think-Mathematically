import sys
# Understand the problem
# Recongize a pattern to the solution
# Categorized the input
# Code the pattern into a function

# Strategy:
# Given A and B
# 1) if AB is divisible by 4, then return 9AB
# 2) if BA is divisible by 4, then return 9BA
# 3) if AB / BA is not divisible by 4
# 3a) if A > B, and B is even, then for Xi in [0,9] starting from 9 return AXiB, with XiB being the largest multiple of 4 possible from XiB
#     if A > B, and B is odd, then for Xi in [0,9] starting from 9 return ABXi, with BXi being the largest multiple of 4 possible from XiB
# 3b) if B > A, then for Xi in [0,9] starting from 9 return BAXi, with AXi being the largest multiple of 4 possible from AXi


def biggest_three_digit_4(a, b):
    if int(a+b) % 4 == 0:
        return f'9{a}{b}'
    elif int(b+a) % 4 == 0:
        return f'9{b}{a}'
    else:
        a = int(a)
        b = int(b)
        if a > b:
            for i in range(9, -1, -1):
                if b % 2 != 0:
                    if int(f'{b}{i}') % 4 == 0:
                        return f'{a}{b}{i}'
                    else:
                        continue
                else:
                    if int(f'{i}{b}') % 4 == 0:
                        return f'{a}{i}{b}'
                    else:
                        continue
        else:
            for i in range(9, -1, -1):
                if a % 2 != 0:
                    if int(f'{a}{i}') % 4 == 0:
                        return f'{b}{a}{i}'
                else:
                    if int(f'{i}{a}') % 4 == 0:
                        return f'{a}{i}{a}'
                    else:
                        continue


print(biggest_three_digit_4(sys.argv[1], sys.argv[2]))
