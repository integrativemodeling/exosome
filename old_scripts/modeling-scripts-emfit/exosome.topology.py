def get_pdb_bead_bits(hierarchy):
    pdbbits=[]
    beadbits=[]
    for h in hierarchy:
       if "_pdb" in h.get_name():pdbbits.append(h)
       if "_bead" in h.get_name():beadbits.append(h)
    return (pdbbits,beadbits)
    
datadirectory="../data/"

'''
 "Dis3 ",  1001
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

beadsize=10

#-----------------
simo.create_component("Dis3",color=0.0)
simo.add_component_sequence("Dis3", datadirectory+"exosome.fasta",id="Dis3")
Dis3=simo.autobuild_model("Dis3", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="J",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Dis3)
Dis3_dens=simo.add_component_density("Dis3",
                               pdbbits,
                               num_components=20, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Dis3_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Dis3_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Dis3_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc
                          

simo.show_component_table("Dis3")
simo.setup_component_geometry("Dis3")



#-----------------

simo.create_component("Rrp45",color=0.1)
simo.add_component_sequence("Rrp45", datadirectory+"exosome.fasta",id="Rrp45")
Rrp45=simo.autobuild_model("Rrp45", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="A",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Rrp45)
Rrp45_dens=simo.add_component_density("Rrp45",
                               pdbbits,
                               num_components=6, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Rrp45_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Rrp45_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Rrp45_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                          
                          
simo.show_component_table("Rrp45")
simo.setup_component_geometry("Rrp45")



#-----------------

simo.create_component("Rrp4",color=0.2)
simo.add_component_sequence("Rrp4", datadirectory+"exosome.fasta",id="Rrp4")
Rrp4=simo.autobuild_model("Rrp4", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="H",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Rrp4)
Rrp4_dens=simo.add_component_density("Rrp4",
                               pdbbits,
                               num_components=7, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Rrp4_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Rrp4_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Rrp4_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc  
                          
simo.show_component_table("Rrp4")
simo.setup_component_geometry("Rrp4")



#-----------------

simo.create_component("Csl4",color=0.3)
simo.add_component_sequence("Csl4", datadirectory+"exosome.fasta",id="Csl4")
Csl4=simo.autobuild_model("Csl4", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="I",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          

#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Csl4)
Csl4_dens=simo.add_component_density("Csl4",
                               pdbbits,
                               num_components=6, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Csl4_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Csl4_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Csl4_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc  
                          
simo.show_component_table("Csl4")
simo.setup_component_geometry("Csl4")

#-----------------

simo.create_component("Mtr3",color=0.4)
simo.add_component_sequence("Mtr3", datadirectory+"exosome.fasta",id="Mtr3")
Mtr3=simo.autobuild_model("Mtr3", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="F",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Mtr3)
Mtr3_dens=simo.add_component_density("Mtr3",
                               pdbbits,
                               num_components=5, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Mtr3_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Mtr3_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Mtr3_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                            
                          
simo.show_component_table("Mtr3")
simo.setup_component_geometry("Mtr3")
#-----------------

simo.create_component("Rrp40",color=0.5)
simo.add_component_sequence("Rrp40", datadirectory+"exosome.fasta",id="Rrp40")
Rrp40=simo.autobuild_model("Rrp40", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="G",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Rrp40)
Rrp40_dens=simo.add_component_density("Rrp40",
                               pdbbits,
                               num_components=5, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Rrp40_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Rrp40_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Rrp40_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                             
                          
simo.show_component_table("Rrp40")
simo.setup_component_geometry("Rrp40")



#-----------------

simo.create_component("Rrp42",color=0.6)
simo.add_component_sequence("Rrp42", datadirectory+"exosome.fasta",id="Rrp42")
Rrp42=simo.autobuild_model("Rrp42", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="E",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Rrp42)
Rrp42_dens=simo.add_component_density("Rrp42",
                               pdbbits,
                               num_components=5, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Rrp42_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Rrp42_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Rrp42_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                            
                          
simo.show_component_table("Rrp42")
simo.setup_component_geometry("Rrp42")



#-----------------

simo.create_component("Ski6",color=0.7)
simo.add_component_sequence("Ski6", datadirectory+"exosome.fasta",id="Ski6")
Ski6=simo.autobuild_model("Ski6", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="B",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Ski6)
Ski6_dens=simo.add_component_density("Ski6",
                               pdbbits,
                               num_components=5, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Ski6_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Ski6_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Ski6_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                                    
                          
                          
simo.show_component_table("Ski6")
simo.setup_component_geometry("Ski6")



#-----------------

simo.create_component("Rrp46",color=0.8)
simo.add_component_sequence("Rrp46", datadirectory+"exosome.fasta",id="Rrp46")
Rrp46=simo.autobuild_model("Rrp46", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="D",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Rrp46)
Rrp46_dens=simo.add_component_density("Rrp46",
                               pdbbits,
                               num_components=5, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Rrp46_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Rrp46_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Rrp46_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                                 
                          
simo.show_component_table("Rrp46")
simo.setup_component_geometry("Rrp46")


#-----------------

simo.create_component("Rrp43",color=0.9)
simo.add_component_sequence("Rrp43", datadirectory+"exosome.fasta",id="Rrp43")
Rrp43=simo.autobuild_model("Rrp43", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="C",
                          resolutions=[1,10], 
                          missingbeadsize=beadsize)
                          
#density generation for the EM restraint
(pdbbits,beadbits)=get_pdb_bead_bits(Rrp43)
Rrp43_dens=simo.add_component_density("Rrp43",
                               pdbbits,
                               num_components=8, # number of gaussian into which the simulated density is approximated
                               resolution=0,      # resolution that you want to calculate the simulated density
                               inputfile=datadirectory+'densities/Rrp43_dens.txt') # read what it was calculated before
                               #outputfile=datadirectory+'densities/Rrp43_dens.txt', # do the calculation
                               #outputmap=datadirectory+'densities/Rrp43_dens.mrc',
                               #multiply_by_total_mass=True) # do the calculation and output the mrc                                       
                          
simo.show_component_table("Rrp43")
simo.setup_component_geometry("Rrp43")


#-----------------

simo.create_component("Lrp1",color=1.0)
simo.add_component_sequence("Lrp1", datadirectory+"exosome.fasta",id="Lrp1")
Lrp1=simo.add_component_necklace("Lrp1",
                            begin=1,
                            end=184,
                            length=5)
simo.show_component_table("Lrp1")
simo.setup_component_geometry("Lrp1")
#-----------------

simo.create_component("Rrp6",color=0.95)
simo.add_component_sequence("Rrp6", datadirectory+"exosome.fasta",id="Rrp6")
Rrp6_1=simo.autobuild_model("Rrp6", 
                          pdbname=datadirectory+"2HBJ.pdb",
                          chain="A",
                          resolutions=[1,10], 
                          resrange=(1,526),
                          missingbeadsize=beadsize)
Rrp6_2=simo.autobuild_model("Rrp6", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="K",
                          resolutions=[1,10], 
                          resrange=(527,560),                          
                          missingbeadsize=beadsize)
Rrp6_3=simo.autobuild_model("Rrp6", 
                          pdbname=datadirectory+"4IFD.pdb",
                          chain="K",
                          resolutions=[1,10], 
                          resrange=(561,733),                          
                          missingbeadsize=beadsize)
simo.show_component_table("Rrp6")
simo.setup_component_geometry("Rrp6")
#-----------------


simo.setup_component_sequence_connectivity("Dis3") 
simo.setup_component_sequence_connectivity("Rrp45")
simo.setup_component_sequence_connectivity("Rrp4")
simo.setup_component_sequence_connectivity("Csl4")
simo.setup_component_sequence_connectivity("Mtr3")
simo.setup_component_sequence_connectivity("Rrp40")
simo.setup_component_sequence_connectivity("Rrp42")
simo.setup_component_sequence_connectivity("Ski6")
simo.setup_component_sequence_connectivity("Rrp43")
simo.setup_component_sequence_connectivity("Rrp46")
simo.setup_component_sequence_connectivity("Lrp1")
simo.setup_component_sequence_connectivity("Rrp6")

simo.set_rigid_body_from_hierarchies(Dis3+Dis3_dens) 
simo.set_rigid_body_from_hierarchies(Rrp45+Rrp45_dens)
simo.set_rigid_body_from_hierarchies(Rrp4+Rrp4_dens)
simo.set_rigid_body_from_hierarchies(Csl4+Csl4_dens)
simo.set_rigid_body_from_hierarchies(Mtr3+Mtr3_dens)
simo.set_rigid_body_from_hierarchies(Rrp40+Rrp40_dens)
simo.set_rigid_body_from_hierarchies(Rrp42+Rrp42_dens)
simo.set_rigid_body_from_hierarchies(Ski6+Ski6_dens)
simo.set_rigid_body_from_hierarchies(Rrp43+Rrp43_dens)
simo.set_rigid_body_from_hierarchies(Rrp46+Rrp46_dens)
simo.set_rigid_body_from_hierarchies(Lrp1)
simo.set_rigid_body_from_hierarchies(Rrp6_1)
simo.set_rigid_body_from_hierarchies(Rrp6_2)
simo.set_rigid_body_from_hierarchies(Rrp6_3)

resdensities=Dis3_dens+Rrp45_dens+Rrp4_dens+Csl4_dens+Mtr3_dens+Rrp40_dens+Rrp42_dens+Ski6_dens+Rrp43_dens+Rrp46_dens

Rrp6=Rrp6_1+Rrp6_2+Rrp6_3

simo.set_super_rigid_body_from_hierarchies(Rrp6)

simo.set_super_rigid_body_from_hierarchies(Lrp1+Rrp6+Rrp43+Rrp4)
simo.set_super_rigid_body_from_hierarchies(Lrp1+Rrp6)
simo.set_super_rigid_body_from_hierarchies(Rrp6+Rrp43)
simo.set_super_rigid_body_from_hierarchies(Rrp6+Rrp4)
simo.set_super_rigid_body_from_hierarchies(Dis3+Rrp45)
simo.set_super_rigid_body_from_hierarchies(Csl4+Rrp42)
simo.set_super_rigid_body_from_hierarchies(Dis3+Rrp45+Rrp4+Mtr3+Rrp40+Rrp42+Ski6+Rrp43+Rrp46+Lrp1+Rrp6)

simo.set_floppy_bodies()

