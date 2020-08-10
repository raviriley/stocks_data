from datetime import datetime
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web
import stocks_data.stocksetup as setup

#import quandl

class stock(): # time_period, data_source, ticker, data, percent_change, dates, values_open, values_close
    #ticker = ""
    def __init__(self, stock_ticker_symbol):
        self.ticker = stock_ticker_symbol
        self.start = setup.start_date
        self.end = setup.end_date
        self.data_source = setup.data_source
        
        if (self.data_source == "yahoo" or self.data_source == "yh"):
            self.data = web.DataReader(self.ticker, "yahoo", self.start, self.end)
            self.dates = self.data.index.strftime("%m/%d/%Y").tolist() #List of dates in time_period
            
            self.values_open = self.data['Open'].tolist() # Open, Close, or High
            self.values_close = self.data['Adj Close'].tolist()
            self.values_high = self.data['High'].tolist()
            self.values_low = self.data['Low'].tolist()
            
            self.all_values = []
            for i in range(len(self.data)):
                self.all_values.append(self.values_open[i])
                self.all_values.append(self.values_high[i])
                self.all_values.append(self.values_close[i])
            
            self.highest_value = max(self.all_values)

            self.percent_change = []
            for i in range(len(self.data)):
                percent_change_calc = ( ( (self.values_close[i]-self.values_close[0]) / self.values_close[0] ) * 100 ) # ((new-old)/old)*100
                self.percent_change.append(percent_change_calc)
            
            self.years = self.data.index.strftime("%Y").tolist()
            self.years = list(dict.fromkeys(self.years))

        # elif (data_source == "quandl" or data_source == "q"):
        #     quandl.ApiConfig.api_key = setup.api_key
        #     os.environ["QUANDL_API_KEY"] = setup.api_key
        #     self.data = web.DataReader(("WIKI/"+self.ticker), "quandl", self.start, self.end)

        # elif (data_source == "alpha vantage" or data_source == "av"):
        #     os.environ["ALPHAVANTAGE_API_KEY"] = setup.api_key
        #     self.data = web.DataReader(self.ticker, "av-daily", start=self.start, end=self.end, api_key=os.getenv('ALPHAVANTAGE_API_KEY'))

        # elif (data_source == "iex"):
        #     os.environ["IEX_API_KEY"] = setup.api_key
        #     self.data = web.DataReader(self.ticker, "iex", self.start, self.end)

        # elif (data_source == "tiingo" or data_source == "rh"):
        #     os.environ["TIINGO_API_KEY"] = setup.api_key
        #     self.data = pdr.get_data_tiingo(self.ticker, api_key=os.getenv('TIINGO_API_KEY'))

        else:
            print("Invalid data source. Choices are yahoo/yh (default), quandl/q, iex, tiingo, or alpha vantage/av")
            raise ValueError("Invalid data source. Choices are yahoo/yh (default), quandl/q, iex, tiingo, or alpha vantage/av")
    
    def __str__(self):
        return self.ticker

    

"""
    def getHighestValue(self):
        return self.highest_value
    
    def getPercentChange(self):
        return self.percent_change

    def getDataSource(self):
        return self.data_source
    def getDates(self):
        return self.dates
    def getYears(self):
        return self.years
    def getData(self):
        return self.data
    def getAllValues(self):
        return self.all_values
    def getValuesOpen(self):
        return self.values_open
    def getValuesClose(self):
        return self.values_close
    def getValuesHigh(self):
        return self.values_high
    def getValuesLow(self):
        return self.values_low
"""