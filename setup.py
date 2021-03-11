# _*_ encoding: utf-8 _*_

from setuptools import setup

NAME = 'gpsweekconverter'
VERSION = '0.1.0'
AUTHOR = 'Fernando Ferreira'
AUTHOR_EMAIL = 'fernando.ferreira.tbe@gmail.com'
DESCRIPTION = 'GPSWeek converter'
LONG_DESCRIPTION = 'Simple library create to help gsp week conversion.'
LICENSE = 'MIT'
URL = 'https://github.com/fernandoferreiratbe/gpsweek-converter.git'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    license=LICENSE,
    package=[
        'gpsweekconverter',
        'gpsweekconverter.test'
    ],
    install_requires=[
        'wheel' >= '0.32.0',
        'astropy' >= '4.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
