from flask import Blueprint

from controllers.connect_controller import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    excluir_usuario
)

connect_routes = Blueprint("connect_routes", __name__)


@connect_routes.route("/usuarios", methods=["POST"])
def criar_usuario():
    return cadastrar_usuario()


@connect_routes.route("/usuarios", methods=["GET"])
def obter_usuarios():
    return listar_usuarios()


@connect_routes.route("/usuarios/<int:id_usuario>", methods=["GET"])
def obter_usuario(id_usuario):
    return buscar_usuario(id_usuario)


@connect_routes.route("/usuarios/<int:id_usuario>", methods=["PUT"])
def editar_usuario(id_usuario):
    return atualizar_usuario(id_usuario)


@connect_routes.route("/usuarios/<int:id_usuario>", methods=["DELETE"])
def remover_usuario(id_usuario):
    return excluir_usuario(id_usuario)
