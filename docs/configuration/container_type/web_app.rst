Web Application Settings
========================

To build a Web Application container use the following setting for the top-level ``type`` key:

.. sourcecode:: yaml

    type: jupyter-notebook

Then use the top-level ``web_apps`` key to provide one or more web applications that are run via
`Jupyter Server Proxy <https://jupyter-server-proxy.readthedocs.io/en/latest/>`_:

.. sourcecode:: yaml

    web_apps:
      - path:          # The URL path that the web application is hosted at.
        cmdline:       # The command line used to start the web application.
        port:          # The port the web application is listening on.
        default:       # Whether this web application should be the default to load.
        timeout:       # How long to wait for the web application to start up.
        absolute_url:  # Whether an absolute URL is provided

* ``path``: The URL path that the web application is hosted at. This **cannot** be ``/`` and must also not be a path
  used by anything else such as ``/lab`` or ``/tree``.
* ``cmdline``: The command line to run. This can either be a string, in which case it will be split using
  `shlex.split <https://docs.python.org/3/library/shlex.html>`, or a list. In either case the following to substitution
  variables can be used:

  * ``{port}`` is replaced with the random port the Jupyter proxy has selected for the web application.
  * ``{base_url}`` is replaced with the full path the application is hosted at. This will differ whether the container
    is run directly via Docker or via JupyterHub and this setting handles the distinction.

* ``port`` [optional]: The port the web application listens on. If unspecified, this defaults to 0, which means the
  Jupyter proxy will pick a random port (see above for substitution values for that random port).
* ``default`` [optional]: Whether this web application is the default to run in the container.
* ``timeout`` [optional]: How long to wait for the application to start, before giving up.
* ``absolute_url`` [optional]: Whether to pass an absolute url or a relative url to the ``cmdline`` via the
  ``{base_url}`` substitution.

For multiple web applications simply repeat the configuration block.
