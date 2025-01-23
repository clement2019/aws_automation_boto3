#!/bin/zsh
for b in $(aws s3 ls | cut -d" " -f3)
do
  echo -n $b
  if [[ "$(aws s3api list-objects-v2 --bucket $b --max-items 1)" == "" ]]
  then
    echo " BUCKET EMPTY"
  else
    echo ""
  fi
done