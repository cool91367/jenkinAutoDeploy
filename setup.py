# -*- coding: utf-8 -*-
import os
import sys

from pyreleaseplugin import CleanCommand, ReleaseCommand, SnapshotCommand
from setuptools import find_packages, setup, Command


def read(fname):
    """Utility function to read the README file into the long_description."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


version_file = "pyreleaseplugin/_version.py"
with open(version_file) as fp:
    exec(fp.read())

setup(
    name="eyesmedia-corpus-service",
    version=__version__,
    author="kari",
    author_email="kari.lin@eyesmedia.com.tw",
    description="eyesmedia-corpus-service",
    license="Copyright eyesmedia",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    # package_data={
    #     "chat.source": ['*.json']
    # },
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6.3',
    ],
    cmdclass={"snapshot": SnapshotCommand, "release": ReleaseCommand, "clean": CleanCommand}
)
