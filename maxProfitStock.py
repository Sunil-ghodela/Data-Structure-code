stockArray = [100, 180, 1000, 20000, 310, 40, 5350, 695, 200]

def maxProfitAaja(stockList):

  start = 0
  stockProfitList = []
  stockBuy = None

  tempStockDiff = 0

  while(start < len(stockList)):

    if stockBuy == None:
      if start+1 < len(stockList):
        if stockList[start] > stockList[start+1]:
          stockBuy = stockList[start+1]
    else:
        if start+1 < len(stockList):
            if stockList[start] < stockList[start+1]:
                if tempStockDiff < stockList[start+1] - stockList[start]:
                    tempStockDiff = stockList[start+1] - stockList[start]
                    stockProfitList = {stockBuy: stockList[start+1]}
        else:
            # tempStockDiff = stockList[start+1] - stockList[start]


            if stockList[start-1] < stockList[start]:
                if tempStockDiff < stockList[start] - stockList[start-1]:
                    stockProfitList = {stockBuy: stockList[start]}
                else:
                    stockProfitList = {stockBuy: tempStockDiff+stockBuy}

    start += 1
  
  return stockProfitList

profitList = maxProfitAaja(stockArray)
print(profitList)
