def dp(weights, prices, capacity, index, memo):
  if capacity<=0 or index>=len(weights):
    return 0
  if (capacity, index) in memo:
    return memo[(capacity, index)]
  
  if weights[index]>capacity:
    memo[(capacity, index)]= dp(weights, prices,capacity, index+1, memo)
    return memo[(capacity, index)]
  
  memo[(capacity, index)]= max(prices[index]+dp(weights, prices, capacity-weights[index], index+1, memo),
  dp(weights, prices, capacity, index+1, memo))
  return memo[(capacity, index)]


def knapsack(weights, prices, capacity):
  # your code goes here
  memo={}  
  return dp(weights, prices, capacity, 0,memo)