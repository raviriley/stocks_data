import pandas as pd

#import urllib.request as urllib
import re
import requests

#import wget

nasdaq_url = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"
nyse_url = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
amex_url = "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download"
sec_url = "https://www.sec.gov/include/ticker.txt"

#print('Beginning file download with wget module')

#wget.download(amex_url, '/Users/raviriley/Downloads/test.csv')

c=pd.read_csv(nasdaq_url)
print(c)


def fetch_file(url):
    '''
    Gets and downloads files
    '''
    file_fetcher = urllib.build_opener()
    #file_fetcher.addheaders = [('User-agent', 'Mozilla/5.0')]
    print("1")
    file_data = file_fetcher.open(url).read()
    print("2")
    file_data = file_data.decode("utf-8")
    print("3")
    symbol_data = re.split("\r?\n", file_data)
    print(symbol_data)

#fetch_file(amex_url)


# url = sec_url
# print("1")
# r = requests.get(url, allow_redirects=True)
# print("2")
# open('_inputdata/sec.txt', 'wb').write(r.content)
# print("3")