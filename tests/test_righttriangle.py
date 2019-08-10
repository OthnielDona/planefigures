"""Tests for right triangle function"""
import pytest
import planefigures as figures

def test_righttriangle_on_string_arguments():
    with pytest.raises(TypeError):
        figures.righttriangle('12', 12, 60)

    with pytest.raises(TypeError):
        figures.righttriangle(12, '12', 60)

    with pytest.raises(TypeError):
        figures.righttriangle(12, 12, '60')

def test_minimum_arguments(capsys):
    figures.righttriangle(60)
    captured = capsys.readouterr()
    assert 'provide at least two' in captured.out