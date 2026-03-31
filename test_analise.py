from analise import calcular_roi
import pytest

def test_roi_padrao():
    assert calcular_roi(1000, 3000) == 200.0

def test_roi_prejuizo():
    assert calcular_roi(1000, 500) == -50.0

def test_roi_equilibrio():
    assert calcular_roi(1000, 1000) == 0.0

def test_roi_investimento_zero():
    assert calcular_roi(0, 500) == 0

def test_roi_valores_altos():
    assert calcular_roi(1000000, 2000000) == 100.0