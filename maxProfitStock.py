stockArray = [100, 180, 1000, 100, 200, 310, 40, 535, 695, 10]


def maxProfitAaja(stockList):

    start = 0
    stockProfitList = {}

    tempStockDiff = 0

    while(start < len(stockList)): # first time entry for array
        k = start+1
        while(k < len(stockList)-1): # will check all posiblity to purchase with update max diff
            if stockList[k] - stockList[start] > tempStockDiff:
                tempStockDiff = stockList[k] - stockList[start]
                stockProfitList[stockList[start]] = stockList[k] - stockList[start]
                
            k += 1
        
        # checking last max. score if any then updating it 
        for temp in range(len(stockList)):
            if stockList[temp] in stockProfitList:
                if stockProfitList[stockList[temp]] < tempStockDiff:
                    del stockProfitList[stockList[temp]]
                    stockProfitList[stockList[start]] = tempStockDiff

        start += 1

     
    stockProfitList[stockProfitList.keys()[0]] = stockProfitList.keys()[0] + stockProfitList[stockProfitList.keys()[0]]

    return stockProfitList

profitList = maxProfitAaja(stockArray)
print(profitList)
