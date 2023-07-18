__version__ = '0.0.0'

import json
from typing import Any

import requests


class GeophiresSimulationParameters:
    def __init__(self):
        self._parameters = {}

    def get_parameters(self) -> dict:
        return self._parameters

    def with_gradient_1(self, gradient_1: float):
        return self.with_parameter('Gradient 1', gradient_1)

    def with_maximum_temperature(self, max_temp: float):
        return self.with_parameter('Maximum Temperature', max_temp)

    def with_reservoir_model(self, reservoir_model: int):
        return self.with_parameter('Reservoir Model', reservoir_model)

    def with_parameter(self, parameter_name: str, parameter_value: Any):
        self._parameters[parameter_name] = parameter_value
        return self


class GeophiresSimulationRequest:
    def __init__(self, simulation_parameters: GeophiresSimulationParameters):
        self._simulation_parameters = simulation_parameters

    def get_simulation_parameters(self) -> GeophiresSimulationParameters:
        return self._simulation_parameters


class GeophiresSimulationResult:
    def __init__(self):
        pass


class GeophiresServiceClient:
    def __init__(self, endpoint: str = 'https://xi0du897va.execute-api.us-west-2.amazonaws.com/'):
        self._endpoint = endpoint

    def get_geophires_simulation_result(self, geophires_simulation_request: GeophiresSimulationRequest):
        # -> GeophiresSimulationResult:
        response = requests.post(
            self._endpoint,
            json={'geophires_input_parameters': geophires_simulation_request.get_simulation_parameters().get_parameters()},
            timeout=30,
        )
        return json.loads(response.text)
