Constants
=========

Quoine defines constants for Order Types, Order Side and Order Status. These are accessible from the Quoinex or Qryptos classes.

.. code:: python


    SIDE_BUY = 'buy'
    SIDE_SELL = 'sell'

    STATUS_FILLED = 'filled'
    STATUS_LIVE = 'live'
    STATUS_PARTIAL = 'partially_filled'
    STATUS_CANCELLED = 'cancelled'

    ORDER_TYPE_LIMIT = 'limit'
    ORDER_TYPE_MARKET = 'market'
    ORDER_TYPE_MARKET_RANGE = 'market_with_range'


To use in your code import the contents of the `enums.py` module

.. code:: python

    from quoine.client import Quoinex

    order_type = Quoinex.ORDER_TYPE_LIMIT
    order_side = Quoinex.SIDE_BUY
