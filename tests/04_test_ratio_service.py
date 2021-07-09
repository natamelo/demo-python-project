import unittest
from src.services.ratio_service import RatioService
from src.util.exceptions import NotFoundError


class TestCalculatorFormatter(unittest.TestCase):

    def test1_calculate_values_by_params_with_valid_params(self):
        model_id = '67352'
        year = '2010'
        result = RatioService.calculate_values_by_params(model_id, year)

        self.assertEqual(result.id, '67352')
        self.assertEqual(result.year, '2010')
        self.assertEqual(
            result.ratios, {'AuctionRatio': 135227.159496, 'MarketRatio': 247416.420108})

    def test2_calculate_values_by_params_with_invalid_params(self):
        model_id = '67352'
        year = '2099'

        result = RatioService.calculate_values_by_params(model_id, year)

        self.assertEqual(result.valid, False)

    def test3_calculate_values(self):
        inputs = [{'id': '67352', 'year': '2007'},
                  {'id': '87964', 'year': '2011'}]
        result = RatioService.calculate_values(inputs)

        self.assertEqual(result[0].id, '67352')
        self.assertEqual(result[0].year, '2007')
        self.assertEqual(result[0].valid, True)
        self.assertEqual(
            result[0].ratios, {'AuctionRatio': 126089.52642, 'MarketRatio': 216384.71025600002})

        self.assertEqual(result[1].id, '87964')
        self.assertEqual(result[1].year, '2011')
        self.assertEqual(result[1].valid, False)
        self.assertEqual(
            result[1].ratios, {})
