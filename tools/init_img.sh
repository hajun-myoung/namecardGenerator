DIR="./tools/"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  echo "You looks like in root Directory. Moving to ${DIR}..."
  cd ${DIR}
fi


cd ../namecards
rm -f *.png
cd ../
