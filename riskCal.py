import sys, argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('ticker')
parser.add_argument('-s', '--start', default='2010-01-01')
parser.add_argument('-rf', '--riskfree', default=0.015)
args = parser.parse_args()

df = pd.read_csv(f'{args.ticker}.csv', parse_dates=True, index_col=0)
cl = df.loc[args.start:,'Adj Close'].dropna()
chgs = np.log(cl).diff()
muA, sdA = chgs.mean()*250, chgs.std()*np.sqrt(250)
sharpe = (muA-args.riskfree)/sdA

print(f'Statistics for {args.ticker} using data since {args.start}')
print((f'Expected Return: {muA:.2%}\n'
        f'Standard Deviation: {sdA:.2%}\n'
        f'Sharpe Ratio: {sharpe:.2%}'))