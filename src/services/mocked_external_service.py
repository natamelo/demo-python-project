import json


class MockedAPI:

    @staticmethod
    def get_mocked_service():
        with open('data/api-response.json', 'r') as file:
            data = json.load(file)
        return data
