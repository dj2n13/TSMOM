""" Get Yahoo data"""
import yfinance as yf
import pandas as pd

class Yahoo:

    def __init__(self, file):

        self.constituents = pd.read_csv('data/{}.csv'.format(file))


    def get_data(self):

        input = " ".join(list(self.constituents['Symbol']))

        self.data = yf.download(input, period="1y")['Adj Close']

        return self.data
