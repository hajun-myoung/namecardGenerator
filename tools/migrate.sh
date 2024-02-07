DIR="./tools/"
if [ -d "$DIR" ]; then
  # Take action if $DIR exists. #
  echo "You looks like in root Directory. Moving to ${DIR}..."
  cd ${DIR}
fi

cd ../additionalImages
cp ./*.png ../images/
rm ./*.png

cd ../additionalNamecards
cp ./*.png ../namecards/
rm ./*.png

cd ..
