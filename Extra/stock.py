## 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    sell_price=0
    profits=[]
    for j in range(len(prices)):
        buying_price=prices[j]
        for i in range(j+1,len(prices)):
            sell_price=prices[i]
            if sell_price>buying_price: 
                profits.append(sell_price-buying_price)
            
    return max(profits) if len(profits)>0 else 0
    
print(maxProfit([34,6,5,4,3]))
print(maxProfit([1,6,5,4,34,3]))

def maxProfit_better(prices):
    buy=prices[0]
    profit=0
    for p in prices:
        if p>buy:
            profit=max(profit,p-buy) 
        if p<buy:
            buy=p
    return profit


print(maxProfit_better([34,6,5,4,3]))
print(maxProfit_better([1,6,5,4,34,3]))
print(maxProfit_better([180,200, 2,3,3,2,10,3,30,2,3,20])) #28
print(maxProfit_better([20,40, 2,3,3,2,10,3,30,2,3,20])) #28
