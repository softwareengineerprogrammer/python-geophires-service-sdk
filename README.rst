========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |version| image:: https://img.shields.io/pypi/v/geophires-service-sdk.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/geophires-service-sdk

.. |wheel| image:: https://img.shields.io/pypi/wheel/geophires-service-sdk.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/geophires-service-sdk

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/geophires-service-sdk.svg
    :alt: Supported versions
    :target: https://pypi.org/project/geophires-service-sdk

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/geophires-service-sdk.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/geophires-service-sdk

.. |commits-since| image:: https://img.shields.io/github/commits-since/softwareengineerprogrammer/python-geophires-service-sdk/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/softwareengineerprogrammer/python-geophires-service-sdk/compare/v0.0.0...main



.. end-badges

GEOPHIRES service SDK

* Free software: MIT license

Installation
============

::

    pip install geophires-service-sdk

You can also install the in-development version with::

    pip install https://github.com/softwareengineerprogrammer/python-geophires-service-sdk/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import geophires_service_sdk
    geophires_service_sdk.longest()


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
