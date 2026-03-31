from analise import calcular_roi

def test_calculo_roi_positivo():
    assert calcular_roi(1000, 3000) == 200.0

def test_calculo_roi_zero():
    assert calcular_roi(0, 1000) == 0