import sys
from src.util.formatter import InputFormatter
from src.services.ratio_service import RatioService

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        inputs = args[0]
        formatted = InputFormatter.extract_values(inputs)
        results = RatioService.calculate_values(formatted)
        for result in results:
            print(result)
    else:
        print('Nothing to do!')
