# Checkpoint 3 - Turma 1TDSPG-2024

## Instruções para o Checkpoint

Você recebeu um arquivo `.zip` contendo os seguintes arquivos:

- `checkpoint4.py`:
  - Este arquivo contém o esqueleto das funções que você deve implementar.
  - Você deve completar as funções de acordo com as especificações fornecidas.
  - Não altere o nome das funções, argumentos ou retornos.
  - Haverá uma variável `__author__` no arquivo, que você deverá preencher com um dicionário, contendo seu nome e RM. Exemplo

  ```python
    __author__ = {
        "nome": "Fulano de Tal",
        "rm": "RM123456"
    }

    def minha_funcao():
      pass
    ...
    def minha_outra_funcao():
      pass
    ...
    ```

  - Atente-se ao formato do nome e RM, pois o arquivo será validado automaticamente.

- `test_cp4.py`:
  - Este arquivo contém testes que serão utilizados para avaliar as funções que você implementará.
  - Você pode executar os testes localmente para verificar se as funções estão implementadas corretamente.
  - Não altere o conteúdo deste arquivo.
  - Estes testes são apenas uma parte da avaliação, então implemente todas as funções de acordo com as especificações.

**Atenção:** Vocês receberam metade dos casos de teste, sendo 10 casos de teste para cada função, 5 dados e 5 reservados para correção. Portanto, é importante que vocês testem suas funções com diferentes casos de teste para garantir que elas estão implementadas corretamente.

- Cada função possui peso de 2 pontos na nota final.
- Cada caso de teste possui o peso de 0,2 pontos na nota final.

### Entrega

- Apenas o arquivo `checkpoint4.py` deverá ser entregue.
- Atenção com submissões erradas, pois não será possível realizar a troca do arquivo após a entrega.

## Questão 1

Você recebeu a seguinte lista de dicionários, onde cada dicionário representa uma pessoa com nome, idade e status de estudante (`True` ou `False`):

```python
pessoas = [
    {"nome": "Alice", "idade": 25, "estudante": True},
    {"nome": "Carlos", "idade": 30, "estudante": False},
    {"nome": "Bianca", "idade": 22, "estudante": True},
    {"nome": "Daniel", "idade": 28, "estudante": False}
]
```

Escreva uma função `filtrar_estudantes(pessoas)` que receba essa lista e retorne uma nova lista contendo apenas as pessoas que são estudantes (`estudante == True`). A função deve retornar a lista com dicionários formatados da seguinte forma: `{"nome": nome, "idade": idade}`.

---

## Questão 2  

Com base na função `filtrar_estudantes(pessoas)` criada na questão anterior, escreva uma função chamada `calcular_media_idade` que receba a lista filtrada de estudantes e retorne a média da idade dos estudantes. Caso a lista de estudantes esteja vazia, a função deve retornar `None`.

---

## Questão 3  

Utilizando a função `calcular_media_idade` desenvolvida na questão anterior, crie uma nova função chamada `adicionar_novo_estudante` que receba a lista original de `pessoas` e adicione um novo estudante ao dicionário, apenas se a média de idade dos estudantes existentes for menor que 25. O novo estudante deve ser um dicionário com nome, idade e status de estudante, fornecidos como argumentos para a função.

---

## Questão 4  

Com base na função `adicionar_novo_estudante`, escreva uma função `atualizar_estudantes` que receba a lista original de `pessoas` e um dicionário com as informações de um novo estudante. A função deve verificar se o nome do estudante já existe na lista. Caso o nome já exista, a função deve atualizar a idade e o status de estudante, caso contrário, deve adicionar o novo estudante à lista.

Use blocos `try/except` para garantir que a função manipule corretamente entradas mal formatadas (por exemplo, um dicionário faltando a chave "nome" ou "idade").

---

## Questão 5  

Com base na lista final de `pessoas` gerada após as modificações feitas nas questões anteriores, crie uma função chamada `calcular_media_por_status` que receba a lista de `pessoas` e calcule a média de idade separadamente para estudantes e não-estudantes. A função deve retornar um dicionário com duas chaves: `"media_estudantes"` e `"media_nao_estudantes"`, contendo as médias calculadas. A função deve garantir que, caso a lista de estudantes ou não-estudantes esteja vazia, o valor correspondente no dicionário seja `None`.
