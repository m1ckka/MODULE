from dataclasses import dataclass

@dataclass
class RouteInfo:
    """Info about route
    Args:
        id (int) Route ID.
        start_of_trip (str): Beginning of the route.
        finish_of_trip (str): End of the route.
        transport_model (str): Model of transport.
    """
    id: int
    start_of_trip: str
    finish_of_trip: str
    transport_model: str

class Route:

    def __init__(self) -> None:
        self._route_info = None

    def route_info(self):
        return self._route_info

    def route_info(self, route_info: RouteInfo) -> None:
        if isinstance(route_info, RouteInfo):
            self._route_info = route_info

    def route_info(self, RouteInfo: RouteInfo) -> None:
        if isinstance(RouteInfo, RouteInfo):
            self._RouteInfo = RouteInfo
