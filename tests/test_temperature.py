"""Tests for temperature conversion."""

import pytest

from ci_pipeline_lab.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_freezing_point_is_32_fahrenheit() -> None:
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point_is_212_fahrenheit() -> None:
    assert celsius_to_fahrenheit(100) == 212


def test_scales_meet_at_minus_40() -> None:
    assert celsius_to_fahrenheit(-40) == -40
    assert fahrenheit_to_celsius(-40) == -40


def test_round_trip_returns_original_celsius() -> None:
    original = 37.0
    converted = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
    assert converted == pytest.approx(original)
