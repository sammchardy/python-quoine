#!/usr/bin/env python
# coding=utf-8

from quoine.client import Quoinex
from quoine.exceptions import QuoineAPIException, QuoineRequestException
import pytest
import requests_mock


client = Quoinex('api_key', 'api_secret')


def test_invalid_json():
    """Test Invalid response Exception"""

    with pytest.raises(QuoineRequestException):
        with requests_mock.mock() as m:
            m.get('https://api.quoine.com/products', text='<head></html>')
            client.get_products()


def test_api_exception():
    """Test API response Exception"""

    with pytest.raises(QuoineAPIException):
        with requests_mock.mock() as m:
            json_obj = {"errors": {"user": ["not_enough_free_balance"]}}
            m.get('https://api.quoine.com/products/1/price_levels', json=json_obj, status_code=400)
            client.get_order_book(product_id=1)
