import IMP
import IMP.pmi
import IMP.pmi.metadata
import IMP.pmi.macros
import sys

model=IMP.Model()

# initialize the macro

mc=IMP.pmi.macros.AnalysisReplicaExchange0(model,
                                        stat_file_name_suffix="stat",     # don't change
                                        merge_directories=[ # change this list splitting the runs or adding new runs
                                        "../modeling-scripts_Rrp6.1/",
					"../modeling-scripts_Rrp6.2/"
        				],
                                        global_output_directory="./output/") # don't change
if '--mmcif' in sys.argv:
    mc.test_mode = simo.dry_run
    for po in simo.protocol_output:
        mc.add_protocol_output(po)

# fields that have to be extracted for the stat file

feature_list=["ISDCrossLinkMS_Distance_intrarb",
              "ISDCrossLinkMS_Distance_interrb",
              "ISDCrossLinkMS_Data_Score",
              "GaussianEMRestraint_None",
              "SimplifiedModel_Linker_Score_None",
              "ISDCrossLinkMS_Psi",
              "ISDCrossLinkMS_Sigma"]

# Dictionary of densities to be calculated
# the key is the name of the file and the value if the selection
# example:
#              {"med17-CTD":[(200,300,"med17")],"med17-CTD.med14":[(200,300,"med17"),"med14"]   }

reduced_density_dict={"MPP6":["MPP6"],
                  "Rrp6":["Rrp6"],
                  "Lrp1":["Lrp1"],
                  "Rrp46_gfp":[(246,229+246,"Rrp46_gfp")]}

# list of component names needed to calculate the RMSD for the clustering

names=["Rrp6","Dis3"]
aligncomp=["Dis3"]

components_names={}
for i in names:
    components_names[i]=i

align_component_names={}
for i in aligncomp:
    align_component_names[i]=i


nclusters=2                                       # number of clusters needed by kmeans
mc.clustering("SimplifiedModel_Total_Score_None",  # don't change, field where to find the score
              "rmf_file",                          # don't change, field where to find the path for the rmf_file
              "rmf_frame_index",                   # don't change, field for the frame index
              prefiltervalue=365,               # prefilter the models by score
              number_of_best_scoring_models=200,   # number of models to be clustered
              alignment_components=align_component_names,      # don't change, (list of proteins you want to use for structural alignment
              rmsd_calculation_components=components_names, # list of proteins used to calculated the rmsd
              distance_matrix_file="distance.rawmatrix.pkl", # save the distance matrix
              outputdir="kmeans_weight_500_"+str(nclusters)+"/",  # directory name for the clustering
              feature_keys=feature_list,                     # extract these fields from the stat file
              load_distance_matrix_file=False,                # skip the matrix calcuklation and read the precalculated matrix
              skip_clustering=False,                         # skip clustering
              display_plot=False,                            # display the heat map plot of the distance matrix
              exit_after_display=False,                      # exit after having displayed the distance matrix plot
              get_every=1,                                   # skip structures for faster computation
              number_of_clusters=nclusters,                  # number of clusters to be used by kmeans algorithm
              voxel_size=3.0,                                # voxel size of the mrc files
              density_custom_ranges=reduced_density_dict)    # setup the list of densities to be calculated


if '--mmcif' in sys.argv:
    # Point to deposited ensembles in DCD format
    dcds = []
    for i in range(nclusters):
        r = IMP.pmi.metadata.Repository(doi="10.5281/zenodo.583313",
                       url="https://zenodo.org/record/583313/"
                           "files/Rrp6-cluster%d.dcd" % i)
        dcds.append(IMP.pmi.metadata.FileLocation(path='.', repo=r,
                            details="All models in cluster %d" % (i+1)))
    for po in simo.protocol_output:
        if hasattr(po, 'set_ensemble_file'):
            for i, dcd in enumerate(dcds):
                po.set_ensemble_file(i, dcd)
