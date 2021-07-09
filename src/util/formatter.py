from .exceptions import InputError


class InputFormatter:

    @staticmethod
    def _extract_values_from_pair(input_value):
        input_value = input_value.upper()
        if 'ID' in input_value and 'YEAR' in input_value:
            id_index = input_value.index('ID')
            year_index = input_value.index('YEAR')
            id = input_value[id_index + 3:].strip()
            year = input_value[year_index + 5: id_index].strip()
            if id.isdigit() and year.isdigit():
                return {"id": id, "year": year}
        raise InputError()

    @staticmethod
    def extract_values(line):
        inputs = line.split(',')
        return [InputFormatter._extract_values_from_pair(item) for item in inputs]
