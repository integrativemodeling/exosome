import sys
sys.path.append('/veena1/home/pellarin/imp-projects/XL_analysis/src/')
import xltable
import glob




### data labels
ddir='data/'

cluster_directory="kmeans_weight_500_2/cluster.1/"

field_map={}
field_map["prot1"]='Protein 1'
field_map["prot2"]='Protein 2'
field_map["res1"]='Residue1'
field_map["res2"]='Residue2'
field_map["score"]='Score'


prot_list=["Dis3","Rrp45","Rrp4","Csl4","Mtr3","Rrp40","Rrp42","Ski6","Rrp46_gfp","Rrp43","Lrp1","Rrp6"]


                                    

xlt=xltable.XLTable(contact_threshold=30)
xlt.load_crosslinks("../data/exosome_XLMS_column07012014.csv",field_map)
for prot in prot_list:
    if prot=="MPP6": 
       fastaprot="Mpp6"
    else:
       fastaprot=prot
    xlt.load_sequence_from_fasta_file(fasta_file="../data/exosome.fasta",
                                  id_in_fasta_file=fastaprot,
                                  protein_name=prot)  


for rmf in glob.glob(cluster_directory+"*.rmf3")[0::10]:
   xlt.load_rmf_coordinates(rmf,0,prot_list)

### creating contact map
xlt.setup_contact_map()

### plotting

xlt.plot_table(prot_listx=prot_list,
           prot_listy=prot_list,
           alphablend=0.4,
           scale_symbol_size=1.5,
           gap_between_components=50,
           filename=cluster_directory+"/XL_table_tail.pdf",
           contactmap=True,
           crosslink_threshold=35.0,
           display_residue_pairs=False,
           color_crosslinks_by_distance=False)
