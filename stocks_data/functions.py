import pandas as pd
from stocks_data.stock import stock

def getCorrelatedPairsFromStocks(list_of_stocks, pearson_threshold):
    threshold = pearson_threshold
    dic_pearsons={}
    stocks_tickers = []
    for i in range(len(list_of_stocks)):
        stocks_tickers.append(list_of_stocks[i].ticker)
    for ticker in stocks_tickers:
        dic_pearsons[ticker]=stock(ticker).percent_change
    df=pd.DataFrame(dic_pearsons, columns = stocks_tickers)
    corrMatrix=df.corr()
    best_pairs = [] 
    for ticker in stocks_tickers:
        for i in range(len(stocks_tickers)):
            if (corrMatrix.iloc[i][ticker])>threshold and ticker!=stocks_tickers[i] and ([stocks_tickers[i],ticker] not in best_pairs):
                best_pairs.append([ticker, stocks_tickers[i]])
    return best_pairs

def getCorrelatedPairsFromTickers(stocks_tickers, pearson_threshold):
    threshold = pearson_threshold
    dic_pearsons={}
    for ticker in stocks_tickers:
        dic_pearsons[ticker]=stock(ticker).percent_change
    df=pd.DataFrame(dic_pearsons, columns = stocks_tickers)
    corrMatrix=df.corr()
    #sb.heatmap(corrMatrix, annot=True, cmap='RdBu_r')
    #plt.show()
    best_pairs = [] 
    for ticker in stocks_tickers:
        for i in range(len(stocks_tickers)):
            if (corrMatrix.iloc[i][ticker])>threshold and ticker!=stocks_tickers[i] and ([stocks_tickers[i],ticker] not in best_pairs ):
                best_pairs.append([ticker, stocks_tickers[i]])
    return best_pairs

def getCorrelatedPairsFromCSV(csv_file, pearson_threshold):
    stocks_tickers = pd.read_csv(csv_file, delimiter=",")
    
    threshold = pearson_threshold
    dic_pearsons={}
    for ticker in stocks_tickers:
        dic_pearsons[ticker]=stock(ticker).percent_change
    df=pd.DataFrame(dic_pearsons, columns = stocks_tickers)
    corrMatrix=df.corr()
    #sb.heatmap(corrMatrix, annot=True, cmap='RdBu_r')
    #plt.show()
    best_pairs = [] 
    for ticker in stocks_tickers:
        for i in range(len(stocks_tickers)):
            if (corrMatrix.iloc[i][ticker])>threshold and ticker!=stocks_tickers[i] and ([stocks_tickers[i],ticker] not in best_pairs ):
                best_pairs.append([ticker, stocks_tickers[i]])
    return best_pairs

# test speed of making my own pearson 