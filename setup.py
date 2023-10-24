# A basic setup.py needed for shub deploy to work

from setuptools import setup, find_packages

setup(
    name='zyte-spider-templates-project',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'scrapy': ['settings = zyte_spider_templates_project.settings'],
    },
)
