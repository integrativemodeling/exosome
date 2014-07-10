def get_pdb_bead_bits(hierarchy):
    pdbbits=[]
    beadbits=[]
    for h in hierarchy:
       if "_pdb" in h.get_name():pdbbits.append(h)
       if "_bead" in h.get_name():beadbits.append(h)
    return (pdbbits,beadbits)

def create_density(simo,compname,comphier,txtfilename,mrcfilename,num_components,read=True):
    #density generation for the EM restraint
   (pdbbits,beadbits)=get_pdb_bead_bits(comphier)
   
   
   if read:
      outhier=simo.add_component_density(compname,
                               pdbbits,
                               num_components=num_components, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=txtfilename) # read what it was calculated before

   else:
      outhier=simo.add_component_density(compname,
                               pdbbits,
                               num_components=num_components, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               outputfile=txtfilename, # do the calculation
                               outputmap=mrcfilename,
                               multiply_by_total_mass=True) # do the calculation and output the mrc                                    
   return outhier

def autobuild(simo,comname,pdbname,chain,resrange,read=True,beadsize=5,color=0.0):
    if pdbname is not None:
      if resrange[-1]==-1: resrange=(resrange[0],len(simo.sequence_dict[comname]))
      if read==False:    
         print "res0",comname, resrange
         outhier=simo.autobuild_model(comname, 
                          pdbname=pdbname,
                          chain=chain,
                          resrange=resrange,
                          resolutions=[0,1,10],
                          color=color, 
                          missingbeadsize=beadsize)
      else:
         print "res1",comname, resrange
         outhier=simo.autobuild_model(comname, 
                          pdbname=pdbname,
                          chain=chain,
                          resrange=resrange,                          
                          resolutions=[1,10], 
                          color=color,
                          missingbeadsize=beadsize)                                 
      return outhier
    else:
      seq_len=len(simo.sequence_dict[comname])
      outhier=simo.add_component_necklace(comname,
                            begin=1,
                            end=seq_len,
                            length=beadsize)  
                            
    return outhier    


datadirectory="../data/"

'''
 sizes
 "Dis3",  1001
 "Rrp45", 305
 "Rrp4", 359
 "Csl4", 292
 "Mtr3", 250
 "Rrp40 ", 240
 "Ski7", 747
 "Rrp42", 265
 "Ski6", 246
 "Rrp43", 394
 "Rrp46", 223
 "Lrp1", 184
 "Rrp6", 733
'''



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

domain_dict={}
resdensities=[]
super_rigid_bodies={}

for d in domains:
    comp_name        =d[0]
    hier_name        =d[1]
    color            =d[2]
    fasta_file       =d[3]
    fasta_id         =d[4]
    pdb_name         =d[5]
    chain_id         =d[6]
    res_range        =d[7]
    read_em_files    =d[8]
    bead_size        =d[9]
    super_rb         =d[10]
    em_num_components=d[11]
    em_txt_file_name =d[12]
    em_mrc_file_name =d[13]
    if comp_name not in simo.get_component_names():
       simo.create_component(comp_name,color=0.0)
       simo.add_component_sequence(comp_name,fasta_file,fasta_id)
    outhier=autobuild(simo,comp_name,pdb_name,chain_id,res_range,read=read_em_files,beadsize=bead_size,color=color)
    
    if not read_em_files is None:
       dens_hier=create_density(simo,comp_name,outhier,em_txt_file_name,em_mrc_file_name,em_num_components,read_em_files)
    else:
       dens_hier=[]
    
    resdensities+=dens_hier
    domain_dict[hier_name]=outhier+dens_hier
    simo.set_rigid_body_from_hierarchies(domain_dict[hier_name])
    
    for k in super_rb:
        if k not in super_rigid_bodies:
           super_rigid_bodies[k]=domain_dict[hier_name]
    else:
        super_rigid_bodies[k]+=domain_dict[hier_name]
    
    
    
for c in simo.get_component_names():
    simo.setup_component_sequence_connectivity(c)

for k in super_rigid_bodies:
    simo.set_super_rigid_body_from_hierarchies(super_rigid_bodies[k])

simo.set_floppy_bodies()

