import dataclasses


class Item:
    def __init__(self) -> None:
        pass


class Path:
    def __init__(self) -> None:
        pass


class Crossroad:
    def __init__(self) -> None:
        pass


class Road:
    """This class represents a single road connecting two crossroads. It contains cars and items on the road."""

    def __init__(self, path: Path, cross_0: Crossroad, cross_1: Crossroad) -> None:
        assert isinstance(path, Path), f"Expected Path, got {type(path)}"
        assert isinstance(cross_0, Crossroad), f"Expected Crossroad, got {type(cross_0)}"
        assert isinstance(cross_1, Crossroad), f"Expected Crossroad, got {type(cross_1)}"
        self._path = path
        self._cross_0 = cross_0
        self._cross_1 = cross_1
        self._cars: list[Car] = []
        self._items: list[Item] = []


@dataclasses.dataclass(frozen=True, slots=True)
class CarProperties:
    max_speed: float
    mass: float


class Car:
    def __init__(self, properties: CarProperties, road: Road):
        self._road = road
        self._position = 0
        self._speed = 0
        self._properties = properties

    def update(self, dt: float) -> None:
        pass

    def distance_to(self, car: "Car") -> float:
        return 0
