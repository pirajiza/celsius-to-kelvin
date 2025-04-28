import pytest
from src.converter import celsius_to_kelvin, kelvin_to_fahrenheit

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15
    assert round(celsius_to_kelvin(-273.15), 2) == 0.00
    with pytest.raises(ValueError):
        celsius_to_kelvin(-274)

def test_kelvin_to_fahrenheit():
    assert round(kelvin_to_fahrenheit(273.15), 2) == 32.00
    assert round(kelvin_to_fahrenheit(373.15), 2) == 212.00
    assert round(kelvin_to_fahrenheit(0), 2) == -459.67

