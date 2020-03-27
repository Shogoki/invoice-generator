from ariadne.wsgi import GraphQL
from ariadne import gql, load_schema_from_path, QueryType, ObjectType, fallback_resolvers, MutationType
from backend import db
from backend.models import Customer, Invoice, InvoiceItem
from datetime import datetime

"""


  
  
  
  

  deleteCustomerById(customerId: ID!): Customer!

  updateCustomer(customerId: ID!, firstname: String, lastname: String, street: String, zip: String, city: String, email: String, defaultPrice: Float): Customer!
  """

mutation = MutationType()


@mutation.field("createCustomer")
def create_customer(_, info, firstname: str, lastname: str, street: str, zip: str, city: str, email: str, company: str = "", defaultPrice: float = 80.00):
    customer = Customer(firstname, lastname, street,
                        zip, city, email, defaultPrice, company)
    db.session.add(customer)
    db.session.commit()
    return customer


@mutation.field("createInvoice")
def create_invoice(_, info, customerId: int, date: str = None, month: int = None):
    if month is None:
        month = datetime.now().month - 1
        month = 12 if month == 0 else month
    if date is None:
        date = datetime.now().strftime("%d.%m.%Y")
    invoice = Invoice(customerId, month, date)
    db.session.add(invoice)
    db.session.commit()
    return invoice


@mutation.field("deleteInvoice")
def delete_invoice(_, info, invoiceId: int):
    Invoice.query.filter(Invoice._id == invoiceId).delete()
    db.session.commit()
    return True


@mutation.field("sendInvoice")
def send_invoice(_, info, invoiceId: int):
    # TODO: Implement call to send mail API
    return Invoice.query.filter(Invoice._id == invoiceId).first()


@mutation.field("addInvoiceItem")
def add_invoice_item(invoiceId: int, description: str, price: float = None, amount: int = 1):

    invoice = Invoice.query.filter(Invoice._id == invoiceId).first()
    if price is None:
        price = invoice.customer.default_price
    item = InvoiceItem(description, amount, price)
    invoice._items.append(item)
    db.session.commit()
    return item


@mutation.field("removeInvoiceItem")
def remvove_invoice_item(_, info, invoiceId: int, itemPos: int):
    InvoiceItem.query.filter(InvoiceItem._invoice_id ==
                             invoiceId, InvoiceItem.pos == itemPos).delete()
    db.session().commit()
    return True


@mutation.field("removeCustomer")
def remove_customer(_, info, customerId: int):
    Customer.query.filter(Customer._id == customerId).delete()
    db.session.commit()
    return True


@mutation.field("updateCustomer")
def update_customer(_, info, customerId: int, firstname: str = None, lastname: str = None, street: str = None, zip: str = None, city: str = None, email: str = None, defaultPrice: float = None, company: str = None):
    customer = Customer.query.filter(Customer._id == customerId).first()
    if firstname is not None:
        customer.firstname = firstname
    if lastname is not None:
        customer.lastname = lastname
    if street is not None:
        customer.street = street
    if zip is not None:
        customer.zip = zip
    if city is not None:
        customer.city = city
    if email is not None:
        customer.email = email
    if defaultPrice is not None:
        customer.default_price = defaultPrice
    if company is not None:
        customer.company = company
    db.session.commit()
    return customer
