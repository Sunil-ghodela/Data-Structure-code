minVal = 0
maxVal = 10

stockArray = [100, 180, 260, 310, 40, 535, 695]

def maxProfitAaja(stockList):

  start = 0
  stockProfitList = []
  stockBuy = None

  while(start < len(stockList)):
    if stockBuy == None:
      if stockList[start] < stockList[start+1]:
        stockBuy = stockList[start] # // logic-1st
    else:
      if start+1 <= len(stockList): # // logic-2nd
        if stockList[start] > stockList[start-1]: # // logic-3nd
          if start == len(stockList)-1:# // logic-4rd
            stockProfitList.append({stockBuy: stockList[start]})
        else:
          stockProfitList.append({ stockBuy: stockList[start-1]})
          stockBuy = stockList[start] # // logic-5th
    start += 1
  return stockProfitList

profitList = maxProfitAaja(stockArray)
print(profitList)
