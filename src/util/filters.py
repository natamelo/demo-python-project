from .exceptions import NotFoundError


class DataFilter:

    def __init__(self, data):
        self.data = data

    def get_model_by_id(self, model_id):
        if model_id in self.data:
            return self.data[model_id]
        raise NotFoundError('model', args={'model_id': model_id})

    def get_ratios_by_params(self, model_id, year):
        model = self.get_model_by_id(model_id)
        years = model['schedule']['years']
        if year in years:
            return years[year]
        raise NotFoundError('ratios', args={'model_id': model_id, 'year': year})

    def get_cost_by_model_id(self, model_id):
        model = self.get_model_by_id(model_id)
        return model['saleDetails']['cost']
