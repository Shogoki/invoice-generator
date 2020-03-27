from backend.resolvers.query import query
from backend.resolvers.customer import customer
from backend.resolvers.mutation import mutation
from backend.resolvers.invoice import invoice
from backend.resolvers.invoice_item import invoice_item

resolvers = [query, mutation, customer, invoice, invoice_item]
