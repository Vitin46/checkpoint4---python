import pytest
from checkpoint4 import (
    filtrar_estudantes,
    calcular_media_idade,
    adicionar_novo_estudante,
    atualizar_estudantes,
    calcular_media_por_status,
)


@pytest.fixture
def sample_data():
    return [
        {"nome": "Alice", "idade": 25, "estudante": True},
        {"nome": "Carlos", "idade": 30, "estudante": False},
        {"nome": "Bianca", "idade": 22, "estudante": True},
        {"nome": "Daniel", "idade": 28, "estudante": False},
    ]


@pytest.mark.parametrize(
    "pessoas, target, expected",
    [
        # Caso 1: Dados da fixture original
        (
            [
                {"nome": "Alice", "idade": 25, "estudante": True},
                {"nome": "Carlos", "idade": 30, "estudante": False},
                {"nome": "Bianca", "idade": 22, "estudante": True},
                {"nome": "Daniel", "idade": 28, "estudante": False},
            ],
            False,
            [{"nome": "Carlos", "idade": 30}, {"nome": "Daniel", "idade": 28}],
        ),
        # Caso 2: Dados diferentes, com outros nomes
        (
            [
                {"nome": "John", "idade": 20, "estudante": True},
                {"nome": "Jane", "idade": 22, "estudante": True},
                {"nome": "Doe", "idade": 30, "estudante": False},
                {"nome": "Smith", "idade": 40, "estudante": False},
            ],
            True,
            [{"nome": "John", "idade": 20}, {"nome": "Jane", "idade": 22}],
        ),
        # Caso 3: Outros dados
        (
            [
                {"nome": "Mark", "idade": 21, "estudante": True},
                {"nome": "Tom", "idade": 35, "estudante": False},
                {"nome": "Eva", "idade": 19, "estudante": True},
                {"nome": "Lucy", "idade": 32, "estudante": False},
            ],
            False,
            [{"nome": "Tom", "idade": 35}, {"nome": "Lucy", "idade": 32}],
        ),
        # Casos com lista vazia
        ([], True, []),  # Nenhuma pessoa
        # Casos com apenas estudantes ou não estudantes
        (
            [{"nome": "Doe", "idade": 30, "estudante": False}],
            False,
            [{"nome": "Doe", "idade": 30}],
        ),
    ],
)
def test_filtrar_estudantes(pessoas, target, expected):
    result = filtrar_estudantes(pessoas, target)
    assert result == expected


@pytest.mark.parametrize(
    "sample_data, expected",
    [
        ([{"nome": "Carlos", "idade": 30, "estudante": False}], None),
        (
            [
                {"nome": "Alice", "idade": 25, "estudante": True},
                {"nome": "Carlos", "idade": 30, "estudante": False},
            ],
            25,
        ),
        ([{"nome": "John", "idade": 20, "estudante": True}], 20),
        (
            [
                {"nome": "Mark", "idade": 21, "estudante": True},
                {"nome": "Tom", "idade": 35, "estudante": True},
            ],
            28,
        ),
        (
            [
                {"nome": "Eva", "idade": 19, "estudante": True},
                {"nome": "Lucy", "idade": 32, "estudante": False},
            ],
            19,
        ),
    ],
)
def test_calcular_media_idade(sample_data, expected, mocker):
    mock_filtrar_estudantes = mocker.patch(
        "checkpoint4.filtrar_estudantes",
        return_value=[p for p in sample_data if p["estudante"]],
    )

    media_idade = calcular_media_idade(sample_data)

    mock_filtrar_estudantes.assert_called_once_with(sample_data)
    assert media_idade == expected


@pytest.mark.parametrize(
    "sample_data, nome, idade, estudante, expected_length",
    [
        ([{"nome": "Carlos", "idade": 30, "estudante": False}], "Alice", 24, True, 2),
        (
            [
                {"nome": "Alice", "idade": 25, "estudante": True},
                {"nome": "Bianca", "idade": 22, "estudante": True},
            ],
            "Carlos",
            28,
            True,
            3,
        ),
        ([{"nome": "Daniel", "idade": 28, "estudante": False}], "Jane", 22, True, 2),
        ([{"nome": "Smith", "idade": 40, "estudante": False}], "Eva", 19, True, 2),
        ([{"nome": "Alice", "idade": 25, "estudante": True}], "Carlos", 30, True, 2),
    ],
)
def test_adicionar_novo_estudante(
    sample_data, nome, idade, estudante, expected_length, mocker
):
    mock_calcular_media_idade = mocker.patch(
        "checkpoint4.calcular_media_idade", return_value=23
    )

    adicionar_novo_estudante(sample_data, nome, idade, estudante)

    mock_calcular_media_idade.assert_called_once_with(sample_data)
    assert len(sample_data) == expected_length
    assert any(
        p["nome"] == nome and p["idade"] == idade and p["estudante"] == estudante
        for p in sample_data
    )


@pytest.mark.parametrize(
    "sample_data, novo_estudante, expected_result",
    [
        (
            [{"nome": "Carlos", "idade": 30, "estudante": False}],
            {"nome": "Carlos", "idade": 31, "estudante": True},
            1,
        ),
        (
            [{"nome": "Carlos", "idade": 30, "estudante": False}],
            {"nome": "John", "idade": 20, "estudante": True},
            2,
        ),
        (
            [{"nome": "Doe", "idade": 30, "estudante": True}],
            {"nome": "Mark", "idade": 21, "estudante": True},
            2,
        ),
        (
            [{"nome": "Lucy", "idade": 32, "estudante": False}],
            {"nome": "Tom", "idade": 35, "estudante": True},
            2,
        ),
        (
            [{"nome": "Alice", "idade": 25, "estudante": True}],
            {"nome": "Carlos", "idade": 30, "estudante": True},
            2,
        ),
    ],
)
def test_atualizar_estudantes(sample_data, novo_estudante, expected_result, mocker):
    mock_adicionar_novo_estudante = mocker.patch("checkpoint4.adicionar_novo_estudante")

    atualizar_estudantes(sample_data, novo_estudante)

    if novo_estudante["nome"] in [p["nome"] for p in sample_data]:
        assert mock_adicionar_novo_estudante.called is False
        assert any(
            p["nome"] == novo_estudante["nome"]
            and p["idade"] == novo_estudante["idade"]
            and p["estudante"] == novo_estudante["estudante"]
            for p in sample_data
        )
    else:
        mock_adicionar_novo_estudante.assert_called_once_with(
            sample_data,
            novo_estudante["nome"],
            novo_estudante["idade"],
            novo_estudante["estudante"],
        )
        assert len(sample_data) == expected_result


@pytest.mark.parametrize(
    "sample_data, expected",
    [
        (
            [{"nome": "Carlos", "idade": 30, "estudante": False}],
            {"media_estudantes": None, "media_nao_estudantes": 30},
        ),
        (
            [
                {"nome": "Bianca", "idade": 22, "estudante": True},
                {"nome": "Daniel", "idade": 28, "estudante": False},
            ],
            {"media_estudantes": 22, "media_nao_estudantes": 28},
        ),
        (
            [{"nome": "John", "idade": 20, "estudante": True}],
            {"media_estudantes": 20, "media_nao_estudantes": None},
        ),
        (
            [
                {"nome": "Mark", "idade": 21, "estudante": True},
                {"nome": "Tom", "idade": 35, "estudante": False},
            ],
            {"media_estudantes": 21, "media_nao_estudantes": 35},
        ),
        (
            [{"nome": "Doe", "idade": 30, "estudante": False}],
            {"media_estudantes": None, "media_nao_estudantes": 30},
        ),
    ],
)
def test_calcular_media_por_status(sample_data, expected, mocker):
    mock_filtrar_estudantes = mocker.patch(
        "checkpoint4.filtrar_estudantes",
        side_effect=[
            [p for p in sample_data if p["estudante"]],
            [p for p in sample_data if not p["estudante"]],
        ],
    )

    medias = calcular_media_por_status(sample_data)

    mock_filtrar_estudantes.assert_any_call(sample_data, target=True)
    mock_filtrar_estudantes.assert_any_call(sample_data, target=False)

    assert medias == expected
