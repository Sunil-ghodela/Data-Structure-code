minVal = 0
maxVal = 10

stockArray = [100, 180, 260, 310, 40, 535, 695]

def maxProfitAaja(stockList):

  start = 0
  stockProfitList = []
  stockBuy = None

  while(start < len(stockList)):
    tempStockDiff = 0

    if stockBuy == None:
      if stockList[start] < stockList[start+1]:
        stockBuy = stockList[start]
    else:
      if start+1 < len(stockList):
        if stockList[start] > stockList[start-1]:
          # print(start)
          # print(stockList[start])
          # print(stockList[start+1])
          # print(stockList[start] - stockList[start-1])
          tempStockDiff = stockList[start] - stockList[start-1]
        else:
          # print(start)
          # print(tempStockDiff)
          # print(stockBuy)
          stockProfitList.append({ 'stock buy'+ str(stockBuy): 'stock sell' + str(stockList[start-1])})
          stockBuy = None


          # if tempStockDiffPlusOne > tempStockDiff:
          #   tempStockDiff = tempStockDiffPlusOne
          # else:
          #   stockProfitList.append({stockBuy:stockList[start]})
    start += 1
  
  return stockProfitList

profitList = maxProfitAaja(stockArray)
print(profitList)
