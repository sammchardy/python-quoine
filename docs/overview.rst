Getting Started
===============

Installation
------------

``python-quoine`` is available on `PYPI <https://pypi.python.org/pypi/python-quoine/>`_.
Install with ``pip``:

.. code:: bash

    pip install python-quoine


Register on Quoinex
-------------------

Firstly register an account with `Quoinex <https://accounts.quoinex.com/sign-up?affiliate=PAxghztC67615>`_
or `Qryptos <https://accounts.qryptos.com/sign-up?affiliate=PAxghztC67615>`_.

Generate an API Key
-------------------

To use signed account methods you are required to `create an API Key  <https://accounts.quoinex.com/settings/api-token>`_.

Initialise the client
---------------------

Pass your API Token Id and Secret

Import the client you want to use, the methods available are the same.

.. code:: python

    from quoine.client import Quoinex, Qryptos
    quoinex_client = Quoinex(api_token_id, api_secret)

    qryptos_client = Qryptos(api_token_id, api_secret)

    # optionally pass a language parameter
    # ie en, en-us
    qryptos_client = Qryptos(api_token_id, api_secret, language='zh')

    # optionally pass a vendor id if applicable
    qryptos_client = Qryptos(api_token_id, api_secret, vendor_id='vendor_id')


API Rate Limit
--------------

API users should not make more than 300 requests per 5 minute.

Requests that go beyond the limit will return with a 429 status

Pagination
----------

Some API requesting lists will be paginated with the following format:

.. code:: python

    {
        "models": [ "<json objects>" ],
        "current_page": "<current page>",
        "total_pages": "<number of pages>"
    }

The default number of items returned is 20. To get more, you can specify parameter `limit`. Note that the maximum number of items that can be returned at a time is 1000

To get the next page use the `page` parameter.
