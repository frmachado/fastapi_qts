import time, pytest
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, cobranca",
    [
        (0, "BASICO", -1, -1.0),
        (2, "PREMIUM", 4, 6.84),

        (1, "Basico", 2, 6.01),
        (1, "pr emium", 2, -2.0),
        (1, "empre sarial", 2, -2.0),
        (1, "", 2, -2.0),

        (1, "BASICO", 0, 1.0),
        (2, "PREMIUM", 0, 1.8),
        (3, "EMPRESARIAL", 0, 2.4),

        (10, "BASICO", 0, 10.0),
        (10, "BASICO", 1, 15.05),
        (10, "BASICO", 15, 15.75),
        (10, "BASICO", 30, 16.5),
        (10, "BASICO", 31, 38.1),

                
    ]
)
def test_calcular_entradas_validas(valor_base,plano, dias_atraso, cobranca):
    assert processar_cobranca(valor_base, plano, dias_atraso ) == cobranca

def test_calcular_tempo_execusao():
    inicio = time.perf_counter()
    resultado = processar_cobranca(1, "BASICO", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado > 0.0
    assert tempo_decorrido < 0.1