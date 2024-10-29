import time

def find_coins_greedy(amount, value):
    coin_count = {}
    value.sort(reverse=True)

    for coin in value:
        count = amount // coin
        if count > 0:
            coin_count[coin] = count
            amount -= count * coin

    return coin_count

