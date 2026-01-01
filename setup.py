#!/usr/bin/env python3
"""
Setup script for GaziSiber Fetch
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gazisiber-fetch",
    version="1.0.0",
    author="GaziSiber",
    description="A system information display tool for Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbdullahZeynel/gazisiber-fetch",
    py_modules=["gazisiber_fetch"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gazisiber=gazisiber_fetch:main",
        ],
    },
    license="GPL-3.0",
)
