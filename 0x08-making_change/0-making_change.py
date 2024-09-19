#!/usr/bin/python3
"""Module for Making Change."""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total.

    If total is 0 or less, returns 0. If total cannot be met by any number
    of coins, returns -1.
    Assumes that coins is a list of the values of the coins in your
    possession, the value of a coin is always an integer greater than 0,
    and you have an infinite number of each denomination of coin.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if coin > total:
            continue
        count = total // coin
        total -= count * coin
        coin_count += count
        if total == 0:
            break
    if total > 0:
        return -1
    return coin_count
