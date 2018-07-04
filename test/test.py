#!/usr/bin/env python

import unittest
import os
import sys
import utils
import subprocess

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(utils.TestBase):
    def test_mmcif(self):
        """Test generation of mmCIF output"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.1'))
        if os.path.exists("exosome.cif"):
            os.unlink("exosome.cif")
        p = subprocess.check_call(
                ["python", "exosome.modeling.py", "--mmcif", "--dry-run"])
        # Check size of output file
        with open("exosome.cif") as fh:
            wcl = len(fh.readlines())
        self.assertTrue(wcl >= 66180)

if __name__ == '__main__':
    unittest.main()
