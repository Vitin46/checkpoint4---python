__author__ = {
    "nome": "Victor Egidio Lira",
    "rm": "RM556653",
}


# Questão 1: Filtrar estudantes
def filtrar_estudantes(pessoas, target=True):
    """
    Filtra as pessoas que são estudantes ou não-estudantes,
    com base no parâmetro 'target'.

    :param pessoas: lista de dicionários representando as pessoas
    :param target: booleano, True para filtrar estudantes, False para não-estudantes
    :return: lista filtrada de dicionários com nome e idade
    """
    # Comece a implementação aqui

    return [
        {"nome": pessoa["nome"], "idade": pessoa["idade"]}
        for pessoa in pessoas
        if pessoa["estudante"] == target
    ]


# Questão 2: Calcular média de idade dos estudantes
def calcular_media_idade(pessoas):
    """
    Calcula a média de idade das pessoas filtradas como estudantes.

    :param pessoas: lista de dicionários representando as pessoas
    :return: média da idade dos estudantes ou None se não houver estudantes
    """
    # A função deverá obrigatoriamente chamar a função filtrar_estudantes
    estudantes = filtrar_estudantes(pessoas)

    # Comece a implementação aqui
    if not estudantes:
        return None

    total_idade = sum(estudante["idade"] for estudante in estudantes)
    
    media_idade = total_idade / len(estudantes)
    
    return media_idade   


# Questão 3: Adicionar novo estudante se a média de idade for menor que 25
def adicionar_novo_estudante(pessoas, nome, idade, estudante=True):
    """
    Adiciona um novo estudante à lista de pessoas se a média de idade dos
    estudantes existentes for menor que 25.

    :param pessoas: lista de dicionários representando as pessoas
    :param nome: string, nome do novo estudante
    :param idade: inteiro, idade do novo estudante
    :param estudante: booleano, status de estudante (True por padrão)
    """
    # A função deverá obrigatoriamente chamar a função calcular_media_idade
    media_estudantes = calcular_media_idade(pessoas)

    # Comece a implementação aqui

    if media_estudantes is None or media_estudantes < 25:
        pessoas.append({"nome": nome, "idade": idade, "estudante": estudante})

    # Não retorna nada, pois apenas modifica a lista pessoas


# Questão 4: Atualizar estudantes ou adicionar novo estudante
def atualizar_estudantes(pessoas, novo_estudante):
    """
    Atualiza as informações de um estudante na lista de pessoas ou
    adiciona um novo estudante se ele não estiver presente.

    :param pessoas: lista de dicionários representando as pessoas
    :param novo_estudante: dicionário com as informações do novo estudante
    """

    # comece a implementação aqui
    nome_novo_estudante = novo_estudante["nome"]
    idade_novo_estudante = novo_estudante["idade"]
    estudante_novo_estudante = novo_estudante["estudante"]

    encontrado = False

    for pessoa in pessoas:
        if pessoa["nome"] == nome_novo_estudante:
            # Atualiza as informações do estudante existente
            pessoa["idade"] = idade_novo_estudante
            pessoa["estudante"] = estudante_novo_estudante
            encontrado = True
            break
    
    
    # deverá chamar a função adicionar_novo_estudante,
    # caso atenda aos critérios
    if not encontrado:
        # Adiciona o novo estudante diretamente à lista pessoas
        pessoas.append({
            "nome": nome_novo_estudante,
            "idade": idade_novo_estudante,
            "estudante": estudante_novo_estudante,
        })
    # Não retorna nada, pois apenas modifica a lista pessoas


# Questão 5: Calcular média de idade por status de estudante
def calcular_media_por_status(pessoas):
    """
    Calcula a média de idade separadamente para estudantes e não-estudantes.

    :param pessoas: lista de dicionários representando as pessoas
    :return: dicionário com as médias de idade dos estudantes e não-estudantes
    """
    # Comece a implementação aqui

    estudantes = filtrar_estudantes(pessoas)
    nao_estudantes = [{"nome": pessoa["nome"], "idade": pessoa["idade"]} for pessoa in pessoas if pessoa["estudante"] is False]

    media_estudantes = calcular_media_idade(estudantes)
    media_nao_estudantes = calcular_media_idade(nao_estudantes)

    return {
        "media_estudantes": media_estudantes,
        "media_nao_estudantes": media_nao_estudantes,
    }
