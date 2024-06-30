""" Time Series Momentum using SP500"""
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TSMOM:

    def __init__(self, data):

        self.data = data


    def _daily_to_monthly(self):

        self.data.index = pd.to_datetime(self.data.index)

        self.data = self.data.resample('1M').mean()

        return self.data


    def _get_cum_prod(self):

        monthly_return = self._daily_to_monthly().pct_change(1) + 1

        self.cum_prod = monthly_return.cumprod(skipna = True).reset_index(drop = True).reset_index()

        return self.cum_prod


    def _get_signal(self):

        self.signal = self._get_cum_prod().sort_values(by = 11, ascending = False, axis = 1)

        self.signal = self.signal.drop(['index'], axis =1)

        return self.signal


    def top20(self):

        selection = list(self._get_signal().iloc[:,1:21].columns)

        self._plot_performance(selection)


    def top10(self):

        selection = list(self._get_signal().iloc[:,1:11].columns)

        self._plot_performance(selection)


    def top5(self):

        selection = list(self._get_signal().iloc[:,1:6].columns)

        self._plot_performance(selection)


    def _plot_performance(self, selection):

        with plt.style.context("seaborn-darkgrid", after_reset=True):

            self.data = self.data.fillna(1)

            sns.set_style("ticks")

            plt.style.use("dark_background")

            fig = sns.lineplot(data=self.cum_prod[selection], dashes = False)

            fig.set(xticks=[i for i in range(12)])

            fig.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)






