# -*- coding: utf-8 -*-
"""This package is meant to run against a PyVISA builbot.

The PyVISA builbot is connected to a fake instrument implemented using the
Keysight Virtual Instrument IO Test software.

For this part of the testsuite to be run, you need to set the
PYVISA_KEYSIGHT_VIRTUAL_INSTR environment value.

To enable coverage for the shell, one needs to add/edit sitecustomize.py in
site-packages and add the following::

import coverage
coverage.process_startup()

See https://coverage.readthedocs.io/en/v4.5.x/subprocess.html for details.

"""
import os
import unittest

require_virtual_instr = unittest.skipUnless(
    "PYVISA_KEYSIGHT_VIRTUAL_INSTR" in os.environ,
    "Requires the Keysight virtual instrument. Run on PyVISA " "buildbot.",
)


RESOURCE_ADDRESSES = {
    # "GPIB::INSTR": "GPIB::19::INSTR",
    # "USB::INSTR": "USB::",
    "TCPIP::INSTR": "TCPIP::127.0.0.1::INSTR",  # ie localhost
    "TCPIP::SOCKET": "TCPIP::127.0.0.1::5025::SOCKET",
}

ALIASES = {
    "TCPIP::127.0.0.1::INSTR": "tcpip",
}
