
def setup(startDate, endDate, dataSource="yahoo", apiKey=None):
    global start_date, end_date, data_source, api_key
    start_date = startDate
    end_date = endDate
    data_source = dataSource.lower()
    api_key = apiKey


