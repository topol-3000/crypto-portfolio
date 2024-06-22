==========================
Crypto Portfolio
==========================

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/badge/python-3.10%2B-blue.svg
    :target: https://www.python.org/downloads/release/python-3100/

A web-based REST API that enables users to track their crypto portfolios and receive ROI reports via email, enhancing their investment decision-making process.


Getting Started
===============

Preparations
-------

Copy ``.env.dist`` file, rename it to ``.env.dev`` and fill it with your data.



Install
-------

Build and start application in development mode::

    make install



Run earlier installed application
----------

To run the Django development server and database::

    make up

Make Migrations
---------------

Create new migrations based on the changes detected in your models::

    make make-migrations

Migrate
-------

Apply the migrations and update the database schema::

    make migrate

Contact
=======

Yevhenii Diemientiev - yevhenii.diemientiev.pe@gmail.com
