import IMP
import IMP.core
import IMP.base
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.restraints.crosslinking
import IMP.pmi.restraints.stereochemistry
import IMP.pmi.restraints.em
import IMP.pmi.restraints.basic
import IMP.pmi.representation
import IMP.pmi.tools
import IMP.pmi.samplers
import IMP.pmi.output
import IMP.pmi.macros

import os

# setting up parameters

rbmaxtrans = 4.00
fbmaxtrans = 4.00
rbmaxrot=0.04
outputobjects = []
sampleobjects = []

# setting up topology

m = IMP.Model()
simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=False)

datadirectory="../data/"


# compname         hier_name     color    fastafile                      fastaid  pdbname                   chain resrange    read                     beadsize rigid_body super_rigid_body emnum_components, emtxtfilename    emmrcfilename                    
domains=[("Dis3",  "Dis3_1",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (1,237,0),    True,                    5,       0,         [0,17],     -20,                datadirectory+"Dis3_1.txt",            datadirectory+"Dis3_1.mrc",      None),
         ("Dis3",  "Dis3_2",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (238,471,0),  True,                    5,       1,         [1,17],     -20,                datadirectory+"Dis3_2.txt",            datadirectory+"Dis3_2.mrc",      None),
         ("Dis3",  "Dis3_3",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (472,-1,0),   True,                    5,       2,         [2,17],     -20,                datadirectory+"Dis3_3.txt",            datadirectory+"Dis3_3.mrc",      None),
         ("Rrp45", "Rrp45",      0.1,     datadirectory+"exosome.fasta", "Rrp45", datadirectory+"4IFD.pdb", "A",  (1,-1,0),     True,                    5,       3,         [3,17],     -20,                datadirectory+"Rrp45.txt",             datadirectory+"Rrp45.mrc",      None),
         ("Rrp4",  "Rrp4_1",     0.2,     datadirectory+"exosome.fasta", "Rrp4",  datadirectory+"4IFD.pdb", "H",  (1,102,0),    True,                    5,       4,         [4,17],     -20,                datadirectory+"Rrp4_1.txt",            datadirectory+"Rrp4_1.mrc",      None),
         ("Rrp4",  "Rrp4_2",     0.2,     datadirectory+"exosome.fasta", "Rrp4",  datadirectory+"4IFD.pdb", "H",  (103,-1,0),   True,                    5,       5,         [5,17],     -20,                datadirectory+"Rrp4_2.txt",            datadirectory+"Rrp4_2.mrc",      None),
         ("Csl4",  "Csl4",       0.3,     datadirectory+"exosome.fasta", "Csl4",  datadirectory+"4IFD.pdb", "I",  (1,-1,0),     True,                    5,       6,         [6,17],     -20,                datadirectory+"Csl4.txt",              datadirectory+"Csl4.mrc",      None),
         ("Mtr3",  "Mtr3_1",     0.4,     datadirectory+"exosome.fasta", "Mtr3",  datadirectory+"4IFD.pdb", "F",  (1,30,0),     None,                    5,       7,         [7,17],     0,                None,            None,      None),
         ("Mtr3",  "Mtr3_2",     0.4,     datadirectory+"exosome.fasta", "Mtr3",  datadirectory+"4IFD.pdb", "F",  (31,-1,0),    True,                    5,       8,         [8,17],     -20,                datadirectory+"Mtr3_2.txt",            datadirectory+"Mtr3_2.mrc",      None),
         ("Rrp40", "Rrp40_1",    0.5,     datadirectory+"exosome.fasta", "Rrp40", datadirectory+"4IFD.pdb", "G",  (1,60,0),     True,                    5,       9,         [9,17],     -20,                datadirectory+"Rrp40_1.txt",           datadirectory+"Rrp40_1.mrc",      None),
         ("Rrp40", "Rrp40_2",    0.5,     datadirectory+"exosome.fasta", "Rrp40", datadirectory+"4IFD.pdb", "G",  (61,-1,0),    True,                    5,       10,         [10,17],     -20,                datadirectory+"Rrp40_2.txt",         datadirectory+"Rrp40_2.mrc",      None),
         ("Rrp42", "Rrp42",      0.6,     datadirectory+"exosome.fasta", "Rrp42", datadirectory+"4IFD.pdb", "E",  (1,-1,0),     True,                    5,       11,         [11,17],     -20,                datadirectory+"Rrp42.txt",           datadirectory+"Rrp42.mrc",      None),
         ("Ski6",  "Ski6",       0.7,     datadirectory+"exosome.fasta", "Rrp42", datadirectory+"4IFD.pdb", "B",  (1,-1,0),     True,                    5,       12,         [12,17],     -20,                datadirectory+"Ski6.txt",            datadirectory+"Ski6.mrc",      None),
         ("Rrp46_gfp", "Rrp46_1",  0.8,   datadirectory+"exosome.fasta", "Rrp46_gfp", datadirectory+"4IFD.pdb", "D",  (1,246,0),     True,               5,       13,         [13,17],     -20,                datadirectory+"Rrp46_1.txt",         datadirectory+"Rrp46_1.mrc",      None),
         ("Rrp46_gfp", "Rrp46_2",  1.0,   datadirectory+"exosome.fasta", "Rrp46_gfp", datadirectory+"GFP_1GFL.pdb", "A",  (1,229,246),     None,         5,       14,         [14,17],     0,                None,            None,      None),
         ("Rrp43", "Rrp43",      0.9,     datadirectory+"exosome.fasta", "Rrp43", datadirectory+"4IFD.pdb", "C",  (1,-1,0),     True,                    5,       15,         [15,17],     -20,                datadirectory+"Rrp43.txt",            datadirectory+"Rrp43.mrc",      None)]




bm1=IMP.pmi.macros.BuildModel1(simo)
bm1.build_model(domains)
resdensities=bm1.get_density_hierarchies([d[1] for d in domains])


# randomize the initial configuration

simo.shuffle_configuration(100)

# defines the movers

simo.set_rigid_bodies_max_rot(rbmaxrot)
simo.set_floppy_bodies_max_trans(fbmaxtrans)
simo.set_rigid_bodies_max_trans(rbmaxtrans)

outputobjects.append(simo)
sampleobjects.append(simo)

# scoring function

ev = IMP.pmi.restraints.stereochemistry.ExcludedVolumeSphere(simo,resolution=10)
ev.add_to_model()
outputobjects.append(ev)



from IMP.pmi.io.crosslink import FilterOperator as FO
import operator
cldbkc=IMP.pmi.io.crosslink.CrossLinkDataBaseKeywordsConverter()
cldbkc.set_protein1_key("Protein 1")
cldbkc.set_protein2_key("Protein 2")
cldbkc.set_residue1_key("Residue1")
cldbkc.set_residue2_key("Residue2")
cldb=IMP.pmi.io.crosslink.CrossLinkDataBase(cldbkc)
cldb.create_set_from_file('../data/exosome_XLMS_column07012014.csv')
cldb.offset_residue_index("GFP",246)
cldb.set_value(cldb.protein1_key,"Rrp46_gfp",FO(cldb.protein1_key,operator.eq,"GFP"))
cldb.set_value(cldb.protein1_key,"Rrp46_gfp",FO(cldb.protein1_key,operator.eq,"Rrp46"))
cldb.set_value(cldb.protein2_key,"Rrp46_gfp",FO(cldb.protein2_key,operator.eq,"GFP"))
cldb.set_value(cldb.protein2_key,"Rrp46_gfp",FO(cldb.protein2_key,operator.eq,"Rrp46"))

import IMP.pmi.restraints.crosslinking_new
xl = IMP.pmi.restraints.crosslinking_new.CrossLinkingMassSpectrometryRestraint(simo,
                            cldb,
                            length=21.0,
                            slope=0.01,
                            resolution=1.0,
                            label="XL")
xl.add_to_model()
sigma=xl.sigma_dictionary["SIGMA"][0]
psi=xl.psi_dictionary["PSI"][0]
sigma.set_scale(9.0)
psi.set_scale(0.01)
xl.set_psi_is_sampled(False)
xl.set_sigma_is_sampled(True)
sampleobjects.append(xl)
outputobjects.append(xl)



simo.optimize_floppy_bodies(100)


gemt = IMP.pmi.restraints.em.GaussianEMRestraint(resdensities,
                                                 '../data/emd_1438_endogenous_noDis3.map.mrc.gmm.50.txt',
                                                 scale_target_to_mass=True,
                                                 slope=0.000001,
                                                 weight=80.0)
gemt.add_to_model()
outputobjects.append(gemt)



# sampling
mc1=IMP.pmi.macros.ReplicaExchange0(m,
                                    simo,
                                    monte_carlo_sample_objects=sampleobjects,
                                    output_objects=outputobjects,
                                    crosslink_restraints=[xl],
                                    monte_carlo_temperature=1.0,
                                    replica_exchange_minimum_temperature=1.0,
                                    replica_exchange_maximum_temperature=2.5,
                                    number_of_best_scoring_models=500,
                                    monte_carlo_steps=10,
                                    number_of_frames=50000,
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



