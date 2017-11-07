Exceptions
==========

QuoineResponseException
-----------------------

Raised if a non JSON response is returned

QuoineAPIException
------------------

On an API call error a quoine.exceptions.QuoineAPIException will be raised.

The exception provides access to the

- `status_code` - response status code
- `response` - response object
- `messages` - Quoine error message dictionary
- `request` - request object if available

.. code:: python

    try:
        client.get_products()
    except QuoineAPIException as e:
        print(e.status_code)
        print(e.messages)
