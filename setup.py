# A basic setup.py needed for shub deploy to work

from setuptools import setup, find_packages

setup(
    name='zyte-crawlers-project',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'scrapy': ['settings = zyte_crawlers_project.settings'],
    },
)
