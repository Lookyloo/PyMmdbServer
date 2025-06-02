.. PyLookyloo documentation master file, created by
   sphinx-quickstart on Tue Mar 23 12:28:17 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyMmdbServer's documentation!
=============================================

This is the client API for `MMDB Server <https://github.com/adulau/mmdb-server>`_

Installation
------------

The package is available on PyPi, so you can install it with::

  pip install pymmdbserver


Usage
-----

You can use `mmdbserver` as a python script::

	$ mmdbserver -h
    usage: mmdbserver [-h] [--url URL] [ip]

    Query a thing.

    positional arguments:
      ip          IP address to query. If not set, returns the geolookup information from the client IP.

    options:
      -h, --help  show this help message and exit
      --url URL   URL of the instance.

Or as a library:

.. toctree::
   :glob:

   api_reference


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
