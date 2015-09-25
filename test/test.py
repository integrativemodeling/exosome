#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import shutil

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def test_Rrp6(self):
        """Test model building and analysis of exo10+Rrp6 complex"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.1'))
        self.run_modeling_script()
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.2'))
        self.run_modeling_script()
        os.chdir(os.path.join(TOPDIR, 'Rrp6.analysis'))
        self.run_analysis_script()

    def test_Ski7(self):
        """Test model building and analysis of exo10+Ski7 complex"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Ski7.1'))
        self.run_modeling_script()
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Ski7.2'))
        self.run_modeling_script()
        os.chdir(os.path.join(TOPDIR, 'Ski7.analysis'))
        self.run_analysis_script()

    def run_modeling_script(self):
        """Run IMP modeling"""
        # clean pregenerated outputs
        shutil.rmtree('output')
        p = subprocess.check_call(["python", 'exosome.modeling.py', "--test"])
        # todo: assert outputs

    def run_analysis_script(self):
        """Run IMP analysis"""
        p = subprocess.check_call(["python", 'clustering.py'])
        p = subprocess.check_call(["python", 'precision_rmsf.py', "--test"])
        # todo: assert outputs

if __name__ == '__main__':
    unittest.main()
