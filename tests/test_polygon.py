"""Tests for polygon function"""
import pytest
import planefigures as figures

def test_polygon_on_string_arguments():
    with pytest.raises(TypeError):
        figures.polygon('12',12)

    with pytest.raises(TypeError):
        figures.polygon(12,'12')

def test_polygon_on_float_arguments():
    with pytest.raises(TypeError):
        figures.polygon(12.5,12)

    with pytest.raises(TypeError):
        figures.polygon(12,12.4)