#!/usr/bin/env python

import unittest
import os
import sys
import subprocess

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def test_Rrp6.1(self):
        """Test model building of exo10+Rrp6 complex (first calculation)"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.1'))
        self.run_modeling_script()

    def test_Rrp6.2(self):
        """Test model building of exo10+Rrp6 complex (second calculation)"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.2'))
        self.run_modeling_script()

    def test_Ski7.1(self):
        """Test model building of exo10+Ski7 complex (first calculation)"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Ski7.1'))
        self.run_modeling_script()

    def test_Ski7.2(self):
        """Test model building of exo10+Ski7 complex (second calculation)"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Ski7.2'))
        self.run_modeling_script()

    def run_modeling_script(self)
        """Run IMP modeling"""
        p = subprocess.check_call(["python", 'exosome.modeling.py', "--test"])
        # todo: run analysis, assert outputs

if __name__ == '__main__':
    unittest.main()
