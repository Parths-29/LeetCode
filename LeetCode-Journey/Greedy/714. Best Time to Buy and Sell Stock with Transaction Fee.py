def maxProfit(prices, fee):
    '''
    Approach:

    We maintain two states:
    hold → max profit when holding stock
    cash → max profit when not holding stock

    Transitions:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)

    Return cash at end.
    '''

    hold = -prices[0]
    cash = 0

    for price in prices[1:]:
        prev_hold = hold
        hold = max(hold, cash - price)
        cash = max(cash, prev_hold + price - fee)

    return cash


# ====== INPUT / OUTPUT ======
prices = list(map(int, input("Enter prices: ").split()))
fee = int(input("Enter transaction fee: "))
print("Maximum profit:", maxProfit(prices, fee))