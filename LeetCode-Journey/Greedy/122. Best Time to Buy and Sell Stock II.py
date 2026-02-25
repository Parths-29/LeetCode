def maxProfit(prices):
    '''
    Approach:

    1️⃣ Traverse array.
    2️⃣ Whenever price increases,
         add the difference to profit.
    3️⃣ Return total profit.
    '''

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


# ====== INPUT / OUTPUT ======
prices = list(map(int, input("Enter prices: ").split()))
print("Maximum profit:", maxProfit(prices))