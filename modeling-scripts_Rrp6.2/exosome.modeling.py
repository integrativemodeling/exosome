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
         ("Ski6",  "Ski6",       0.7,     datadirectory+"exosome.fasta", "Ski6", datadirectory+"4IFD.pdb", "B",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
         ("Rrp46_gfp", "Rrp46_1",  0.8,   datadirectory+"exosome.fasta", "Rrp46_gfp", datadirectory+"4IFD.pdb", "D",  (1,246,0),     None,               5,       0,         [0],     0,                None,            None, None),
         ("Rrp46_gfp", "Rrp46_2",  1.0,   datadirectory+"exosome.fasta", "Rrp46_gfp", datadirectory+"GFP_1GFL.pdb", "A",  (1,229,246),     None,         5,       5,         [5],     0,                None,            None, None),
         ("Rrp43", "Rrp43",      0.9,     datadirectory+"exosome.fasta", "Rrp43", datadirectory+"4IFD.pdb", "C",  (1,-1,0),     None,                    5,       0,         [0],     0,                None,            None, None),
         ("Lrp1",  "Lrp1",       1.0,     datadirectory+"exosome.fasta", "Lrp1",  None                    , " ",  (1,-1,0),     None,                    5,       1,         [1],     0,                None,            None, None),
         ("Rrp6",  "Rrp6_1",     0.65,    datadirectory+"exosome.fasta", "Rrp6",  datadirectory+"2HBJ.pdb", "A",  (1,526,0),    None,                    5,       2,         [2],     0,                None,            None, None),
         ("Rrp6",  "Rrp6_2",     0.65,    datadirectory+"exosome.fasta", "Rrp6",  datadirectory+"4IFD.pdb", "K",  (527,733,0),  None,                    5,       0,         [0],     0,                None,            None, None),
         ("MPP6",  "MPP6",       0.55,    datadirectory+"exosome.fasta", "Mpp6",  None,                     " ",  (1,-1,0),     None,                    5,       3,         [3],     0,                None,            None, None)]




bm1=IMP.pmi1.macros.BuildModel1(simo)
bm1.build_model(domains)
resdensities=bm1.get_density_hierarchies([h[1] for h in domains])


# randomize the initial configuration

simo.shuffle_configuration(100)

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


# sampling

simo.optimize_floppy_bodies(100)

nframes=50000
if '--test' in sys.argv: nframes=2000
mc1=IMP.pmi1.macros.ReplicaExchange0(m,
                                    simo,
                                    monte_carlo_sample_objects=sampleobjects,
                                    output_objects=outputobjects,
                                    crosslink_restraints=[xl1],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=nframes,
                                    write_initial_rmf=True,
                                    initial_rmf_name_suffix="initial",
                                    stat_file_name_suffix="stat",
                                    best_pdb_name_suffix="model",
                                    do_clean_first=True,
                                    do_create_directories=True,
                                    global_output_directory="output",
                                    rmf_dir="rmfs/",
                                    best_pdb_dir="pdbs/",
                                    replica_stat_file_suffix="stat_replica")
mc1.execute_macro()



