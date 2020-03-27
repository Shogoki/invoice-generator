from ariadne.wsgi import GraphQL
from ariadne import gql, load_schema_from_path, QueryType, ObjectType, fallback_resolvers, MutationType

from backend.models import Customer, Invoice, InvoiceItem

# Define Resolvers
query = QueryType()

"""
listInvoices(limit: Int = 100): [Invoice]

  # Info for a specific invoice
  # @param ID! invoiceId The id of the invoice to retrieve
  # @return [Invoice]
  getInvoice(invoiceId: ID!): Invoice

  # List all customers
  # @param Int! limit How many items to return at one time (default 100)
  # @return [[Customer]]
  listCustomers(limit: Int = 100): [Customer]

  # Info for a specific customer
  # @param Float! customerId The id of the customer to retrieve
  # @return [Customer]
  getCustomer(customerId: ID!): Customer
  """


@query.field("listInvoices")
def list_invoices(_, info, limit: int = 100):
    return Invoice.query.limit(limit).all()


@query.field("getInvoice")
def get_invoice(_, info, invoiceId: int):
    return Invoice.query.filter(Invoice._id == invoiceId).first()


@query.field("listCustomers")
def list_customers(_, info, limit: int = 100):
    return Customer.query.limit(limit).all()


@query.field("getCustomer")
def get_customer(_, info, customerId: int):
    return Customer.query.filter(Customer._id == customerId).first()
