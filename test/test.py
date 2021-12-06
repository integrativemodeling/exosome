#!/usr/bin/env python

import unittest
import os
import sys
import utils
import subprocess
import ihm.reader

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(utils.TestBase):
    def test_mmcif(self):
        """Test generation of mmCIF output"""
        os.chdir(os.path.join(TOPDIR, 'modeling-scripts_Rrp6.1'))
        if os.path.exists("exosome.cif"):
            os.unlink("exosome.cif")
        # Potentially override methods that need network access
        env = os.environ.copy()
        env['PYTHONPATH'] = os.path.join(TOPDIR, 'test', 'mock') \
                            + ':' + env.get('PYTHONPATH', '')
        p = subprocess.check_call(
                ["python", "exosome.modeling.py", "--mmcif", "--dry-run"],
                env=env)
        # Check output file
        self._check_mmcif_file('exosome.cif')

    def _check_mmcif_file(self, fname):
        with open(fname) as fh:
            s, = ihm.reader.read(fh)
        self.assertEqual(len(s.citations), 4)
        self.assertEqual(len(s.software), 3)
        self.assertEqual(len(s.orphan_starting_models), 14)
        # Should be 2 states
        self.assertEqual(len(s.state_groups), 1)
        state1, state2 = s.state_groups[0]
        self.assertEqual(state1.name,
                         "Rrp6-Lrp1-Mpp6-exo10 nucleus-localized complex")
        self.assertEqual(state2.name,
                         "Ski7-exo10 cytoplasm-localized complex")
        # Each state has 2 models
        self.assertEqual(sum(len(x) for x in state1), 2)
        self.assertEqual(sum(len(x) for x in state2), 2)
        # Check # of spheres and atoms in each model
        models = [g[0] for g in state1]
        self.assertEqual([len(m._spheres) for m in models], [4198, 4198])
        self.assertEqual([len(m._atoms) for m in models], [0, 0])
        models = [g[0] for g in state2]
        self.assertEqual([len(m._spheres) for m in models], [4139, 4139])
        self.assertEqual([len(m._atoms) for m in models], [0, 0])

        # Should be 4 ensembles (clusters)
        self.assertEqual([e.num_models for e in s.ensembles],
                         [69, 131, 159, 41])
        # Check localization densities
        self.assertEqual([len(e.densities) for e in s.ensembles], [4, 4, 2, 2])
        self.assertEqual([len(e.sequence) for e in s.entities],
                         [1001, 305, 359, 292, 250, 240, 265, 265, 475, 394,
                          184, 733, 186, 387, 747])
        self.assertEqual([a.details for a in s.asym_units],
                         ['Dis3', 'Rrp45', 'Rrp4', 'Csl4', 'Mtr3', 'Rrp40',
                          'Rrp42', 'Ski6', 'Rrp46_gfp', 'Rrp43', 'Lrp1',
                          'Rrp6', 'MPP6', 'Ski7'])
        # Just one restraint - crosslinks
        xl, = s.restraints
        self.assertEqual(len(xl.experimental_cross_links), 218)
        self.assertEqual(len(xl.cross_links), 216)
        self.assertEqual(xl.dataset.location.path,
                         'exosome-v1.0.1/data/exosome_XLMS_column07012014.csv')
        self.assertEqual(sum(len(x.fits) for x in xl.cross_links), 628)


if __name__ == '__main__':
    unittest.main()
