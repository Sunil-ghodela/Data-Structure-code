stockArray = [100, 180, 200, 310, 40, 535, 695, 200]

def maxProfitAaja(stockList):

  start = 0
  stockProfitList = []
  stockBuy = None

  while(start < len(stockList)):
    tempStockDiff = 0

    if stockBuy == None:
      if start+1 < len(stockList):
        if stockList[start] > stockList[start+1]:
          stockBuy = stockList[start+1]
    else:
      if start+1 <= len(stockList):
        if start+1 == len(stockList):
          stockProfitList.append({ 'stock buy'+ str(stockBuy): 'stock sell' + str(stockList[start])})
        else:
          if stockList[start] < stockList[start+1]:
            tempStockDiff = stockList[start] - stockList[start-1]
          else:
            stockProfitList.append({ 'stock buy'+ str(stockBuy): 'stock sell' + str(stockList[start])})
            break
    start += 1
  
  return stockProfitList

profitList = maxProfitAaja(stockArray)
print(profitList)
