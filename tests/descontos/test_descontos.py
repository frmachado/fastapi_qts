from app.descontos.descontos import calcular_desconto


def test_valor_zero():
    assert calcular_desconto(0, True) == 0


def test_valor_negativo():
    assert calcular_desconto(-100, False) == 0


def test_cliente_vip():
    assert calcular_desconto(100, True) == 80


def test_cliente_nao_vip():
    assert calcular_desconto(100, False) == 90


def test_valor_pequeno_vip():
    resultado = calcular_desconto(0.01, True)
    assert round(resultado, 3) == 0.008


def test_valor_pequeno_nao_vip():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.009


def test_valor_alto_vip():
    assert calcular_desconto(200, True) == 160


def test_valor_alto_nao_vip():
    assert calcular_desconto(200, False) == 180
    