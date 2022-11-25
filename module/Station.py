from dataclasses import dataclass
from Route import Route, RouteInfo
from Staff import Passenger

@dataclass
class StationInfo:
    """Info about station.
    Args:
        passenger_id (int): Passenger ID.
        city (str): City where station
        transport(str): transport model
        routes (list): list of routes
    """
    passenger_id: int
    city: str
    transport: str
    routes: list

class Station:

    def __init__(self):
        self._station_info = None

    def station_info(self) -> str:
        return self._station_info

    def station_info(self, station_info: StationInfo) -> None:
        if isinstance(station_info, StationInfo):
            self._station_info = station_info

    def create_route(self, finish_of_trip: str, amount: int, transport_model: str) -> str:
        for route_id in range(0, amount):
            new_route = Route()
            new_route_info = RouteInfo(id, self._station_info.city, finish_of_trip, transport_model)
            new_route.route_info = new_route_info
            self._station_info.routes.append(new_route)

        return f"Added routes:\nAmount routes: {amount}\nFrom: {self._station_info.city} to " \
               f"{finish_of_trip}\nTransport model: {transport_model}"

    def write_all_routes(self) -> str:
        result = f""
        if not self._station_info.routes:
            result += f"No available routes"
        else:
            for i in range(0, len(self._station_info.routes)):
                result += f"{self._station_info.routes[i].route_info}\n"
        return result

    def take_route(self, passenger: Passenger) -> str:
        amount_of_routes = len(self._station_info.routes)
        passenger.passenger_info_.routes.append(self._station_info.routes[amount_of_routes-1].route_info.id)
        self._station_info.routes.remove(self._station_info.routes[amount_of_routes-1])
        return f"Passenger chose route with ID: {passenger.passenger_info_.routes}"