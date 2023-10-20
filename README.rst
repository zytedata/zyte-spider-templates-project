=====================
zyte-crawlers-project
=====================

This is a Scrapy project that uses spiders defined in `zyte-spider-templates`_.

.. _zyte-spider-templates: https://github.com/zytedata/zyte-spider-templates

Requirements
============

* Python 3.8+
* Scrapy 2.11+
* zyte-spider-templates

You also need a `Zyte API`_ subscription.

.. _Zyte API: https://docs.zyte.com/zyte-api/get-started.html

Usage
=====

.. note:: As some modifications to the files in this repo are needed before it
   can be used, it's recommended to fork it.

This is an already created and configured Scrapy project so when you follow
guides like the `Scrapy Cloud tutorial
<https://docs.zyte.com/web-scraping/tutorial/cloud.html>`_ you should skip
most of the parts that talk about creating and configuring it. Still, you need
some additional configuration specific to your account. Here is a short guide
for using this project on Scrapy Cloud.

1. Create a Scrapy Cloud project on the Zyte dashboard if you don't have it
   yet.
2. Make sure you have a Zyte API subscription. For Scrapy Cloud runs the API
   key will be used automatically, for local runs you need to set a setting or
   an environment variable, as described in `scrapy-zyte-api docs
   <https://github.com/scrapy-plugins/scrapy-zyte-api#quick-start>`_.
3. Run ``shub login`` and enter your `Scrapy Cloud API key
   <https://app.zyte.com/o/settings/apikey>`_.
4. Deploy your project with ``shub deploy 000000``, replacing ``000000`` with
   your Scrapy Cloud project ID (found in the project dashboard URL).
   Alternatively, put the project ID into the ``scrapinghub.yml`` file to be
   able to run simply ``shub deploy``.
5. Now you should be able to create smart spiders on your Scrapy Cloud project
   using the templates from this project.

For more information and more verbose descriptions of specific steps you can
check:

* `The Scrapy Cloud tutorial
  <https://docs.zyte.com/web-scraping/tutorial/cloud.html>`_.
* `The shub documentation <https://shub.readthedocs.io/>`_.
* `The Zyte API documentation
  <https://docs.zyte.com/zyte-api/get-started.html>`_.
* `The zyte-spider-templates documentation
  <https://github.com/zytedata/zyte-spider-templates>`_.

Customization
=============

By default all spiders and page objects defined in ``zyte-spider-templates``
are available in this project (because the ``SPIDER_MODULES`` setting value
includes ``"zyte_spider_templates.spiders"`` and the ``SCRAPY_POET_DISCOVER``
setting value includes ``"zyte_spider_templates.page_objects"``). You can
also add your own spiders (to the ``zyte_crawlers_project.spiders`` package)
and page objects (to the ``zyte_crawlers_project.page_objects`` package) and
subclass the ``zyte-spider-templates`` ones.
