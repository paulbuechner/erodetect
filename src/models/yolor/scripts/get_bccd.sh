#!/bin/bash
# Script credit to https://github.com/ultralytics/yolov5
# BCCD BCCD Dataset from https://public.roboflow.com/object-detection/bccd
# Download command: bash scripts/get_bccd.sh
# Default dataset location is next to /yolor:
#   /parent_folder
#     /data/bccd
#     /yolor

# Download/unzip labels
d='../data/bccd/' # unzip directory
url=https://public.roboflow.com/ds/OD25lP5osO?key=XlW7qHAm5F
f='bccd.zip' # MB
echo 'Downloading' $url$f ' ...'
curl -L $url -o $f && unzip -q $f -d $d && rm $f & # download, unzip, remove in background
wait # finish background tasks
