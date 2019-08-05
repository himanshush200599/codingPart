# Time and space O(NK)
def maxProfitWithKTransactions(prices,k):
	if not len(prices):
		return 0
	profits = [[0 for d in prices] for i in range(k+1)]
	for t in range(1,k+1):
		maxSoFar = float("-inf")
		for d in range(1,len(prices)):
			maxSoFar = max(maxSoFar,profits[t-1][d-1]-prices[d-1])
			profits[t][d] = max(profits[t][d-1],maxSoFar+prices[d])
	return profits[-1][-1]
