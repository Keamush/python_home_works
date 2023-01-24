from typing import NamedTuple, Tuple, Union


class PlanetData(NamedTuple):
    """Planet data DTO"""
    planet_size: Tuple[float, float]
    planet_color: Union[str, Tuple[float, float, float]]
    radius: int
    increase_angle: float
    name: str = 'planet'
