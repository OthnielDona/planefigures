"""Tests for polygon function"""
import pytest
import planefigures as figures

def test_rectangle_on_string_arguments():
    with pytest.raises(TypeError):
        figures.rectangle('12',12)

    with pytest.raises(TypeError):
        figures.rectangle(12,'12')

def test_rectangle_on_float_arguments():
    with pytest.raises(TypeError):
        figures.rectangle(12.5,12)

    with pytest.raises(TypeError):
        figures.rectangle(12,12.4)