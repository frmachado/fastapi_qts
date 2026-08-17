import pytest
from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
"renda_mensal, score_credito, restrito, retorno_esperado",
    [
    (0.01, 400, True, "renda invalida"),
    (-1, -20, True, "renda invalida"),
    (5, -3, False, "score invalido"),
    (2, 1001, False, "score invalido"),
    (3, 700, True, "reprovado"),
    (3, 350, False, "reprovado"),
    (3, 500, False, "aprovado padrao"),
    (3, 830, False, "aprovado premium")
    ],
)


@pytest.mark.parametrize(
"renda_mensal, score_credito, restrito, retorno_esperado",
    [
    (0, 10, True, "renda invalida"),
    (-1, -20, True, "renda invalida"),
    (5, -3, False, "score invalido"),
    (2, 1001, False, "score invalido"),
    (3, 700, True, "reprovado"),
    (3, 350, False, "reprovado"),
    (3, 500, False, "aprovado padrao"),
    (3, 830, False, "aprovado premium")
    ],
)

def test_classificar_credito_caixa_preta(
    renda_mensal,score_credito,restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito ) == retorno_esperado


