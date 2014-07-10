   


datadirectory="../data/"


# compname         hier_name     color    fastafile                      fastaid  pdbname                   chain resrange    read    beadsize super_rigid_body emnum_components, emtxtfilename                               emmrcfilename                    
domains=[("Dis3",  "Dis3_1",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (1,237),    True,   5,       [0,10,12],       5,                datadirectory+'densities/Dis3_1_dens.txt',  datadirectory+'densities/Dis3_1_dens.mrc'),
         ("Dis3",  "Dis3_2",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (243,471),  True,   5,       [0,10,12],       5,                datadirectory+'densities/Dis3_2_dens.txt',  datadirectory+'densities/Dis3_2_dens.mrc'),
         ("Dis3",  "Dis3_3",     0.0,     datadirectory+"exosome.fasta", "Dis3",  datadirectory+"4IFD.pdb", "J",  (472,-1),   True,   5,       [0,10,12],       10,               datadirectory+'densities/Dis3_3_dens.txt',  datadirectory+'densities/Dis3_3_dens.mrc'),
         ("Rrp45", "Rrp45",      0.1,     datadirectory+"exosome.fasta", "Rrp45", datadirectory+"4IFD.pdb", "A",  (1,-1),     True,   5,       [10,12],         6,                datadirectory+'densities/Rrp45_dens.txt',   datadirectory+'densities/Rrp45_dens.mrc'),
         ("Rrp4",  "Rrp4_1",     0.2,     datadirectory+"exosome.fasta", "Rrp4",  datadirectory+"4IFD.pdb", "H",  (1,102),    True,   5,       [1,6,9,12],      2,                datadirectory+'densities/Rrp4_1_dens.txt',  datadirectory+'densities/Rrp4_1_dens.mrc'),
         ("Rrp4",  "Rrp4_2",     0.2,     datadirectory+"exosome.fasta", "Rrp4",  datadirectory+"4IFD.pdb", "H",  (103,-1),   True,   5,       [1,6,9,12],      4,                datadirectory+'densities/Rrp4_2_dens.txt',  datadirectory+'densities/Rrp4_2_dens.mrc'),
         ("Csl4",  "Csl4",       0.3,     datadirectory+"exosome.fasta", "Csl4",  datadirectory+"4IFD.pdb", "I",  (1,-1),     True,   5,       [11,12],         6,                datadirectory+'densities/Csl4_dens.txt',    datadirectory+'densities/Csl4_dens.mrc'),
         ("Mtr3",  "Mtr3_1",     0.4,     datadirectory+"exosome.fasta", "Mtr3",  datadirectory+"4IFD.pdb", "F",  (1,30),     None,   5,       [2,12],          0,                None,                                       None),
         ("Mtr3",  "Mtr3_2",     0.4,     datadirectory+"exosome.fasta", "Mtr3",  datadirectory+"4IFD.pdb", "F",  (31,-1),    True,   5,       [2,12],          5,                datadirectory+'densities/Mtr3_dens.txt',    datadirectory+'densities/Mtr3_dens.mrc'),
         ("Rrp40", "Rrp40_1",    0.5,     datadirectory+"exosome.fasta", "Rrp40", datadirectory+"4IFD.pdb", "G",  (1,60),     True,   5,       [3,12],          1,                datadirectory+'densities/Rrp40_1_dens.txt', datadirectory+'densities/Rrp40_1_dens.mrc'),
         ("Rrp40", "Rrp40_2",    0.5,     datadirectory+"exosome.fasta", "Rrp40", datadirectory+"4IFD.pdb", "G",  (61,-1),    True,   5,       [3,12],          4,                datadirectory+'densities/Rrp40_2_dens.txt', datadirectory+'densities/Rrp40_2_dens.mrc'),
         ("Rrp42", "Rrp42",      0.6,     datadirectory+"exosome.fasta", "Rrp42", datadirectory+"4IFD.pdb", "E",  (1,-1),     True,   5,       [11,12],         5,                datadirectory+'densities/Rrp42_dens.txt',   datadirectory+'densities/Rrp42_dens.mrc'),
         ("Ski6",  "Ski6",       0.7,     datadirectory+"exosome.fasta", "Rrp42", datadirectory+"4IFD.pdb", "B",  (1,-1),     True,   5,       [12],            5,                datadirectory+'densities/Ski6_dens.txt',    datadirectory+'densities/Ski6_dens.mrc'),
         ("Rrp46", "Rrp46",      0.8,     datadirectory+"exosome.fasta", "Rrp46", datadirectory+"4IFD.pdb", "D",  (1,-1),     True,   5,       [12],            5,                datadirectory+'densities/Rrp46_dens.txt',   datadirectory+'densities/Rrp46_dens.mrc'),
         ("Rrp43", "Rrp43",      0.9,     datadirectory+"exosome.fasta", "Rrp43", datadirectory+"4IFD.pdb", "C",  (1,-1),     True,   5,       [6,8,12],        8,                datadirectory+'densities/Rrp43_dens.txt',   datadirectory+'densities/Rrp43_dens.mrc'),
         ("Lrp1",  "Lrp1",       1.0,     datadirectory+"exosome.fasta", "Lrp1",  None                    , " ",  (1,-1),     None,   5,       [5,7,12,13],     0,                None,                                       None),
         ("Rrp6",  "Rrp6_1",     0.65,    datadirectory+"exosome.fasta", "Rrp6",  datadirectory+"2HBJ.pdb", "A",  (1,526),    None,   5,       [4,6,7,8,9,12,13], 0,                None,                                       None),
         ("Rrp6",  "Rrp6_2",     0.65,    datadirectory+"exosome.fasta", "Rrp6",  datadirectory+"4IFD.pdb", "K",  (527,560),  None,   5,       [4,6,7,8,9,12],  0,                None,                                       None),
         ("Rrp6",  "Rrp6_3",     0.65,    datadirectory+"exosome.fasta", "Rrp6",  datadirectory+"4IFD.pdb", "K",  (561,-1),   None,   5,       [4,6,7,8,9,12],  0,                None,                                       None)]

bm1=IMP.pmi.macros.BuildModel1(simo)
bm1.build_model(domains)
resdensities=bm1.get_density_hierarchies()
