Executions Endpoints
====================

`Get Executions <quoine.html#quoine.client.Quoine.get_executions>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    executions = client.get_executions(
        product_id=1,
        limit=200)


`Get Executions by Timestamp <quoine.html#quoine.client.Quoine.get_executions_since_time>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note this call has an optional limit parameter but no paging.

.. code:: python

    import time

    since = int(time.time())
    executions = client.get_executions_since_time(
        product_id=1,
        timestamp=since,
        limit=50)


`Get My Executions <quoine.html#quoine.client.Quoine.get_my_executions>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    executions = client.get_my_executions(product_id=1)
