from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if len(prices) < 2:
        return 0.
    minsofar = prices[0]
    max_profit = 0
    for p in prices:
        max_profit = max(max_profit, p-minsofar)
        minsofar = min(p, minsofar)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
