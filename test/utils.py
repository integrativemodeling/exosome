import unittest
import subprocess
import shutil

class TestBase(unittest.TestCase):
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
