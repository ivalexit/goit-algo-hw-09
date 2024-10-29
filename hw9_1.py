import time

def find_coins_greedy(amount, values):
    coin_count = {}
    values.sort(reverse=True)

    for coin in values:
        count = amount // coin
        if count > 0:
            coin_count[coin] = count
            amount -= count * coin

    return coin_count


def find_min_coins(amount, values):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in values:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return {} 

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Касир може ввести суму
try:
    amount = int(input("Enter the amount to provide change for: "))
    values = [50, 25, 10, 5, 2, 1]  # Наявні номінали монет



