try:
    from flask import Blueprint as Bp, render_template as rt, request as req
    from Database.Models.cliente import Cliente
    from datetime import datetime
except ImportError as e:
    print(f"Error: {e}")
    exit()

cliente = Bp("cliente", __name__)


@cliente.route("/")
def listar_clientes():
    clientes = Cliente.select()
    return rt("lista_clientes.html", clientes=clientes)


@cliente.route("/", methods=["POST"])
def inserir_cliente():
    data = req.json

    if (
        Cliente.select().where(Cliente.email == data["email"]).exists()
        or Cliente.select().where(Cliente.telefone == data["telefone"]).exists()
    ):
        return (
            rt("error.html", error="Email ou número de telefone já cadastrados!"),
            400,
        )

    else:
        novo_usuario = Cliente.create(
            nome=data["nome"],
            email=data["email"],
            telefone=data["telefone"],
            data_nascimento=data["dataNascimento"],
        )

        return rt("item_cliente.html", cliente=novo_usuario)


@cliente.route("/new")
def form_cliente():
    return rt("form_cliente.html")


@cliente.route("/<int:cliente_id>")
def detalhe_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return rt("detalhe_cliente.html", cliente=cliente)


@cliente.route("/<int:cliente_id>/edit")
def form_edit_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return rt("form_cliente.html", cliente=cliente)


@cliente.route("/<int:cliente_id>/update", methods=["PUT"])
def atualizar_cliente(cliente_id):
    data = req.json

    cliente = Cliente.get_by_id(cliente_id)

    if (
        Cliente.select()
        .where((Cliente.email == data["email"]) & (Cliente.id != cliente_id))
        .exists()
    ) or (
        Cliente.select()
        .where((Cliente.telefone == data["telefone"]) & (Cliente.id != cliente_id))
        .exists()
    ):
        return rt("error.html", error="Email ou número de telefone já cadastrados!")

    else:
        cliente.nome = data["nome"]
        cliente.email = data["email"]
        cliente.telefone = data["telefone"]
        cliente.data_nascimento = data["dataNascimento"]
        cliente.save()

        return rt("item_cliente.html", cliente=cliente)


@cliente.route("/<int:cliente_id>", methods=["DELETE"])
def deletar_cliente(cliente_id):
    Cliente.delete_by_id(cliente_id)
    return {"Deletado com succeso": "ok"}
