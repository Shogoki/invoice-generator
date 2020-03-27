from ariadne import gql, load_schema_from_path, QueryType, ObjectType, fallback_resolvers, MutationType
from ariadne.wsgi import GraphQL
from ariadne import make_executable_schema, graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from backend.resolvers import resolvers
from backend import app, db
#from backend.models import Invoice, Customer, InvoiceItem

# INIT DATABSE

with app.app_context():
    db.create_all()

schema = make_executable_schema(load_schema_from_path(
    "schema.graphql"), resolvers)


@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        # extensions=[ResolveBatcher],
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


#app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
