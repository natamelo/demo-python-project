import unittest
from src.util.filters import DataFilter
from src.services.mocked_external_service import MockedAPI
from src.util.exceptions import NotFoundError


class TestCalculatorFormatter(unittest.TestCase):

    @classmethod
    def setUp(self):
        data = MockedAPI.get_mocked_service()
        self.data_filters = DataFilter(data)

    def test1_get_model_by_id_with_valid_id(self):
        model_id = '67352'
        result = self.data_filters.get_model_by_id(model_id)
        self.assertIsNotNone(result)

    def test2_get_model_by_id_with_invalid_id(self):
        model_id = 'X'

        with self.assertRaises(NotFoundError) as context:
            self.data_filters.get_model_by_id(model_id)

        self.assertEqual(str(context.exception),
                         "model not found for args: {'model_id': 'X'}")

    def test3_get_ratios_by_params_with_valid_id(self):
        model_id = '67352'
        year_id = '2006'
        result = self.data_filters.get_ratios_by_params(model_id, year_id)
        self.assertEqual(
            result, {"marketRatio": 0.311276, "auctionRatio": 0.181383})

    def test4_get_model_by_id_with_valid_id(self):
        model_id = '67352'
        year_id = 'X'

        with self.assertRaises(NotFoundError) as context:
            self.data_filters.get_ratios_by_params(model_id, year_id)

        self.assertEqual(str(context.exception),
                         "ratios not found for args: {'model_id': '67352', 'year': 'X'}")

    def test5_get_cost_by_model_id_with_valid_id(self):
        model_id = '67352'
        result = self.data_filters.get_cost_by_model_id(model_id)
        self.assertEqual(result, 681252)

    def test6_get_cost_by_model_id_with_invalid_id(self):
        model_id = 'X'

        with self.assertRaises(NotFoundError):
            self.data_filters.get_cost_by_model_id(model_id)
