#!/bin/bash

# Create a temporary filename
export nano=`date +%s%N`

export OUT=/tmp/$nano.wav

while IFS='=' read -r -d '&' key value; do
  case $key in
    image)
      IMAGE=$value
      ;;
   esac
done <<EOF
${Http_Query}&
EOF



cat - > ${OUT}
pocketsphinx_continuous -infile ${OUT} -logfn ${IMAGE}.txt 
 
rm  ${OUT}


