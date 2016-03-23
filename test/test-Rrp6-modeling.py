#!/usr/bin/env python

import unittest
import os
import sys
import utils

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(utils.TestBase):
    def test_Rrp6(self):
        """Test model building and analysis of exo10+Rrp6 complex"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.1'))
        self.run_modeling_script()
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.2'))
        self.run_modeling_script()
        os.chdir(os.path.join(TOPDIR, 'Rrp6.analysis'))
        self.run_analysis_script()

if __name__ == '__main__':
    unittest.main()
