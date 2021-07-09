import unittest
from src.util.calculator import Calculator


class TestCalculatorFormatter(unittest.TestCase):

    def test1_calculate(self):
        result = Calculator.calculate(0.613292, 48929)
        self.assertEqual(result, 30007.764268)

    def test2_calculate_values(self):
        ratios = {'marketRatio': 0.613292, 'auctionRatio': 0.417468}
        result = Calculator.calculate_values(10, **ratios)
        self.assertEqual(
            result, {'AuctionRatio': 4.17468, 'MarketRatio': 6.1329199999999995})
