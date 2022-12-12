# _*_ coding:utf-8 _*_
# @Time : 2022/12/12 16:02 
# @Author : zhut96
# @File : setup.py 
# @Software: PyCharm

from setuptools import setup, find_packages
import os
import platform
import logging
import codecs

"""
setup module for core.
Created on 12/12/2012
@author: zhut96
"""
PACKAGE = "aio-alipay"
NAME = "aio-alipay-sdk-python"
DESCRIPTION = "The official Aliyun SDK for Python."
AUTHOR = "zhut96"
AUTHOR_EMAIL = "zhut96@outlook.com"
URL = "https://github.com/Pig-Tong/aio-alipay-sdk-python"

TOPDIR = os.path.dirname(__file__) or "."
VERSION = __import__(PACKAGE).__version__

desc_file = codecs.open("README.rst", 'r', 'utf-8')
try:
    LONG_DESCRIPTION = desc_file.read()
finally:
    desc_file.close()

requires = ["aiohttp", "alipay-sdk-python"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache",
    url=URL,
    keywords=["alipay", "sdk", "aio"],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    platforms='any',
    install_requires=requires,
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
    )
)
