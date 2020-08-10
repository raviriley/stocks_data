import os

def setup(startDate, endDate, dataSource="yahoo", api_key=None):
    global data_source, start_date, end_date
    data_source = dataSource.lower()
    start_date = startDate
    end_date = endDate
    if (data_source.lower() == "iex"):
        os.environ["IEX_API_KEY"] = api_key

