'''
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
'''

# Time complexity: O(n)
# Space complexity: O(1)
def buy_and_sell_stock(prices):
    min_price = float("inf")
    max_profit = 0
    
    for price in prices:
        # Update the minimum buy price so far
        if price < min_price:
            min_price = price
        # Calculate profit if sold today and update max_profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
        
    return max_profit

print(buy_and_sell_stock(prices=[7,1,5,3,6,4]))


# OR

'''
# Time complexity: O(n**2)
# Space complexity: O(1)
def buy_and_sell_stock(prices):
    max_profit = 0
    n = len(prices)
    for i in range(n-1):
        profit = 0
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            max_profit = max(profit, max_profit)
    return max_profit

print(buy_and_sell_stock(prices=[7,1,5,3,6,4]))
'''
