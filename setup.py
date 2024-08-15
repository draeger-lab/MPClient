# coding: utf-8

"""
    Model Polisher API

    API for the Model Polisher.  # noqa: E501

    OpenAPI spec version: 2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "model-polisher"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "python-libsbml >= 5.20.4"]

setup(
    name=NAME,
    version=VERSION,
    description="Model Polisher API",
    author_email="",
    url="https://github.com/draeger-lab/MPClient",
    keywords=["Swagger", "Model Polisher API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API for the Model Polisher.  # noqa: E501
    """
)
