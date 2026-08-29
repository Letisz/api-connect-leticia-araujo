usuarios = [
    {
        "id": 1,
        "nome": "Ana Silva",
        "email": "ana@email.com"
    },
    {
        "id": 2,
        "nome": "Carlos Souza",
        "email": "carlos@email.com"
    }
]

proximo_id = 3


def gerar_id():
    global proximo_id

    novo_id = proximo_id
    proximo_id += 1

    return novo_id
