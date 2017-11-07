Order Endpoints
===============


`Fetch all orders <quoine.html#quoine.client.Quoinex.get_orders>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    orders = client.get_orders(product_id=1, limit=10)

`Fetch an order <quoine.html#quoine.client.Quoinex.get_order>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    order = client.get_order(order_id=2157479)


`Place an order <quoine.html#quoine.client.Quoinex.create_order>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Place an order**

Use the `create_order` function to have full control over creating an order
.. code:: python

    order = client.create_order(
        type=Quoinex.ORDER_TYPE_LIMIT
        product_id=1,
        side=Quoinex.SIDE_BUY,
        quantity='100',
        price='0.00001')

**Place a limit order**

Use the helper functions to easily place a limit buy or sell order

.. code:: python

    order = client.create_limit_buy(
        product_id=1,
        quantity='100',
        price='0.00001')

    order = client.create_limit_sell(
        product_id=1,
        quantity='100',
        price='0.00001')


**Place a market order**

Use the helper functions to easily place a market buy or sell order

.. code:: python

    order = client.create_market_buy(
        product_id=1,
        quantity='100')

    order = client.create_market_sell(
        product_id=1,
        quantity='100')

    # place a market buy with range for slippage
    order = client.create_market_buy(
        product_id=1,
        quantity='100',
        price_range='0.001')

`Edit a live order <quoine.html#quoine.client.Client.update_live_order>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    order = client.update_live_order(
        order_id=2157479,
        quantity='101',
        price='0.001')


`Cancel an order <quoine.html#quoine.client.Quoinex.cancel_order>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    result = client.cancel_order(order_id=2157479)


`Get an orders trades <quoine.html#quoine.client.Quoinex.get_order_trades>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    trades = client.get_order_trades(order_id=2157479)
