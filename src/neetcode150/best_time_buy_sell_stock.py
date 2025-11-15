# LeetCode 121 — Best Time to Buy and Sell Stock - LeetCode wording simplified

# You are given an array prices where:
# prices[i] = stock price on day i.

# You want to choose one day to buy and a later day to sell to get the maximum profit.

# Return the maximum profit you can achieve.
# If you cannot make any profit, return 0.

# def maxProfit(prices):
#     min_price = float('inf')   # Start with the highest number possible
#                                # This will be updated to the lowest price as we loop

#     max_profit = 0             # Track the best profit found so far

#     for day, price in enumerate(prices):
#         # If today's price is lower than any we've seen, update min_price
#         if price < min_price:
#             min_price = price

#         # Profit if we BUY at min_price and SELL today at price
#         profit = price - min_price

#         # If this profit is the best we've seen, update max_profit
#         if profit > max_profit:
#             max_profit = profit

#         # Print step-by-step analysis for learning
#         # print(f"{day:3} | {price:5} | {min_price:15} | {profit:20} | {max_profit}")

#     return max_profit


def maxProfit(prices):
    
    min_price = float('inf') 
    max_profit = 0           

    for day, price in enumerate(prices):
        
        if price < min_price:
            min_price = price
        
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

if __name__ == "__main__":
    print("Final Answer:", maxProfit([7, 1, 5, 3, 6, 4]))
