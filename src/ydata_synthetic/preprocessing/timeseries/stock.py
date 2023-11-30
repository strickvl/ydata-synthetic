"""
    Get the stock data from Yahoo finance data
    Data from the period 01 January 2017 - 24 January 2021
"""
import pandas as pd

from ydata_synthetic.preprocessing.timeseries.utils import real_data_loading

def transformations(path, seq_len: int):
    stock_df = pd.read_csv(path)
    try:
        stock_df = stock_df.set_index('Date').sort_index()
    except:
        stock_df=stock_df
    return real_data_loading(stock_df.values, seq_len=seq_len)
