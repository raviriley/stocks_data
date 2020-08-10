import stocks_data as sd

start = "7/29/2019" # can be a datetime() or anything date parser takes in
end = "today"
#end = datetime(2020, 6, 30)
#data_source = "yahoo" 
#api_key = "example"

sd.setup(start, end)

stock1 = sd.stock("FB")
print(stock1.ticker)
fatmang = ["FB", "AAPL", "TSLA", "MSFT", "AMZN", "NFLX", "GOOG", "GOOGL"]

print(sd.getCorrelatedPairsFromTickers(fatmang, 0.95))