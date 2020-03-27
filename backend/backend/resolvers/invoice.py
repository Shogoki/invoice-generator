from ariadne import gql, load_schema_from_path, QueryType, ObjectType, fallback_resolvers, MutationType
from ariadne.wsgi import GraphQL
# from ariadne.constants import PLAYGROUND_HTML
# from flask import Flask, request, jsonify
from flask import render_template
from backend.models import Invoice
import pdfkit
import os
import uuid
import base64

INVOICE_CONSTANTS = {
    "own_address": os.getenv("INVOICE_OWN_ADDRESS", "Max Mustermann<br />Musterstr. 41<br />12345 Musterhausen<br />Ust-IdNr: 123456"),
    "payment_days": os.getenv("INVOICE_PAYMENT_DAYS", 30),
    "acocunt_owner":  os.getenv("INVOICE_ACCOUNT_OWNER", "Max Mustermann"),
    "acocunt_iban":  os.getenv("INVOICE_ACCOUNT_IBAN", "DE123456789"),
    "acocunt_bic":  os.getenv("INVOICE_ACCOUNT_BIC", "XYZ123")
}
# Define Resolvers
invoice = ObjectType("Invoice")


@invoice.field("_id")
def resolve_invoice_id(obj: Invoice, info):
    return obj.id


@invoice.field("month")
def resolve_invoice_month(obj: Invoice, info):
    return obj.month


@invoice.field("total")
def resolve_invoice_total(obj: Invoice, info):
    return obj.total


@invoice.field("address")
def resolve_invoice_address(obj: Invoice, info):
    return obj.address


@invoice.field("sent")
def resolve_invoice_sent(obj: Invoice, info):
    return obj.sent


@invoice.field("customer")
def resolve_invoice_customer(obj: Invoice, info):
    return obj._customer


@invoice.field("items")
def resolve_invoice_items(obj: Invoice, info):
    return obj.items


@invoice.field("pdf")
def render_invoice_pdf(obj: Invoice, info):
    return html_to_pdf(render_template("invoice.html", invoice=obj))


def html_to_pdf(html):
    filename = "/tmp/{}.pdf".format(uuid.uuid4())
    pdfkit.from_string(html, filename)
    with open(filename, "rb") as pdf:
        b64 = base64.encodebytes(pdf.read()).decode()
    os.remove(filename)
    return b64
