=============================
zyte-spider-templates-project
=============================

This is a starting template for a `Scrapy
<https://docs.scrapy.org/en/latest/>`_ project, with built-in integration with
Zyte technologies (`scrapy-zyte-api
<https://github.com/scrapy-plugins/scrapy-zyte-api>`_, `zyte-crawlers
<https://github.com/zytedata/zyte-crawlers>`_) and recommended best
practices (dependency pinning, static code checking, type hints).

Requirements
============

* Python 3.8+


First steps
===========

After you clone this repository, follow these step to make it yours:

#.  Rename the ``zyte_spider_templates_project`` folder to a valid Python
    module name that you would like to use as your project ID, and update
    ``scrapy.cfg`` and ``<project ID>/settings.py`` (``SCRAPY_POET_DISCOVER``
    and ``SPIDER_MODULES`` settings) accordingly.

#.  For local development, assign your `Zyte API key
    <https://app.zyte.com/o/zyte-api/api-access>`_ to the ``ZYTE_API_KEY``
    environment variable, for example, using `direnv <https://direnv.net/>`_.

    .. note:: `Scrapy Cloud
        <https://docs.zyte.com/scrapy-cloud/get-started.html>`_
        automatically configures your API key through a Scrapy setting.

#.  Remove or replace the ``LICENSE`` and ``README.rst`` files.

#.  Delete ``.git``, and start a fresh Git repository::

        git init
        git add -A
        git commit -m "Initial commit"


Development
===========

-   Use a `virtual environment <https://docs.python.org/3/library/venv.html>`_
    for local development and
    `pip-tools <https://pip-tools.readthedocs.io/en/latest/>`_ for dependency
    management.

-   Run ``pre-commit install`` to enable static code checks before commits.

-   Use spiders from `zyte-crawlers
    <https://github.com/zytedata/zyte-crawlers>`_, for example::

        scrapy crawl ecommerce -a url="https://books.toscrape.com/" -o output.jsonl

-   Subclass spiders from `zyte-crawlers
    <https://github.com/zytedata/zyte-crawlers>`_ or `write spiders
    from scratch <https://docs.scrapy.org/en/latest/topics/spiders.html>`_.

    Define your spiders in Python files and modules within
    ``<project ID>/spiders/``.

-   Use `web-poet <https://web-poet.readthedocs.io/en/stable/>`_ and
    `scrapy-poet <https://scrapy-poet.readthedocs.io/en/stable/>`_ to modify
    the parsing behavior of spiders, in all, some, or specific websites.

    Define your page objects in Python files and modules within
    ``<project ID>/page_objects/``.
