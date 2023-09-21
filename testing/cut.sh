#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


# Need to make files to test with...
echo -e "${_C}Creating data/TMP_people.csv with the built-in paste tool...${_Z}"
paste -d, data/names8 data/ages8 data/colors8 data/verbs8 > data/TMP_people.csv
echo -e "${_C}Creating data/TMP_kids.csv with the built-in paste tool...${_Z}"
paste -d, data/num10 data/names10 data/words5 > data/TMP_kids.csv
echo

# clean these files up when the script exits
trap 'echo -e "${_C}Cleaning up temporary CSV files...${_Z}"; rm -f data/TMP_people.csv data/TMP_kids.csv' EXIT

good
echodo $PYTHON src/tt.py cut data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 2 data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 2,4 data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 4,2 data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 2,2,2 data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 2 data/TMP_kids.csv data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 13 data/TMP_people.csv
echodo $PYTHON src/tt.py cut -f 3 data/TMP_kids.csv

error
echodo $PYTHON src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity
echodo $PYTHON src/tt.py cut
echodo $PYTHON src/tt.py cut -f
echodo $PYTHON src/tt.py cut -f 0,-1 data/let3
echodo $PYTHON src/tt.py cut -f 1,2
