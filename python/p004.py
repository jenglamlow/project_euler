#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def answer():
    palindrome_list = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if is_palindrome(product):
                palindrome_list.append(product)

    return max(palindrome_list)

print(answer())

# Solution by answer
# P=100000x10000y1000z100z10yx
# P=100001x10010y1100z
# P=11(9091x910y 100z
# at least a or b must be factor of 11


def solution():
    a = 999
    largestPalindrome = 0
    while a >= 100:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990
            db = 11

        while (b >= a):
            if a * b <= largestPalindrome:
                break

            if is_palindrome(a*b):
                largestPalindrome = a * b

            b = b - db
        a = a - 1

    return largestPalindrome

print(solution())

# HackerRank
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def solution(N):
    a = 999
    largestPalindrome = 0
    while a >= 100:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990
            db = 11

        while (b >= a):
            if a * b <= largestPalindrome:
                break

            if is_palindrome(a*b):
                if a * b < int(N):
                    largestPalindrome = a * b

            b = b - db
        a = a - 1

    return largestPalindrome

for _ in range(int(input())):
    print(int(solution(input())))
