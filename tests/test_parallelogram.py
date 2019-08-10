"""Tests for parallelogram function"""
import pytest
import planefigures as figures

def test_parallelogram_on_string_arguments():
    with pytest.raises(TypeError):
        figures.parallelogram('12', 12, 60)

    with pytest.raises(TypeError):
        figures.parallelogram(12, '12', 60)

    with pytest.raises(TypeError):
        figures.parallelogram(12, 12, '60')

def test_parallelogram_on_float_arguments():
    with pytest.raises(TypeError):
        figures.parallelogram(12.5, 12, 60)

    with pytest.raises(TypeError):
        figures.parallelogram(12, 12.5, 60)