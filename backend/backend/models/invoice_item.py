# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend import util
from backend import db


class InvoiceItem(Model, db.Model):
    __tablename__ = "invoice_items"
    _pos = db.Column(db.Integer, primary_key=True)
    _description = db.Column(db.String(100))
    _amount = db.Column(db.Float)
    _price = db.Column(db.Float)
    _invoice_id = db.Column(db.Integer, db.ForeignKey(
        "invoices._id"), primary_key=True)
    _invoice = db.relationship("Invoice", back_populates="_items")

    def __init__(self,  description=None, amount=None, price=None, pos=None):  # noqa: E501
        """InvoiceItem - a model defined in OpenAPI

        :param pos: The pos of this InvoiceItem.  # noqa: E501
        :type pos: int
        :param description: The description of this InvoiceItem.  # noqa: E501
        :type description: str
        :param amount: The amount of this InvoiceItem.  # noqa: E501
        :type amount: int
        :param price: The price of this InvoiceItem.  # noqa: E501
        :type price: float
        """
        self.openapi_types = {
            'pos': int,
            'description': str,
            'amount': float,
            'price': float
        }

        self.attribute_map = {
            'pos': 'pos',
            'description': 'description',
            'amount': 'amount',
            'price': 'price'
        }

        self._description = description
        self._amount = amount
        self._price = price
        self._pos = pos

    @classmethod
    def from_dict(cls, dikt) -> 'InvoiceItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvoiceItem of this InvoiceItem.  # noqa: E501
        :rtype: InvoiceItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pos(self):
        """Gets the pos of this InvoiceItem.


        :return: The pos of this InvoiceItem.
        :rtype: int
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Sets the pos of this InvoiceItem.


        :param pos: The pos of this InvoiceItem.
        :type pos: int
        """
        if pos is None:
            raise ValueError("Invalid value for `pos`, must not be `None`")  # noqa: E501

        self._pos = pos

    @property
    def description(self):
        """Gets the description of this InvoiceItem.


        :return: The description of this InvoiceItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvoiceItem.


        :param description: The description of this InvoiceItem.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def amount(self):
        """Gets the amount of this InvoiceItem.


        :return: The amount of this InvoiceItem.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceItem.


        :param amount: The amount of this InvoiceItem.
        :type amount: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this InvoiceItem.


        :return: The price of this InvoiceItem.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this InvoiceItem.


        :param price: The price of this InvoiceItem.
        :type price: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price
