import IMP
import IMP.core
import IMP.algebra
import IMP.atom
import IMP.container

import IMP.pmi.mmcif
import IMP.pmi.metadata
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
import sys

# setting up parameters

rbmaxtrans = 2.00
fbmaxtrans = 3.00
rbmaxrot=0.04
outputobjects = []
sampleobjects = []

# setting up topology

m = IMP.Model()
simo = IMP.pmi.representation.Representation(m,upperharmonic=True,disorderedlength=False)

# We used Phyre2 to generate a model for Ski7
simo.add_metadata(IMP.pmi.metadata.Software(
          name='Phyre2', classification='protein homology modeling',
          description='Protein Homology/analogY Recognition Engine V 2.0',
          version='2.0',
          url='http://www.sbg.bio.ic.ac.uk/~phyre2/'))
simo.add_metadata(IMP.pmi.metadata.Citation(
          pmid='26436480',
          title="A strategy for dissecting the architectures of native "
                "macromolecular assemblies.",
          journal="Nat Methods", volume=12, page_range=(1135,1138),
          year=2015,
          authors=['Shi Y', 'Pellarin R', 'Fridy PC', 'Fernandez-Martinez J',
                   'Thompson MK', 'Li Y', 'Wang QJ', 'Sali A', 'Rout MP',
                   'Chait BT'],
          doi='10.1038/nmeth.3617'))
simo.add_metadata(IMP.pmi.metadata.Repository(
          doi="10.5281/zenodo.60731", root="..",
          url="https://zenodo.org/record/60731/files/exosome-v1.0.zip",
          top_directory="exosome-v1.0"))

if '--mmcif' in sys.argv:
    # Record the modeling protocol to an mmCIF file
    po = IMP.pmi.mmcif.ProtocolOutput(open('exosome.cif', 'w'))
    simo.add_protocol_output(po)

simo.dry_run = '--dry-run' in sys.argv

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




bm1=IMP.pmi.macros.BuildModel1(simo)
bm1.build_model(domains)
resdensities=bm1.get_density_hierarchies([h[1] for h in domains])

# Add components that we didn't model but which we have experimental data
# (crosslinks) for. This helps us to interpret the crosslinks file later.
simo.create_non_modeled_component('RPL3')
simo.add_component_sequence('RPL3', datadirectory+"exosome.fasta")

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



columnmap={}
columnmap["Protein1"]="Protein 1"
columnmap["Protein2"]="Protein 2"
columnmap["Residue1"]="Residue1"
columnmap["Residue2"]="Residue2"
columnmap["IDScore"]="Score"
columnmap["XLUniqueID"]="Unique ID"
rename={"GFP":"Rrp46_gfp","Rrp46":"Rrp46_gfp"}
offset={"GFP":246}

ids_map=IMP.pmi.tools.map()
ids_map.set_map_element(1.0,1.0)

xl1 = IMP.pmi.restraints.crosslinking.ISDCrossLinkMS(simo,
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
mc1=IMP.pmi.macros.ReplicaExchange0(m,
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
                                    replica_stat_file_suffix="stat_replica",
                                    test_mode=simo.dry_run)
mc1.execute_macro()

if '--mmcif' in sys.argv:
    # Add clustering info to the mmCIF file
    os.chdir('../Rrp6.analysis')
    loc = IMP.pmi.metadata.FileLocation('clustering.py',
                              details='Main clustering and analysis script')
    simo.add_metadata(IMP.pmi.metadata.PythonScript(location=loc))
    with open('clustering.py') as fh:
        exec(fh.read())
    po.flush()
