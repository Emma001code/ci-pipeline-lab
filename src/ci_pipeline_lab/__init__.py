"""A tiny temperature converter used to practice continuous integration."""

from ci_pipeline_lab.temperature import celsius_to_fahrenheit


def main() -> None:
    """Print the Fahrenheit equivalent of water's freezing point."""
    freezing_celsius = 0
    freezing_fahrenheit = celsius_to_fahrenheit(freezing_celsius)
    print(f"{freezing_celsius}°C is {freezing_fahrenheit}°F")
