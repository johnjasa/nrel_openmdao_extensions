"""
Author: John Jasa <jjasa@nrel.gov>

This package is distributed under Apache 2 license.
"""

from setuptools import setup

from os import path
from io import open

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: Unix
Operating System :: MacOS
"""

metadata = dict(
    name="nrel_openmdao_extensions",
    version="0.0.1",
    description="Additional drivers for OpenMDAO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="John Jasa",
    author_email="jjasa@nrel.gov",
    license="Apache License, Version 2.0",
    classifiers=[_f for _f in CLASSIFIERS.split("\n") if _f],
    packages=["nrel_openmdao_extensions"],
    install_requires=["openmdao"],
    python_requires=">=3.6",
    zip_safe=True,
    keywords="openmdao openmdao_driver",
    entry_points={
        "openmdao_driver": [
            "nlopt_driver = nrel_openmdao_extensions.nrel_openmdao_extensions.nlopt_driver:NLoptDriver",
        ],
    },
)

setup(**metadata)
