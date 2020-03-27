from ariadne import gql, load_schema_from_path, QueryType, ObjectType, fallback_resolvers, MutationType
from ariadne.wsgi import GraphQL
# from ariadne.constants import PLAYGROUND_HTML
# from flask import Flask, request, jsonify

from backend.models import InvoiceItem

"""
type invoice_itemItem {
  pos: Int!

  description: String!

  amount: Int!

  price: Float!

  invoice: Invoice
}
"""
# Define Resolvers
invoice_item = ObjectType("InvoiceItem")


@invoice_item.field("pos")
def resolve_invoice_item_pos(obj: InvoiceItem, info):
    return obj.pos


@invoice_item.field("description")
def resolve_invoice_item_description(obj: InvoiceItem, info):
    return obj.description


@invoice_item.field("amount")
def resolve_invoice_item_amount(obj: InvoiceItem, info):
    return obj.amount


@invoice_item.field("price")
def resolve_invoice_item_price(obj: InvoiceItem, info):
    return obj.price


@invoice_item.field("invoice")
def resolve_invoice_item_invoice(obj: InvoiceItem, info):
    return obj._invoice
