from os import stat


class Calculator:

    @staticmethod
    def calculate(ratio, cost):
        return ratio * cost

    @staticmethod
    def calculate_values(cost, **args):
        return {(ratio[0].capitalize() + ratio[1:]): Calculator.calculate(value, cost) for ratio, value in args.items()}
