from ariadne import gql, load_schema_from_path, QueryType, ObjectType, fallback_resolvers, MutationType
from ariadne.wsgi import GraphQL
# from ariadne.constants import PLAYGROUND_HTML
# from flask import Flask, request, jsonify

from backend.models import Customer

"""
type Customer {
  _id: ID!

  firstname: String!

  lastname: String!

  street: String!

  zip: String!

  city: String!

  email: String!

  defaultPrice: Float!

  invoices: [Invoice]
}
"""
# Define Resolvers
customer = ObjectType("Customer")


@customer.field("_id")
def resolve_customer_id(obj: Customer, info):
    return obj.id


@customer.field("firstname")
def resolve_customer_firstname(obj: Customer, info):
    return obj.firstname


@customer.field("lastname")
def resolve_customer_lastname(obj: Customer, info):
    return obj.lastname


@customer.field("street")
def resolve_customer_street(obj: Customer, info):
    return obj.street


@customer.field("zip")
def resolve_customer_zip(obj: Customer, info):
    return obj.zip


@customer.field("city")
def resolve_customer_city(obj: Customer, info):
    return obj.city


@customer.field("company")
def resolve_customer_company(obj: Customer, info):
    return obj.company


@customer.field("email")
def resolve_customer_email(obj: Customer, info):
    return obj.email


@customer.field("defaultPrice")
def resolve_customer_default_price(obj: Customer, info):
    return 80.0


@customer.field("invoices")
def resolve_customer_invoices(obj: Customer, info):
    return obj._invoices
