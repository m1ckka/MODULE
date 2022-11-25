from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class TransportInfo:
    """Info about transport.
    Args:
        id (int): Transport id.
        model (str): Transport model
        passengers_limit (int): Limit of passengers.
        weight_limit (int): Limit of weight.
    """
    id: int
    model: str
    passengers_limit: int
    weight_limit: int

class Transport(ABC):
    def __init__(self):
        self._transport_info = None
        self.driver = None
        self.model = None

    def transport_info(self):
        return self._transport_info

    def transport_info(self, transport_info: TransportInfo):
        if isinstance(transport_info, TransportInfo):
            self._transport_info = transport_info

    def add_driver(self, driver) -> str:
        self.driver = driver
        return f"Added driver."

    def add_model(self, transport_model: str) -> str:
        self.model = transport_model
        return f"Added model. {self.model}"

class Train(Transport):
    def add_driver(self, driver) -> str:
        self.driver = driver
        return f"Added driver with ID: {self.driver.driver_info[0]}."

    def add_model(self, transport_model: str = "Train") -> str:
        self.model = transport_model
        return f"Transport model is: {self.model}."
