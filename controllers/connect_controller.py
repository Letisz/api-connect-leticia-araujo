from flask import request, jsonify
from data.connect_data import usuarios, gerar_id


def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "O corpo da requisicao e obrigatorio."
        }), 400

    if "nome" not in dados or "email" not in dados:
        return jsonify({
            "error": "Os campos nome e email sao obrigatorios."
        }), 400

    if not isinstance(dados["nome"], str) or not dados["nome"].strip():
        return jsonify({
            "error": "O campo nome nao pode estar vazio."
        }), 400

    if not isinstance(dados["email"], str) or not dados["email"].strip():
        return jsonify({
            "error": "O campo email nao pode estar vazio."
        }), 400

    novo_usuario = {
        "id": gerar_id(),
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201


def listar_usuarios():
    return jsonify({
        "data": usuarios
    }), 200


def buscar_usuario(id_usuario):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuario nao encontrado."
    }), 404


def atualizar_usuario(id_usuario):
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            dados = request.get_json()

            if not dados:
                return jsonify({
                    "error": "Dados para atualizacao sao obrigatorios."
                }), 400

            if "nome" in dados:
                if not isinstance(dados["nome"], str) or not dados["nome"].strip():
                    return jsonify({
                        "error": "O campo nome nao pode estar vazio."
                    }), 400

                usuario["nome"] = dados["nome"]

            if "email" in dados:
                if not isinstance(dados["email"], str) or not dados["email"].strip():
                    return jsonify({
                        "error": "O campo email nao pode estar vazio."
                    }), 400

                usuario["email"] = dados["email"]

            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuario nao encontrado."
    }), 404


def excluir_usuario(id_usuario):
    for indice, usuario in enumerate(usuarios):
        if usuario["id"] == id_usuario:
            usuarios.pop(indice)

            return jsonify({
                "data": {
                    "mensagem": "Usuario excluido com sucesso."
                }
            }), 200

    return jsonify({
        "error": "Usuario nao encontrado."
    }), 404
