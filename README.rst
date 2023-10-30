=============================
zyte-spider-templates-project
=============================

This is a starting template for a `Scrapy
<https://docs.scrapy.org/en/latest/>`_ project, with built-in integration with
Zyte technologies (`scrapy-zyte-api
<https://github.com/scrapy-plugins/scrapy-zyte-api>`_,
`zyte-spider-templates`_).


Requirements
============

* Python 3.8+
* Scrapy 2.11+
* zyte-spider-templates

You also need a `Zyte API`_ subscription for Zyte API features, including AI-powered spiders.

.. _Zyte API: https://docs.zyte.com/zyte-api/get-started.html


First steps
===========

After you clone this repository, follow these step to make it yours:

#.  Rename the ``zyte_spider_templates_project`` folder to a valid Python
    module name that you would like to use as your project ID, and update
    ``scrapy.cfg`` and ``<project ID>/settings.py`` (``BOT_NAME``,
    ``SPIDER_MODULES``, ``NEWSPIDER_MODULE`` and ``SCRAPY_POET_DISCOVER``
    settings) accordingly.

#.  For local development, assign your `Zyte API key
    <https://app.zyte.com/o/zyte-api/api-access>`_ to the ``ZYTE_API_KEY``
    environment variable, for example, using `direnv <https://direnv.net/>`_.

    .. note:: `Scrapy Cloud
        <https://docs.zyte.com/scrapy-cloud/get-started.html>`_
        automatically provides Zyte API key for the jobs, if you have a
        subscription.

#.  Remove or replace the ``LICENSE`` and ``README.rst`` files.

#.  Delete ``.git``, and start a fresh Git repository::

        git init
        git add -A
        git commit -m "Initial commit"


Usage
=====

This is an already created and configured Scrapy project so when you follow
guides like the `Scrapy Cloud tutorial
<https://docs.zyte.com/web-scraping/tutorial/cloud.html>`_ you should skip
most of the parts that talk about creating and configuring it. Still, you need
some additional configuration specific to your account. Here is a short guide
for using this project on Scrapy Cloud.

#.  Create a Scrapy Cloud project on the Zyte dashboard if you don't have it
    yet.
#.  Make sure you have a Zyte API subscription. For Scrapy Cloud runs the API
    key will be used automatically, for local runs you need to set a setting or
    an environment variable, as described in the first steps above.
#.  Run ``shub login`` and enter your `Scrapy Cloud API key
    <https://app.zyte.com/o/settings/apikey>`_.
#.  Deploy your project with ``shub deploy 000000``, replacing ``000000`` with
    your Scrapy Cloud project ID (found in the project dashboard URL).
    Alternatively, put the project ID into the ``scrapinghub.yml`` file to be
    able to run simply ``shub deploy``.
#.  Now you should be able to `create smart spiders
    <https://docs.zyte.com/web-scraping/guides/no-code/index.html#create-a-spider>`_
    on your Scrapy Cloud project using the templates from this project.

For more information and more verbose descriptions of specific steps you can
check:

* `The Scrapy documentation <https://docs.scrapy.org>`_.
* `The Scrapy Cloud tutorial
  <https://docs.zyte.com/web-scraping/tutorial/cloud.html>`_.
* `The shub documentation <https://shub.readthedocs.io/>`_.
* `The Zyte API documentation
  <https://docs.zyte.com/zyte-api/get-started.html>`_.
* `The zyte-spider-templates documentation
  <https://github.com/zytedata/zyte-spider-templates>`_.

You can also run the spiders locally, for example::

        scrapy crawl ecommerce -a url="https://books.toscrape.com/" -o output.jsonl


Development
===========

By default all spiders and page objects defined in `zyte-spider-templates`_ are
available in this project. You can also:

-   Subclass spiders from `zyte-spider-templates`_ or `write spiders
    from scratch <https://docs.scrapy.org/en/latest/topics/spiders.html>`_.

    Define your spiders in Python files and modules within
    ``<project ID>/spiders/``.

-   Use `web-poet <https://web-poet.readthedocs.io/en/stable/>`_ and
    `scrapy-poet <https://scrapy-poet.readthedocs.io/en/stable/>`_ to modify
    the parsing behavior of spiders, in all, some, or specific websites.

    Define your page objects in Python files and modules within
    ``<project ID>/page_objects/``.

.. _zyte-spider-templates: https://github.com/zytedata/zyte-spider-templates
