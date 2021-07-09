from src.util.exceptions import NotFoundError
from .mocked_external_service import MockedAPI
from src.util.filters import DataFilter
from src.util.calculator import Calculator
from collections import namedtuple


class RatioService:

    @staticmethod
    def calculate_values_by_params(model_id, year):
        data = MockedAPI.get_mocked_service()
        filters = DataFilter(data)

        try:
            ratios = filters.get_ratios_by_params(model_id, year)
            cost = filters.get_cost_by_model_id(model_id)

            values = Calculator.calculate_values(cost, **ratios)
            valid = True

        except NotFoundError:
            values = {}
            valid = False

        return RatioService._convert_to_object(model_id, year, valid, values)

    @staticmethod
    def calculate_values(inputs):
        return [RatioService.calculate_values_by_params(item['id'], item['year']) for item in inputs]

    @staticmethod
    def _convert_to_object(model_id, year, valid, ratios):
        Result = namedtuple('Result', ['id', 'year', 'valid', 'ratios'])
        return Result(model_id, year, valid, ratios)
