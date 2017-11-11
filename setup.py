#!/usr/bin/env python
from setuptools import setup

setup(
    name='python-quoine',
    version='0.1.1',
    packages=['quoine'],
    description='Quoinex and Qryptos REST API python implementation',
    url='https://github.com/sammchardy/python-quoine',
    author='Sam McHardy',
    license='MIT',
    author_email='',
    install_requires=['requests', 'six', 'Twisted', 'pyOpenSSL', 'autobahn', 'service-identity'],
    keywords='quoine quoinex qryptos exchange rest api bitcoin ethereum btc eth neo usd jpy',
    classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
