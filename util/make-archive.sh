#!/bin/sh -e

# Simple script to make .zip archives of this repository, suitable for
# upload to Zenodo or a similar DOI-providing service. Unlike Zenodo's
# own GitHub integration (or 'git archive') the repository is split into
# several smaller archives, so that users don't have to download enormous
# archives containing trajectories just to get a small file like a Python
# script or alignment.

ARCHIVE_DIR=for_archival
REPO=exosome

if [ $# -ne 1 ]; then
  echo "Usage: $0 tag"
  exit 1
fi
if [ -e ${ARCHIVE_DIR} ]; then
  echo "The ${ARCHIVE_DIR} directory already exists - please delete it first"
  exit 1
fi
TAG=$1
mkdir ${ARCHIVE_DIR}
TOPDIR=${ARCHIVE_DIR}/${REPO}-${TAG}

zip_subdir() {
  local SUBDIR=$1
  local ZIPNAME=$2

  BASE=`basename ${SUBDIR}`
  CWD=`pwd`
  (cd ${TOPDIR}/${SUBDIR}/.. && zip -r ${CWD}/${ARCHIVE_DIR}/${ZIPNAME} ${BASE})
  rm -rf ${TOPDIR}/${SUBDIR}
  mkdir ${TOPDIR}/${SUBDIR}
  cat > ${TOPDIR}/${SUBDIR}/README.txt <<END
The files in this directory can be found in the ${ZIPNAME} file
at the same DOI where this archive is available.
END
}

git archive --format=tar --prefix=${TOPDIR}/ ${TAG} \
    | tar -xf -

# Put larger directories in their own zipfiles
zip_subdir modeling-scripts_Ski7.2/output Ski7.2-output.zip
zip_subdir modeling-scripts_Rrp6.2/output Rrp6.2-output.zip
zip_subdir Ski7.analysis/kmeans_weight_500_2/cluster.0 Ski7-cluster0.zip
zip_subdir Ski7.analysis/kmeans_weight_500_2/cluster.1 Ski7-cluster1.zip
zip_subdir Rrp6.analysis/kmeans_weight_500_2/cluster.0 Rrp6-cluster0.zip
zip_subdir Rrp6.analysis/kmeans_weight_500_2/cluster.1 Rrp6-cluster1.zip

# Put everything else in the toplevel zipfile
(cd ${ARCHIVE_DIR} && zip -r ${REPO}-${TAG}.zip ${REPO}-${TAG})
rm -rf ${TOPDIR}

echo "zip files created in ${ARCHIVE_DIR}. Upload them and then"
echo "delete that directory."
