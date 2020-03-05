#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Test for sample tdd module.

* Author: YAMAGAMI Satoshi
"""
# noinspection PyProtectedMember
from sample_tdd import __all__
from sample_tdd import __version__


def test_version():
    """Testing __version__ the special variable."""
    assert __version__ == "0.1.0"


def test_all():
    """Testing __all__ the special variable."""
    assert __all__ == ["__version__", "hello_world"]
