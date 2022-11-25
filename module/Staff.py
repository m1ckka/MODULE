from Route import Route
from dataclasses import dataclass

@dataclass

class DriverInfo:
    """Info about driver.
    Args:
        driver_id (int): Driver ID
        full_name (str): Drivers first name
        date_of_birth (int): Drivers date of birth
        experience (int): Driver work experience
    """
    driver_id: int
    full_name: str
    date_of_birth: int
    experience: int

class Driver:
    def __init__(self):
        self.driver_info_ = None

    def driver_info(self):
        return self.driver_info_

    def driver_info(self, driver_info: DriverInfo):
        if isinstance(driver_info, DriverInfo):
            self.driver_info_ = driver_info


class PassengerInfo:
    """Info about Passenger.
    Args:
    passenger_id (int): Passenger ID.
    full_name (str): Passenger full name.
    Date_of_birth (int): Passenger date of birth
    Routes (list): list of routes
    """
    id: int
    full_name: str
    date_of_birth: int
    routes: list

class Passenger:

    def __init__(self) -> None:
        self.passenger_info_ = None

    def passenger_info(self):
        return self.passenger_info_

    def passenger_info(self, passenger_info_: PassengerInfo) -> None:
        if isinstance(passenger_info_, PassengerInfo):
            self.passenger_info_ = passenger_info_

    def add_route(self, route: Route) -> str:
        if route.route_info.id in self.passenger_info_.routes:
            raise ValueError(f"Already exists.")
        else:
            self.passenger_info_.routes.append(route.route_info.id)
            return f"New route id: {route.route_info.id}"

    def delete_route(self, route: Route) -> str:
        if route.route_info.id in self.passenger_info_.routes:
            self.passenger_info_.routes.remove(route.route_info.id)
            return f"Route id: {route.route_info.id} deleted."
        else:
            raise ValueError(f"Route id doesn't exist")
