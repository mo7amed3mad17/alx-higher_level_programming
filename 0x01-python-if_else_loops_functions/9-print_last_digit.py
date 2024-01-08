#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_d = number % 10
        print(l_d, end="")
        return l_d
    elif number < 0:
        l_d = number % -10
        print(-l_d, end="")
        return -l_d
