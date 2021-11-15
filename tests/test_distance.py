# tests/test_lib.py
from mlproject.distance import haversine


def test_type_distance():
    assert type(haversine(2,3,4,5)) == float
