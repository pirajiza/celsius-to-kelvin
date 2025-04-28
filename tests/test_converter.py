import pytest
from src.converter import celsius_to_kelvin

def test_zero():
    assert celsius_to_kelvin(0) == 273.15

def test_positive():
    assert celsius_to_kelvin(25) == 298.15

def test_negative():
    assert celsius_to_kelvin(-273.15) == 0.0

def test_below_absolute_zero():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-274)
