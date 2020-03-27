import sys
# Divisible By Two
# Given Two Numbers A and B,
# If A and B are even, but A > B, then return 9AB, else return 9BA
# if A and B are odd, but A > B, then return AB8, else return BA8
# If A is odd and B is even, return 9AB
# If A is even and B is odd, return 9BA
# If A is 0 and B is odd, return 9B0
# If A is 0 and B is even, return 9B0
# If B is 0 and A is odd
# If B is 0 and A is even


def biggest_three_digit_2(a, b):
    a = int(a)
    b = int(b)
    if a % 2 == 0 and b % 2 == 0:
        if a >= b:
            return f'9{a}{b}'
        else:
            return f'9{b}{a}'
    if a % 2 != 0 and b % 2 != 0:
        if a >= b:
            return f'{a}{b}8'
        else:
            return f'{b}{a}8'
    if a % 2 != 0 and b % 2 == 0:
        return f'9{a}{b}'
    if a % 2 == 0 and b % 2 != 0:
        return f'9{b}{a}'
    if a == 0:
        return f'9{b}{0}'
    if b == 0:
        return f'9{a}{0}'


print(biggest_three_digit_2(sys.argv[1], sys.argv[2]))
