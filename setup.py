#!/usr/bin/python
# coding: utf-8
#
# Copyright (C) 2009  Manuel Hermann <manuel-hermann@gmx.net>
from setuptools import setup

DESCRIPTION = "An easy-to-use HTTP and WebDAV client library."
LONG_DESCRIPTION = """\
An easy-to-use HTML and WebDAV client library for Python
--------------------------------------------------------

This is a small library for contacting HTTP and WebDAV servers. Goal of this
 project until version 1.0 is supporting all WebDAV methods including the
 versioning extensions from RFC 3253).

Features:
 - HTTP methods OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT.
 - WebDAV methods MKCOL, PROPFIND, PROPPATCH, DELETE, COPY, MOVE, LOCK, UNLOCK
 - Support for REPORT method (verion-tree and expand-property, RFC 3253)
 - Cookies
 - SSL
 - Multipart/form-data and application/x-www-form-urlencoded POST requests

This version requires Python 2.5 or later (including Python 3.)
"""

CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: "\
        "GNU Library or Lesser General Public License (LGPL)",
    "Operating System :: OS Independent",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

if __name__ == "__main__":
    setup(
        name="tinydav-fork",
        packages=["tinydav"],
        version='0.3.2.dev0',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author="Manuel Hermann",
        author_email="manuel-hermann@gmx.net",
        url="https://gitlab.helduel.de/open-source/tinydav",
        keywords=["webdav", "https", "http", "library", "client", "lgpl",
                  "rfc2518", "rfc2068", "rfc3253"],
        license="LGPL",
        classifiers=CLASSIFIERS,
    )
