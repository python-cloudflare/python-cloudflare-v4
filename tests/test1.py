#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

import pytest

def test_ips():
    cf = CloudFlare.CloudFlare()
    ips = cf.ips.get()
    assert ips

