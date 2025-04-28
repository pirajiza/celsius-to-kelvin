def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero!")
    return celsius + 273.15



def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32
