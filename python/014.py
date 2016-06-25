#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


collatz_dict = {}


def num_of_chain(n):
    chain_list = []
    while n != 1:
        if str(n) in collatz_dict:
            for i in chain_list:
                collatz_dict[str(i)] = len(chain_list[chain_list.index(i):]) + collatz_dict[str(n)]
            return collatz_dict[str(n)] + len(chain_list)

        chain_list.append(n)

        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    chain_list.append(n)
    for i in chain_list:
        collatz_dict[str(i)] = len(chain_list[chain_list.index(i):])
    return len(chain_list)


def answer(N):
    longest_chain = 0
    longest_term = 0

    for i in range(2, N):
        chain = num_of_chain(i)
        if chain > longest_chain:
            longest_chain = chain
            longest_term = i

    return longest_term

print(answer(1000000))