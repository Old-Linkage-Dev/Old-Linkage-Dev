#!/usr/bin/env python
#-*- coding:utf-8 -*-

import setuptools



_name = "Old-Linkage-Dev";
_version = "0.0.4";
_keywords = ["telnet", "CLI", "website"];
_description = "a module to develop and apply old-style links";
_url = "https://github.com/Tarcadia/Old-Linkage-Dev";
_bturl = "https://github.com/Tarcadia/Old-Linkage-Dev/issues";
_lic = "GNU-v3";

_author = "Tarcadia";
_author_email = "tarcadia@qq.com";



with open("README.md", "r", encoding="utf-8") as fh:
    _ldescription = fh.read();

setuptools.setup(
    name                            = _name,
    version                         = _version,
    author                          = _author,
    author_email                    = _author_email,
    keywords                        = _keywords,
    description                     = _description,
    long_description                = _ldescription,

    long_description_content_type   = "text/markdown",
    url                             = _url,
    project_urls                    = {
        "Bug Tracker"               : _bturl,
    },
    classifiers                     = [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir                     = {
        ""                          : "src"
    },
    packages                        = setuptools.find_packages(where="src"),
    python_requires                 = ">=3.7",
);