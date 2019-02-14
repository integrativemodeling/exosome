#!/usr/bin/env python

import IMP
import IMP.core
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi1.restraints.crosslinking
import IMP.pmi1.restraints.stereochemistry
import IMP.pmi1.restraints.em
import IMP.pmi1.restraints.basic
import IMP.pmi1.representation
import IMP.pmi1.tools
import IMP.pmi1.samplers
import IMP.pmi1.output
import IMP.pmi1.macros

import os
import sys
import unittest

TESTDIR = os.path.abspath(os.path.dirname(sys.argv[0]))

class Tests(unittest.TestCase):
    def test_Ski7(self):
        """Test Ski7"""
        os.chdir(TESTDIR)

        # setting up parameters

        rbmaxtrans = 2.00
        fbmaxtrans = 3.00
        rbmaxrot=0.04
        outputobjects = []
        sampleobjects = []

        # setting up topology

        m = IMP.Model()
        simo = IMP.pmi1.representation.Representation(m,upperharmonic=True,disorderedlength=False)

        datadirectory="../data/"

        # compname         hier_name     color    fastafile                      fastaid  pdbname                   chain resrange    read                     beadsize rigid_body super_rigid_body emnum_components, emtxtfilename    emmrcfilename
        domains=[("Dis3",  "Dis3_1",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (1,237,0),    None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Dis3",  "Dis3_2",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (238,471,0),  None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Dis3",  "Dis3_3",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (472,-1,0),   None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp45", "Rrp45",      0.1,     datadirectory+"exosome.fasta", "Rrp45", datadirectory+"4IFD.pdb", "A",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp4",  "Rrp4_1",     0.2,     datadirectory+"exosome.fasta", "Rrp4",  datadirectory+"4IFD.pdb", "H",  (1,102,0),    None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp4",  "Rrp4_2",     0.2,     datadirectory+"exosome.fasta", "Rrp4",  datadirectory+"4IFD.pdb", "H",  (103,-1,0),   None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Csl4",  "Csl4",       0.3,     datadirectory+"exosome.fasta", "Csl4",  datadirectory+"4IFD.pdb", "I",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Mtr3",  "Mtr3_1",     0.4,     datadirectory+"exosome.fasta", "Mtr3",  datadirectory+"4IFD.pdb", "F",  (1,30,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Mtr3",  "Mtr3_2",     0.4,     datadirectory+"exosome.fasta", "Mtr3",  datadirectory+"4IFD.pdb", "F",  (31,-1,0),    None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp40", "Rrp40_1",    0.5,     datadirectory+"exosome.fasta", "Rrp40", datadirectory+"4IFD.pdb", "G",  (1,60,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp40", "Rrp40_2",    0.5,     datadirectory+"exosome.fasta", "Rrp40", datadirectory+"4IFD.pdb", "G",  (61,-1,0),    None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp42", "Rrp42",      0.6,     datadirectory+"exosome.fasta", "Rrp42", datadirectory+"4IFD.pdb", "E",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Ski6",  "Ski6",       0.7,     datadirectory+"exosome.fasta", "Rrp42", datadirectory+"4IFD.pdb", "B",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Rrp46_gfp", "Rrp46_1",  0.8,   datadirectory+"exosome.fasta", "Rrp46_gfp", datadirectory+"4IFD.pdb", "D",  (1,246,0),     None,               5,       0,         [0],     0,                None,            None, None),
                 ("Rrp46_gfp", "Rrp46_2",  1.0,   datadirectory+"exosome.fasta", "Rrp46_gfp", datadirectory+"GFP_1GFL.pdb", "A",  (1,229,246),     None,         5,       5,         [5],     0,                None,            None, None),
                 ("Rrp43", "Rrp43",      0.9,     datadirectory+"exosome.fasta", "Rrp43", datadirectory+"4IFD.pdb", "C",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
                 ("Ski7",  "Ski7",       0.65,    datadirectory+"exosome.fasta", "Ski7",  datadirectory+"Ski7_3izq_modeller_vmd.pdb", "X",  (1,-1),    None,     5,       2,         [2],     0,                None,            None, None)]

        bm1=IMP.pmi1.macros.BuildModel1(simo)
        bm1.build_model(domains,rmf_file="../Ski7.analysis/kmeans_weight_500_2/cluster.1/0.rmf3",rmf_frame_number=0)
        resdensities=bm1.get_density_hierarchies([h[1] for h in domains])

        # defines the movers

        simo.set_rigid_bodies_max_rot(rbmaxrot)
        simo.set_floppy_bodies_max_trans(fbmaxtrans)
        simo.set_rigid_bodies_max_trans(rbmaxtrans)

        outputobjects.append(simo)
        sampleobjects.append(simo)

        # scoring function

        ev = IMP.pmi1.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
        ev.add_to_model()
        outputobjects.append(ev)


        columnmap={}
        columnmap["Protein1"]="Protein 1"
        columnmap["Protein2"]="Protein 2"
        columnmap["Residue1"]="Residue1"
        columnmap["Residue2"]="Residue2"
        columnmap["IDScore"]="Score"
        columnmap["XLUniqueID"]="Unique ID"
        rename={"GFP":"Rrp46_gfp","Rrp46":"Rrp46_gfp"}
        offset={"GFP":246}

        ids_map=IMP.pmi1.tools.map()
        ids_map.set_map_element(1.0,1.0)

        xl1 = IMP.pmi1.restraints.crosslinking.ISDCrossLinkMS(simo,
                                           '../data/exosome_XLMS_column07012014.csv',
                                           length=21.0,
                                           slope=0.01,
                                           columnmapping=columnmap,
                                           ids_map=ids_map,
                                           resolution=1.0,
                                           label="DSS",
                                           csvfile=True,
                                           rename_dict=rename,
                                           offset_dict=offset)
        xl1.add_to_model()
        sampleobjects.append(xl1)
        outputobjects.append(xl1)
        xl1.set_psi_is_sampled(False)
        psi=xl1.get_psi(1.0)[0]
        psi.set_scale(0.05)

        o=IMP.pmi1.output.Output()
        #o.write_test("test.Ski7.out",[simo,xl1,ev])
        o.test("test.Ski7.out",[simo,xl1,ev])

if __name__ == '__main__':
    unittest.main()
