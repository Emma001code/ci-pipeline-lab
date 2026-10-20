
import os

"""Convert temperatures between Celsius and Fahrenheit."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Return the Fahrenheit equivalent of a Celsius temperature."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Return the Celsius equivalent of a Fahrenheit temperature."""
    return (fahrenheit - 32) * 5 / 9
