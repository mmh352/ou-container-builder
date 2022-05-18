Environment Variables
=====================

The environment variables are used to set environment variables in the container, which are available both at build-
and at run-time:

.. sourcecode:: yaml

    environment:
      - name:   # The name of the environment variable.
        value:  # The value of the environment variable. This will be quoted when output in the container build file.

* ``environment``: List of environment variables to output into the container build file. Each environment variable
  consists of a ``name`` and a ``value`` as separate keys in the config file.
