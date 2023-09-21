#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


good
echodo $PYTHON src/tt.py head data/let3
echodo $PYTHON src/tt.py head data/names10
echodo $PYTHON src/tt.py head data/words200
echodo $PYTHON src/tt.py head -n 13 data/words200
echodo $PYTHON src/tt.py head -n 3 data/complexity
echodo $PYTHON src/tt.py head -n 5 data/ages8 data/names8 data/words200
echodo $PYTHON src/tt.py head -n 3 data/complexity data/debugging

error
echodo $PYTHON src/tt.py head data/let3 DOES_NOT_EXIST data/complexity
echodo $PYTHON src/tt.py head
echodo $PYTHON src/tt.py head -n
echodo $PYTHON src/tt.py head -n seven
echodo $PYTHON src/tt.py head -n -7
echodo $PYTHON src/tt.py head -n 7
