import os, sys, argparse
import backtrader as bt
import pandas as pd
from GoldenCross import GoldenCross
from BuyHold import BuyHold

cerebro = bt.Cerebro()
cerebro.broker.setcash(100_000)

spy_prices = pd.read_csv('SPY.csv', index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GoldenCross)
cerebro.run()
cerebro.plot()