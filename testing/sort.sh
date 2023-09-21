#!/usr/bin/env bash

source testing/config.sh
source testing/functions.sh


good
echodo $PYTHON src/tt.py sort data/colors8
echodo $PYTHON src/tt.py sort data/complexity
echodo $PYTHON src/tt.py sort data/colors8 data/names10
echodo $PYTHON src/tt.py sort data/complexity data/debugging
echodo $PYTHON src/tt.py sort data/names10 data/colors8
echodo $PYTHON src/tt.py sort data/debugging data/complexity
echodo $PYTHON src/tt.py sort data/random20
echodo "$PYTHON src/tt.py sort data/colors8 > sortedColors8"
echodo $PYTHON src/tt.py tac sortedColors8
echodo rm sortedColors8


error
echodo $PYTHON src/tt.py sort data/let3 DOES_NOT_EXIST data/complexity
echodo $PYTHON src/tt.py sort
