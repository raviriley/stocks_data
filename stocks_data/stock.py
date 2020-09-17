import os
from datetime import datetime
import dateparser
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web
import stocks_data.stocksetup as setup

#import quandl

class stock(): # time_period, data_source, ticker, data, percent_change, dates, values_open, values_close
    #ticker = ""
    def __init__(self, stock_ticker_symbol):
        self.ticker = stock_ticker_symbol.upper()
        self.start = setup.start_date
        self.end = setup.end_date
        self.data_source = setup.data_source
        self.api_key = setup.api_key
        
        if (self.data_source == "yahoo" or self.data_source == "yh"):
            self.data = web.DataReader(self.ticker, "yahoo", self.start, self.end)
            self.dates = self.data.index.strftime("%m/%d/%Y").tolist() #List of dates in time_period
            """
            ipo_data = web.DataReader((self.ticker+".us"), 'stooq', retry_count=5, pause=2.0,)
            self.ipo_date = ipo_data.index[-1]
            if (dateparser.parse(self.start) < self.ipo_date):
                raise ValueError(self.ticker+" IPO'd after specified start date")
            """
            self.values_high = self.data['High'].tolist()
            self.values_low = self.data['Low'].tolist()
            self.values_open = self.data['Open'].tolist()
            self.values_close = self.data['Adj Close'].tolist()

            self.years = self.data.index.strftime("%Y").tolist()
        
        elif (self.data_source == "stooq"):
            self.start = dateparser.parse(self.start).strftime("%Y-%m-%d")
            self.end = dateparser.parse(self.end).strftime("%Y-%m-%d")
            self.data = pd.read_csv("https://stooq.com/q/d/l/?s="+self.ticker.lower()+".us&i=d").set_index('Date').loc[self.start:self.end]
            #self.start = dateparser.parse(setup.start_date)
            #elf.end = dateparser.parse(setup.end_date)
            #self.data = web.DataReader((self.ticker+".us"), 'stooq')

            self.dates = self.data.index.values.tolist() #List of dates in time_period
            # format dates:
            self.years = []
            for i in range(len(self.dates)):
                d = dateparser.parse(self.dates[i])
                self.dates[i] = d.strftime("%m/%d/%Y")
                self.years.append(d.strftime("%Y"))
            
            # self.ipo_date = self.data.index[-1]
            # if (self.start < self.ipo_date):
            #     raise ValueError(self.ticker+" IPO'd after specified start date")
            
            self.values_open = self.data['Open'].tolist()
            self.values_high = self.data['High'].tolist()
            self.values_low = self.data['Low'].tolist()
            self.values_close = self.data['Close'].tolist()
            
        elif (self.data_source == "quandl" or self.data_source == "q"):
            import quandl
            quandl.ApiConfig.api_key = self.api_key

            self.start = dateparser.parse(setup.start_date).strftime("%Y-%m-%d")
            self.end = dateparser.parse(setup.end_date).strftime("%Y-%m-%d")

            self.data = quandl.get("WIKI/"+self.ticker, start_date=self.start, end_date=self.end)
            #os.environ["QUANDL_API_KEY"] = self.api_key
            #self.data = web.DataReader(("WIKI/"+self.ticker), "quandl", self.start, self.end)

            #self.values_open = self.data['Open'].tolist()
            #self.values_close = self.data['Close'].tolist()
            #self.values_high = self.data['High'].tolist()
            #self.values_low = self.data['Low'].tolist()

            self.years = self.data.index.strftime("%Y").tolist()

        elif (self.data_source == "alpha vantage" or self.data_source == "av"):
            os.environ["ALPHAVANTAGE_API_KEY"] = self.api_key

            self.data = web.DataReader(self.ticker, "av-daily", start=self.start, end=self.end, api_key=os.getenv('ALPHAVANTAGE_API_KEY'))
            self.values_open = self.data['open'].tolist()
            self.values_high = self.data['high'].tolist()
            self.values_low = self.data['low'].tolist()
            self.values_close = self.data['close'].tolist()

            #self.years = self.data.index.strftime("%Y").tolist()
            self.dates = self.data.index.values.tolist() #List of dates in time_period
            # format dates:
            self.years = []
            for i in range(len(self.dates)):
                d = dateparser.parse(self.dates[i])
                self.dates[i] = d.strftime("%m/%d/%Y")
                self.years.append(d.strftime("%Y"))

        elif (self.data_source == "iex"):
            os.environ["IEX_API_KEY"] = self.api_key
            self.data = web.DataReader(self.ticker, "iex", self.start, self.end)
            self.values_open = self.data['Open'].tolist()
            self.values_high = self.data['High'].tolist()
            self.values_low = self.data['Low'].tolist()
            self.values_close = self.data['Close'].tolist()

            self.years = self.data.index.strftime("%Y").tolist()

        # elif (data_source == "tiingo" or data_source == "rh"):
        #     os.environ["TIINGO_API_KEY"] = setup.api_key
        #     self.data = pdr.get_data_tiingo(self.ticker, api_key=os.getenv('TIINGO_API_KEY'))

        else:
            print("Invalid data source. Choices are yahoo/yh (default), quandl/q, iex, tiingo, or alpha vantage/av")
            raise ValueError("Invalid data source. Choices are yahoo/yh (default), quandl/q, iex, tiingo, or alpha vantage/av")

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
            
        
        self.years = list(dict.fromkeys(self.years))
    
    def __str__(self):
        return self.ticker

    # def __iter__(self):
    #     yield self.ticker
    #     yield self.data
    #     yield self.percent_change
    #     yield self.values_open
    #     yield self.values_high
    #     yield self.values_low
    #     yield self.values_close
    #     yield self.dates
    #     yield self.years
    
    # def price(ticker):
    #     quote=0
    # url=('https://finance.yahoo.com/quote/'+ticker)
    # response=requests.get(url)
    # soup=BeautifulSoup(response.text,'html.parser')
    # price=(soup.find_all('div',class_='D(ib) Mend(20px)'))
    # for container in price:
    #     quote=container.find('span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    # return quote

    """ Accessor methods """

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

