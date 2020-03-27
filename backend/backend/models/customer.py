# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from backend.models.base_model_ import Model
from backend import util
from backend import db
from backend.models import Invoice


class Customer(Model, db.Model):
    __tablename__ = "customers"
    _id = db.Column(db.Integer, primary_key=True)
    _firstname = db.Column(db.String(100))
    _lastname = db.Column(db.String(100))
    _street = db.Column(db.String(100))
    _zip = db.Column(db.String(20))
    _city = db.Column(db.String(100))
    _email = db.Column(db.String(100))
    _company = db.Column(db.String(100))
    _invoices = db.relationship("Invoice", back_populates="_customer")
    _default_price = db.Column(db.Float)

    def __init__(self, firstname=None, lastname=None, street=None, zip=None, city=None, email=None, default_price=80.0, company=""):  # noqa: E501
        """Customer - a model defined in OpenAPI

        :param id: The id of this Customer.  # noqa: E501
        :type id: int
        :param firstname: The firstname of this Customer.  # noqa: E501
        :type firstname: str
        :param lastname: The lastname of this Customer.  # noqa: E501
        :type lastname: str
        :param street: The street of this Customer.  # noqa: E501
        :type street: str
        :param zip: The zip of this Customer.  # noqa: E501
        :type zip: str
        :param city: The city of this Customer.  # noqa: E501
        :type city: str
        :param email: The email of this Customer.  # noqa: E501
        :type email: str
        """
        self.openapi_types = {
            'id': int,
            'firstname': str,
            'lastname': str,
            'street': str,
            'zip': str,
            'city': str,
            'email': str,
            'defaultPrice': float
        }

        self.attribute_map = {
            'id': '_id',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'street': 'street',
            'zip': 'zip',
            'city': 'city',
            'email': 'email',
            'defaultPrice': 'default_price'
        }

        self._firstname = firstname
        self._lastname = lastname
        self._street = street
        self._zip = zip
        self._city = city
        self._email = email
        self._default_price = default_price
        self._company = company

    @classmethod
    def from_dict(cls, dikt) -> 'Customer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Customer of this Customer.  # noqa: E501
        :rtype: Customer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Customer.


        :param id: The id of this Customer.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def defaultPrice(self):
        """Gets the default_price of this Customer.


        :return: The default price of this Customer.
        :rtype: float
        """
        return self._default_price

    @id.setter
    def defaultPrice(self, default_price):
        """Sets the id of this Customer.


        :param default_price: The id of this Customer.
        :type default_price: float
        """
        if id is None:
            raise ValueError("Invalid value for `default Price`, must not be `None`")  # noqa: E501

        self._default_price = default_price

    @property
    def firstname(self):
        """Gets the firstname of this Customer.


        :return: The firstname of this Customer.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Customer.


        :param firstname: The firstname of this Customer.
        :type firstname: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def company(self):
        """Gets the firstname of this Customer.


        :return: The firstname of this Customer.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the firstname of this Customer.


        :param firstname: The firstname of this Customer.
        :ty
        pe firstname: str
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def lastname(self):
        """Gets the lastname of this Customer.


        :return: The lastname of this Customer.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this Customer.


        :param lastname: The lastname of this Customer.
        :type lastname: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501

        self._lastname = lastname

    @property
    def street(self):
        """Gets the street of this Customer.


        :return: The street of this Customer.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this Customer.


        :param street: The street of this Customer.
        :type street: str
        """
        if street is None:
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def zip(self):
        """Gets the zip of this Customer.


        :return: The zip of this Customer.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Customer.


        :param zip: The zip of this Customer.
        :type zip: str
        """
        if zip is None:
            raise ValueError("Invalid value for `zip`, must not be `None`")  # noqa: E501

        self._zip = zip

    @property
    def city(self):
        """Gets the city of this Customer.


        :return: The city of this Customer.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Customer.


        :param city: The city of this Customer.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def email(self):
        """Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.


        :param email: The email of this Customer.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email
