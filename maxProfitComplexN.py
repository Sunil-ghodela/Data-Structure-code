# stockArray = [100, 1, 1000, 100, 200, 310, 40, 535, 6, 10000]
# stockArray = [100, 6, 1000, 100, 200, 310, 40, 100, 535, 10, 10]
stockArray = [100, 1, 1000, 100, 200, 310, 40, 100, 535, 60, 10000]


def maxProfitAaja(stockList):

    start = 0
    stockProfitList = {}

    tempStockDiff = 0

    while(start < len(stockList)):  # first time entry for array
        if start+1 <= len(stockList)-1:
            if stockList[start+1] - stockList[start] > tempStockDiff:
                tempStockDiff = stockList[start+1] - stockList[start]
                if stockProfitList != {}:
                    for item in stockProfitList.keys():
                        if stockProfitList[item] < (stockList[start+1] - stockList[start]):
                            del stockProfitList[item]
                            stockProfitList[stockList[start]] = stockList[start+1]
                else:
                    stockProfitList[stockList[start]] = stockList[start+1]



        # # checking last max. score if any then updating it
        # for temp in range(len(stockList)):
        #     if stockList[temp] in stockProfitList:
        #         if stockProfitList[stockList[temp]] < tempStockDiff:
        #             del stockProfitList[stockList[temp]]
        #             stockProfitList[stockList[start]] = tempStockDiff

        start += 1

    # stockProfitList[stockProfitList.keys()[0]] = stockProfitList.keys()[
    #     0] + stockProfitList[stockProfitList.keys()[0]]

    return stockProfitList


profitList = maxProfitAaja(stockArray)
print(profitList)
