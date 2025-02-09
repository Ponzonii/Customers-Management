# Import necessary modules and handle import errors
try:
    from flask import Blueprint as Bp, render_template as rt, request as req
    from Database.Models.cliente import Cliente
except ImportError as e:
    print(f"Error: {e}")
    exit()

# Create a Blueprint for cliente routes
cliente = Bp("cliente", __name__)

# Route to list all clients
@cliente.route("/list")
def listar_clientes():
    clientes = Cliente.select()
    return rt("lista_clientes.html", clientes=clientes)

# Route to insert a new client
@cliente.route("/new", methods=["POST"])
def inserir_cliente():
    data = req.json

    # Check if email or phone number already exists
    if (
        Cliente.select().where(Cliente.email == data["email"]).exists()
        or Cliente.select().where(Cliente.telefone == data["telefone"]).exists()
    ):
        return (
            rt("error.html", error="Email ou número de telefone já cadastrados!"),
            400,
        )
    else:
        # Create a new client
        novo_usuario = Cliente.create(
            nome=data["nome"],
            email=data["email"],
            telefone=data["telefone"],
            data_nascimento=data["dataNascimento"],
        )
        return rt("item_cliente.html", cliente=novo_usuario)

# Route to display the form for creating a new client
@cliente.route("/form/new")
def form_cliente():
    return rt("form_cliente.html")

# Route to display client details
@cliente.route("/<int:cliente_id>/details")
def detalhe_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return rt("detalhe_cliente.html", cliente=cliente)

# Route to display the form for editing a client
@cliente.route("/<int:cliente_id>/form/edit")
def form_edit_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return rt("form_cliente.html", cliente=cliente)

# Route to update a client's information
@cliente.route("/<int:cliente_id>/update", methods=["PUT"])
def atualizar_cliente(cliente_id):
    data = req.json
    cliente = Cliente.get_by_id(cliente_id)

    # Check if email or phone number already exists for another client
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
        # Update client information
        cliente.nome = data["nome"]
        cliente.email = data["email"]
        cliente.telefone = data["telefone"]
        cliente.data_nascimento = data["dataNascimento"]
        cliente.save()
        return rt("item_cliente.html", cliente=cliente)

# Route to delete a client
@cliente.route("/<int:cliente_id>/delete", methods=["DELETE"])
def deletar_cliente(cliente_id):
    cliente_delete = Cliente.delete_by_id(cliente_id)

    if cliente_delete == 1:
        return {"Deletado com succeso": "ok"}
    # TODO: implementar mensagem de erro caso não seja possível deletar um cliente