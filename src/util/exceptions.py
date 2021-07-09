class NotFoundError(Exception):

    def __init__(self, entity, **args):
        formatted = ', '.join(
            [f'{key}: {value}' for key, value in args.items()])
        super().__init__(f'{entity} not found for {formatted}')


class InputError(Exception):

    def __init__(self):
        super().__init__('Invalid input!')
