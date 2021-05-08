#!/bin/bash

# Create a temporary filename
export nano=`date +%s%N`

export OUT=/tmp/$nano.mp3

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

export file=`echo ${IMAGE:0:4}.xhtml`
curl -d $file http://192.168.1.223:8080/function/getobject > /tmp/$file

python -m aeneas.tools.execute_task \
   ${OUT} \
   /tmp/$file \
   "task_language=eng|os_task_file_format=json|is_text_type=plain" \
  /tmp/$IMAGE.json  > /tmp/output.txt 
rm  ${OUT}
rm /tmp/$file
cat /tmp/$IMAGE.json
rm  /tmp/$IMAGE.json

